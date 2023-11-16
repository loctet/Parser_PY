import z3
from Extension import generateFuntionsFormulas, replace_assertion
from SafeVariableAssignment import SafeVariableAssignment as SafeVars
from VariableDeclarationConverter import VariableDeclarationConverter as VarDefConv
from ParticipantManager import ParticipantManager
from MessagesTemplates import MessagesTemplates

class SolverGenerator:
    def __init__(self):
        self.str_code = ""
        self.solvers = {}
        self.deploy_init_var_val = []
        self.var_names = []
        self.solvers['start'] = []
        self.solvers['starts'] = [] 
        self.paticipants = ParticipantManager()
        
    #Append to the global Code Model
    def append(self, str):
       self.str_code += str + "\n"
       
    def quantifier_closure(self, formula, variables = [], quantifier = "ForAll"):
        return f"{quantifier}([{','.join(variables)}], {formula})" if len(variables) > 0 else formula
    
    def z3_post_condition(self, postC):
        formula = ", ".join(postC.replace(':=', ' == ').split("&"))
        return "True" if postC.strip() == "" else (f"And({formula})")
    
    def get_vars_names_from_input(self, input_c = ""):
        resuls  = VarDefConv.convert_to_z3_declarations(input_c, [])
        return resuls[2]
    
    def add_assertion(self, pre, otherPrecs, func = 'start', inputs = [], postC = "", add = True):
        
        data = self.solvers.get(func, [])
        if not data:
            self.solvers[func] = []
        
        pre = replace_assertion(pre)
        otherPrecs = [replace_assertion(item) for item in otherPrecs]
        otherPrecs = otherPrecs if len(otherPrecs) > 0 else ["True"]
        sVarUpdate, global_vars  = SafeVars.safe_variable_assignment(postC, f'solver_'+ f'_{func}_{len(self.solvers[func])}')
        sparams, deploy_init_var_val, var_names = VarDefConv.convert_to_z3_declarations(";".join([x for x in inputs if x != ""]), self.deploy_init_var_val)
        
        
        hypothesis = self.quantifier_closure(self.z3_post_condition(postC), self.var_names + var_names)
        thesis = f'Or({",".join([self.quantifier_closure(otherPrecs[i], self.get_vars_names_from_input(inputs[i]), "Exists") for i in range(len(otherPrecs))])})' if len(otherPrecs) > 0 else "True"
       
        if func == 'start':
            #self.deploy_init_var_val.append(VarDefConv.convert_to_z3_int_assignement(postC))
            self.append(sparams)
            self.append(VarDefConv.convert_to_z3_int_assignement(postC))
        
        name_func = f'_{func}_{len(self.solvers[func])}'
        result = {
            'sname': f'solver_{func}',
            'snameF': name_func,
            'sparams': "\n    ".join(sparams.split('\n')),
            'sVarUpdate': sVarUpdate,
            'sglobalVars': global_vars,
            'spre': f"{pre}",
            'spost': f"solver_{name_func}.add(And(_pre == z3.sat, Or({','.join(otherPrecs)}))",
            'spost_imply': f"solver_{name_func}.add({self.quantifier_closure(f'Implies({hypothesis}, {thesis})', self.var_names)})"
        }
        if add :  
            self.solvers[func].append(result)
        return result

    def generate_solver_code(self, result_var):
        #create formulas functions
        self.append(generateFuntionsFormulas())
        
        #Add roles to the model 
        for role  in self.paticipants.roles:
            self.append(self.paticipants.roles[role]["declaration"])
            self.append("\n".join(self.paticipants.roles[role]["list"]))
          
        self.append(MessagesTemplates.getResetGlobalFunction("\n    ".join(self.deploy_init_var_val), self.var_names))
        
        checks = []
        for s in self.solvers:
           self.append("\n")
           for item in self.solvers[s]:
                self.append(MessagesTemplates.getFunctionActionDefinition(item))
                checks.append(f"{item['snameF']}(True)")
                
                
        self.append(f"{result_var} = (" + " and ".join(checks) + ")")
        self.append(MessagesTemplates.getResultCheckPart())
        return self.str_code

    def dump_models(self):
        code = ""
        for s in self.solvers:
           for item in self.solvers[s]:
                code += f"\n\nprint('{item['snameF']}: ',{item['snameF']}(True))"
        return code 