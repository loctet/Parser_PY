import copy
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
        self.paticipants = ParticipantManager()
        
    #Append to the global Code Model
    def append(self, str):
       self.str_code += str + "\n"
       
    def quantifier_closure(self, formula, variables = [], quantifier = "ForAll"):
        return f"{quantifier}([{','.join(variables)}], {formula})" if len(variables) > 0 else formula
    
    def z3_post_condition(self, postC):
        if  postC.strip() == "" :
            return "True"
        
        _list = postC.split("&")
        parts = []
        for item in _list:
            if item.strip() == "":
                print(f"{postC} in not correct")
                exit()
                
            _varname, _assign = [a.strip() for a in item.split(":=")]
            if _varname in self.var_names and self.var_names[_varname] == 'string':
                parts.append(f"{_varname}.eq({_assign})")
            else:
                parts.append(f"{_varname} == {_assign}")
        formula = ", ".join(parts)
    
        return  f"And({formula})"
    
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
        for action in indexes:
            if len(indexes[action]) == 1:
                continue
            for i in range(len(indexes[action])):
                grouped = copy.deepcopy(indexes[action])
                index = grouped[i]
                hypo = other_precs[index]
                
                grouped.remove(index)
                result.append(f"ForAll([{','.join(self.get_vars_names_from_input(inputs[index]))}], Implies({hypo},And(Not({') , Not('.join([other_precs[j] for j in grouped])}))))")

        return f'And({",".join(result)})' if result else "True"

    def pre_condition_not_having_old_vars(self, preC):
        if len(PatternChecker.get_all_old_variables(preC)) > 0:
            print(f"{preC} should not contain _old variables")
            exit() 
    
    def add_assertion(self, pre, otherPrecs,inputs, actions, postC = "", add = True):
        self.pre_condition_not_having_old_vars(pre)
        action = actions[0]
        inputs = (self.add_old_var_from_precs_and_inputs([postC], [inputs[0]])[0], self.add_old_var_from_precs_and_inputs(otherPrecs, inputs[1]))
        data = self.solvers.get(action, [])
        if not data:
            self.solvers[action] = []
        
        pre = replace_assertion(pre)
        sVarUpdate, global_vars  = SafeVars.safe_variable_assignment(postC, f'solver__{action}_{len(self.solvers[action])}')
        sparams, deploy_init_var_val, var_names = VarDefConv.convert_to_z3_declarations(";".join([x for x in (inputs[1]+[inputs[0]]) if x != ""]))
        
        hypothesis = self.z3_post_condition(postC)
        thesis = f'Or({",".join([self.quantifier_closure(otherPrecs[i], self.get_vars_names_from_input(inputs[1][i]), "Exists") for i in range(len(otherPrecs))])})' if len(otherPrecs) > 0 else "True"
        thesis_non_eps = self.get_formula_for_determinism_at_stage(otherPrecs, inputs[1], actions[1])
        
        name_func = f'_{action}_{len(self.solvers[action])}'
        
        result = {
            'sname': f'solver_{action}',
            'snameF': name_func,
            'sparams': "\n    ".join(sparams.split('\n')),
            'sglobalVars': global_vars,
            'sformula': self.quantifier_closure(f'Implies({hypothesis}, {thesis})', list(self.var_names.keys()) + list(self.get_vars_names_from_input(inputs[0]).keys())),
            'epsformula': thesis_non_eps
        }
        if add :  
            self.solvers[action].append(result)
        return result

    def generate_solver_code(self, result_var):
        #create formulas functions
        self.append(generateFuntionsFormulas())
        
        #Add roles to the model 
        for role  in self.paticipants.roles:
            self.append(self.paticipants.roles[role]["declaration"])
            self.append("\n".join(self.paticipants.roles[role]["list"]))
          
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
