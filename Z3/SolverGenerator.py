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
        self.solvers['start'] = []
        self.solvers['starts'] = [] 
        self.paticipants = ParticipantManager()
        
    #Append to the global Code Model
    def append(self, str):
       self.str_code += str + "\n"

    def add_assertion(self, pre, otherPrecs, func = 'start', inputs = [], postC = ""):
        
        data = self.solvers.get(func, [])
        if not data:
            self.solvers[func] = []
        
        pre = replace_assertion(pre)
        otherPrecs = [replace_assertion(item) for item in otherPrecs]
        otherPrecs = otherPrecs if len(otherPrecs) > 0 else ["True"]
        sVarUpdate, global_vars  = SafeVars.safe_variable_assignment(postC, f'solver_'+ f'_{func}_{len(self.solvers[func])}')
        
        sparams, self.deploy_init_var_val = VarDefConv.convert_to_z3_declarations(";".join(inputs), self.deploy_init_var_val)
        
        self.solvers[func].append({
            'sname': f'solver_{func}',
            'snameF': f'_{func}_{len(self.solvers[func])}',
            'sparams': sparams,
            'sVarUpdate': sVarUpdate,
            'sglobalVars': global_vars,
            'spre': f"{pre}",
            'spost': f"Or({','.join(otherPrecs)})"
        })

    def generate_solver_code(self, result_var):
        #create formulas functions
        self.append(generateFuntionsFormulas())
        
        #Add roles to the model 
        for role  in self.paticipants.roles:
            self.append(self.paticipants.roles[role]["declaration"])
            self.append("\n".join(self.paticipants.roles[role]["list"]))
          
        self.append(MessagesTemplates.getResetGlobalFunction("\n    ".join(self.deploy_init_var_val) ))
        
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