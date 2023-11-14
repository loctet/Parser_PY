class MessagesTemplates:
    
    @staticmethod
    def getFunctionActionDefinition(funtionData):
        item = funtionData
        return f"""
def {item['snameF']}(reset = False):
    {item['sglobalVars']}
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    {item["sparams"]}
    
    #building the solver for the predancontion
    solver_{item['snameF']} = z3.Solver()
    #set the stack init
    solver_{item['snameF']}.push()
    solver_{item['snameF']}.add({item['spre']})
    #getting the check result of the precondition
    _pre = solver_{item['snameF']}.check()
    
    #remove the pre con to check the post or other precond
    solver_{item['snameF']}.pop()
    
    #update the states variable 
    {item['sVarUpdate']}
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver_{item['snameF']}.add(And(_pre == z3.sat, {item['spost']}))
    return solver_{item['snameF']}.check() == z3.sat
    """
    
    @staticmethod
    def getResultCheckPart():
        return f"""
if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        """
        
    @staticmethod
    def getResetGlobalFunction(deploy_vars, var_names = []):
        var_names = ("global " + ", ".join(var_names)) if len(var_names) > 0 else ""
        return f"""
def reset_deploy_vars():
    {var_names}
    {deploy_vars}
"""

    @staticmethod
    def getFunctionVariableDeclaration(variable_name, value,  solver_name):
        partern = "r'[^\[\]{}()]*[^\[\]{}()\s]'"
        return f"""
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = {partern}
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "{variable_name.strip()}")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        {variable_name} = {value}
        {solver_name}.add({variable_name} == {variable_name})
    else:
        raise NameError(f"State Variable '{{match.group(0)}}' does not exist")
"""

    @staticmethod
    def getMessageWhenVarNotGlobal(assignation_str, solver_name):
        return f"""
    #{assignation_str} do not meet the assignations requirements
    {solver_name}.add(False)              
            """