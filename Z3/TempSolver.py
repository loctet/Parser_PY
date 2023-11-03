from Extension import *

class TempSolver(object):
    str_code = """"""
    solvers = {}
    roles = {}
    deploy_init_var_val = []

    def __init__(self):
       self.solvers['starts'] = []
    
    
    def convert_to_z3_declarations(self, declarations_str, deploy = True):
        declarations = declarations_str.split(';')  # Split input into separate variable declarations
        declarations = [declaration.strip() for declaration in declarations if declaration.strip()]  # Remove any empty declarations
        result = ""
        for declaration in declarations:
            # Split each declaration into type, variable name, and optional initial value
            parts = declaration.split()
            if len(parts) >= 2:
                var_type, var_name = parts[:2]
                z3_var = None
                z3_var_init = None

                if len(parts) > 2:
                    initial_value = parts[3]  # Assuming the initial value is after ":="

                    # Create Z3 variables based on the declared type and assign the initial value
                    if var_type == 'int':
                        initial_value = int(initial_value)
                        z3_var = f"{var_name} = Int('{var_name}')"
                        z3_var_init = f"{var_name} = {initial_value}"

                    if var_type == 'string':
                        initial_value = str(initial_value)
                        z3_var = f"{var_name} = String('{var_name}')"
                        z3_var_init = f"{var_name} = \"{initial_value}\""
                    
                    elif var_type == 'bool':
                        initial_value = bool(initial_value)
                        z3_var = f"{var_name} = Bool('{var_name}')"
                        z3_var_init = f"{var_name} = {initial_value}"
                        
                    elif var_type == 'set':
                        z3_var = f"{var_name} = Array('{var_name}', IntSort(), IntSort())"

                    elif var_type == 'array':
                        z3_var = f"{var_name} = []"
                        z3_var_init = f"{var_name} = {initial_value}"
                else:
                    # Create Z3 variables without initial values
                    if var_type == 'int':
                        z3_var = f"{var_name} = Int('{var_name}')"
                    if var_type == 'string':
                        z3_var = f"{var_name} = String('{var_name}')"
                    elif var_type == 'float':
                        z3_var = f"{var_name} = Real('{var_name}')"
                    elif var_type == 'bool':
                        z3_var = f"{var_name} = Bool('{var_name}')"
                    elif var_type == 'set':
                        z3_var = f"{var_name} = Array('{var_name}', IntSort(), IntSort())"
                    elif var_type == 'array':
                        z3_var = f"{var_name} = []"

                if z3_var is not None:
                    result += f"{z3_var}\n"
                    if z3_var_init is not None:
                        result += f"{z3_var_init}\n"
                        self.deploy_init_var_val.append(z3_var_init)
        return result
    
    
    def safe_variable_assignment(self, assignation_str):
        # Split the input string into individual assignments
        assignments = assignation_str.split(';')

        result = []

        for assignment in assignments:
            # Split each assignment into variable name and value
            parts = assignment.strip().split(':=')
            
            # Ensure there are exactly two parts (variable name and value)
            if len(parts) != 2:
                return ""

            variable_name, value = parts
            partern = "r'[^\[\]{}()]*[^\[\]{}()\s]'"
            result.append(f"""
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = {partern}
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "{variable_name.strip()}")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        {variable_name} = {value}
    else:
        raise NameError(f"State Variable '{{match.group(0)}}' does not exist")
""")
        # Join the generated assignments with newline characters
        generated_code = "\n".join(result)

        return generated_code 
    
    #add a participant
    def add_participant(self, role, participant, index):
        if role not in self.roles:
            self.roles[role] = {
                'name': role,
                'declaration': f"role_{role} = Array('{role}',IntSort() , StringSort())",
                'list': []
            }
        self.roles[role]['list'].append(f"Store(role_{role}, {index}, String('{participant}'))")

    def if_part_in_subset(self, participant, role):
        if role not in self.roles:
            return False
        return participant in self.roles[role]
    
    #Participants Adding list
    def add_participants(self, data):
        for entry in data:
            index = 0
            for participant in entry["participants"]:
                self.add_participant(entry["role"], participant, index)
                index += 1

    #Append to the global Code Model
    def append(self, str):
       self.str_code += str + "\n"

    def add_assertion(self, pre, post, func = 'starts', params = "", updateVars = ""):
        if func not in self.solvers:
            self.solvers[func] = []

        pre = replace_assertion(pre)
        post = replace_assertion(post)

        self.solvers[func].append({
            'sname': f'solver_{func}',
            'snameF': f'_{func}_{len(self.solvers[func])}',
            'sparams': self.convert_to_z3_declarations(params),
            'sVarUpdate': self.safe_variable_assignment(updateVars),
            'spre': f"{pre}",
            'spost': f"{post}"
        })

    def generate_solver_code(self, result_var):
        #create formulas functions
        self.append(generateFormulas())
        
        #Add roles to the model 
        for role  in self.roles:
            self.append(self.roles[role]["declaration"])
            self.append("\n".join(self.roles[role]["list"]))
            
        deploy_vars = "\n    ".join(self.deploy_init_var_val)    
        self.append(f"""
def reset_deploy_vars():
    {deploy_vars}
""")
        
        checks = []
        for s in self.solvers:
           self.append("\n")
           for item in self.solvers[s]:
                self.append(f"""
def {item['snameF']}(reset = True):
    if reset:
        reset_deploy_vars()
    {item["sparams"]}
    {item['sVarUpdate']}
    solver_{item['snameF']} = z3.Solver()
    solver_{item['snameF']}.push()
    solver_{item['snameF']}.add({item['spre']})
    _pre = solver_{item['snameF']}.check()
    solver_{item['snameF']}.pop()
    solver_{item['snameF']}.add(And(_pre == z3.sat, {item['spost']}))
    return solver_{item['snameF']}.check() == z3.sat
                            """)
                checks.append(f"{item['snameF']}()")
        self.append(f"{result_var} = (" + " and ".join(checks) + ")")
        return self.str_code

    def dump_models(self):
        code = ""
        for s in self.solvers:
           self.append("\n")
           for item in self.solvers[s]:
                code += f"print({item['snamePr']}.model()) if {item['snamePr']}.check() == z3.sat else print('{item['snamePr']}')\n"
                code += f"print({item['snamePo']}.model()) if {item['snamePo']}.check() == z3.sat else print('{item['snamePo']}')\n"
        return code