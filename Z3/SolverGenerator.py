import copy
import pickle
from PatternChecker import *
from Extension import generateFuntionsFormulas, replace_assertion
from SafeVariableAssignment import SafeVariableAssignment as SafeVars
from VariableDeclarationConverter import VariableDeclarationConverter as VarDefConv
from ParticipantManager import ParticipantManager
from MessagesTemplates import MessagesTemplates
from collections import defaultdict


class SolverGenerator:
    def __init__(self):
        self.str_code = ""
        self.solvers = {}
        self.deploy_init_var_val = {}
        self.var_names = {}
        self.solvers['start'] = []
        self.solvers['starts'] = [] 
        self.participants = ParticipantManager()
        
    #Append to the global Code Model
    def append(self, str):
       self.str_code += str + "\n"
       
    def quantifier_closure(self, formula, variables = [], quantifier = "ForAll"):
        return f"{quantifier}([{','.join(variables)}], {formula})" if len(variables) > 0 else formula
    
    
    def get_vars_names_from_input(self, input_c):
        resuls  = VarDefConv.convert_to_z3_declarations(input_c)
        return resuls[2]
    
    def add_old_var_from_precs_and_inputs(self, otherPrecs, inputs): 
        for i in range(len(otherPrecs)):
            try:
                inputs[i] = ";".join([ item for item in inputs[i].split(";") if item.strip() != ""] + [ f"{self.var_names[item.replace('_old', '')]} {item}"  for item in PatternChecker.get_all_old_variables(otherPrecs[i])])
            except Exception as e:
                print(f"KeyError: {e}")
                exit()
        return inputs

    def get_formula_for_determinism_at_stage(self, other_precs, inputs, actions):
        indexes = defaultdict(list)

        for i, action in enumerate(actions):
            indexes[action].append(i)

        result = []

        for action, indices in indexes.items():
            if len(indices) == 1:
                continue

            for i, index in enumerate(indices):
                grouped = copy.deepcopy(indices)
                hypothesis = other_precs[index]
                grouped.pop(i)
                var_in = self.get_vars_names_from_input(inputs[index])
                implication_part = f'And(Not({") , Not(".join([other_precs[j] for j in grouped])}))'
                result.append(f"ForAll([{','.join(var_in)}], Implies({hypothesis}, {implication_part}))") if var_in else f"Implies({hypothesis}, {implication_part})"

        return f'And({",".join(result)})' if result else "True"
    
    def get_formula_for_participant_check(self, participants, caller):
        roles_list = []
        result = []
        
        try:
            user, roleU = next(iter(caller.items())) if len(caller) == 1 else ["", ""]
            for p, role in participants["existingParticipants"].items():
                self.participants.add_participant(role, p)
                roles_list.append(role)
                
            for p, role in participants["newParticipants"].items():
                self.participants.add_participant(role, p)
                roles_list.append(role)
            
            roles_list = list(set(roles_list))
            if roleU in roles_list:
                self.participants.add_participant(roleU, user) 
            elif roleU.strip() == "":
                result = [f"'{user}' in {role}_role" for role in roles_list]
                return f"Or({','.join(result) if result else 'False'})" if len(roles_list) > 0 else "True"
            
            roles_list_str = "', '".join(roles_list) 
            return f"'{roleU}' in ['{roles_list_str}']" if len(roles_list) > 0 else "True"
            
        except Exception as e:
            print(f"Participant Error: {e}")

        return "True"

    
    """
    Add an assertion to the solvers data structure based on provided conditions and inputs.

    Parameters:
    - pre (str): The precondition of the assertion.
    - otherPrecs (list): List of other preconditions.
    - inputs (tuple): Tuple containing the inputs for the assertion. The first element is the input string, and the second element is the list of corresponding inputs of other transitions.
    - actions (list): List of actions associated with the assertion. first is the current action and secons is the list of other actions
    - postC (str): The post-condition of the assertion. Defaults to an empty string.
    - add (bool): Flag indicating whether to add the assertion to the solvers data structure. Defaults to True.

    Returns:
    dict: A dictionary containing information about the added assertion.

    The function processes the given conditions and inputs, replaces variables with "_old" versions, and generates Z3-compatible formulas for the assertion. It also handles the addition of the assertion to the solvers data structure.

    """
    def add_assertion(self, pre, otherPrecs, inputs, actions, postC = "", participants = [], caller = {}):
        formula_for_participant_check = self.get_formula_for_participant_check(participants, caller)
        
        # Check and handle special cases in the pre and post conditions
        PatternChecker.pre_condition_not_having_old_vars(pre, postC)

        # Extract Z3-compatible post conditions
        _postC_A, _post_variable = PatternChecker.z3_post_condition(postC, self.var_names)

        # Select the first action (currect transition's action)
        action = actions[0]

        # Replace variables in pre with their "_old" versions
        data = PatternChecker.replace_var_with_old_in_pre(pre, _post_variable, self.var_names)
        # change the precondition to the updatd one
        pre = data[0]

        # Update the inputs with the new "_old" variables
        inputs = (";".join(inputs[0].split(';') + data[1]), inputs[1])
        inputs = (
            self.add_old_var_from_precs_and_inputs([postC], [inputs[0]])[0],
            self.add_old_var_from_precs_and_inputs(otherPrecs, inputs[1])
        )

        # Initialize or get the data associated with the current action
        data = self.solvers.get(action, [])
        if not data:
            self.solvers[action] = []

        # Replace assertion in pre
        pre = replace_assertion(pre)

        # Generate safe variable updates and global variables
        sVarUpdate, global_vars = SafeVars.safe_variable_assignment(postC, f'solver__{action}_{len(self.solvers[action])}')

        # Convert variables and declarations to Z3 format
        sparams, deploy_init_var_val, var_names = VarDefConv.convert_to_z3_declarations(";".join([x for x in (inputs[1]+[inputs[0]]) if x != ""]))

        # Create the hypothesis and thesis for the assertion
        hypothesis = f"And({pre},{_postC_A})"
        thesis = f'Or({",".join([self.quantifier_closure(otherPrecs[i], self.get_vars_names_from_input(inputs[1][i]), "Exists") for i in range(len(otherPrecs))])})' if len(otherPrecs) > 0 else "True"
        thesis_non_eps = self.get_formula_for_determinism_at_stage(otherPrecs, inputs[1], actions[1])

        # Create a unique name for the function
        name_func = f'_{action}_{len(self.solvers[action])}'
        
        sformula = self.quantifier_closure(f'Implies({hypothesis}, {thesis})', list(self.var_names.keys()) + list(self.get_vars_names_from_input(inputs[0]).keys()))
        # Prepare the result dictionary
        result = {
            'sname': f'solver_{action}',
            'snameF': name_func,
            'sparams': "\n    ".join(sparams.split('\n')),
            'spre': pre,
            'sglobalVars': global_vars,
            'sformula': f"And({formula_for_participant_check}, {sformula})",
            'epsformula': thesis_non_eps
        }
        self.solvers[action].append(result)
        
        return result


    def generate_solver_code(self, result_var):
        #create formulas functions
        self.append(generateFuntionsFormulas())
        
        #Add roles to the model 
        for role  in self.participants.roles:
            self.append(self.participants.roles[role]["declaration"])
            self.append("\n".join(self.participants.roles[role]["list"]))
          
        checks = []
        for s in self.solvers:
           self.append("\n")
           for item in self.solvers[s]:
                self.append(MessagesTemplates.getFunctionActionDefinition(item))
                checks.append(f"{item['snameF']}()")
                
                
        self.append(f"{result_var} = (" + " and ".join(checks) + ")")
        self.append(MessagesTemplates.getResultCheckPart())
        return self.str_code

    def dump_models(self):
        code = "print('\\nFuntions minimized formula and satisfiability result :')"
        for s in self.solvers:
           for item in self.solvers[s]:
                code += f"\n\n{item['snameF']}(True)"
        return code 
