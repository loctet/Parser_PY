class VariableDeclarationConverter:
    @staticmethod
    def convert_to_z3_declarations(declarations_str, deploy_init_var_val = [], var_names = [],  deploy=True):
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
                var_names.append(var_name)
                
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
                        deploy_init_var_val.append(z3_var_init)
                        
        return [result, deploy_init_var_val, var_names]
