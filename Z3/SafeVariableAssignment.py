from PatternChecker import *
from MessagesTemplates import MessagesTemplates

class SafeVariableAssignment:
    @staticmethod
    def safe_variable_assignment(assignation_str, solver_name):
        result = []
        global_vars = []
        if not PatternChecker.follows_pattern(assignation_str):
            print(f"/!\Error: {assignation_str} do not meet the assignations requirements")
            result.append(MessagesTemplates.getMessageWhenVarNotGlobal(assignation_str, solver_name))
            return  "\n".join(result) 
        
        # Split the input string into individual assignments
        assignments = assignation_str.split('&')

        for assignment in assignments:
            # Split each assignment into variable name and value
            parts = assignment.strip().split(':=')
            
            # Ensure there are exactly two parts (variable name and value)
            if len(parts) != 2:
                return ["",""]
            
            variable_name, value = parts
            
            global_vars.append(f"global {variable_name}")
            result.append(MessagesTemplates.getFunctionVariableDeclaration(variable_name, value,  solver_name))
        # Join the generated assignments with newline characters
        return  ["\n".join(result), "\n    ".join(global_vars)]
    
   
    