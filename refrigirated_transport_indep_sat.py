from z3 import * 
from Z3.Extension import *

stage = Int('stage')
MaxHum = Int('MaxHum')
MinHum = Int('MinHum')
MaxTem = Int('MaxTem')
MinTem = Int('MinTem')
d = String('d')
cp = String('cp')
hum = Int('hum')
tem = Int('tem')

_hum = Int('_hum')
_tem = Int('_tem')
_hum = Int('_hum')
_tem = Int('_tem')
_cp = String('_cp')
_d = String('_d')

d =  _d


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))

def reset_deploy_vars():
    
    global stage , MaxHum , MinHum , MaxTem , MinTem , d , cp , hum , tem 
    stage = Int('stage')
    MaxHum = Int('MaxHum')
    MinHum = Int('MinHum')
    MaxTem = Int('MaxTem')
    MinTem = Int('MinTem')
    d = String('d')
    cp = String('cp')
    hum = Int('hum')
    tem = Int('tem')
    
    d =  _d





def _start_0(reset = False):
    global d 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _d = String('_d')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver()
    #set the stack init
    solver__start_0.push()
    solver__start_0.add(True)
    #getting the check result of the precondition
    _pre = solver__start_0.check()
    
    #remove the pre con to check the post or other precond
    solver__start_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "d")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        d  =  _d
        solver__start_0.add(d  == d )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__start_0.add(And(_pre == z3.sat, Or(And(d != cp, stage == 0),And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Or(stage == 0, stage == 1, stage == 2))))
    return solver__start_0.check() == z3.sat
    





def _ingestTel_0(reset = False):
    global tem 
    global hum 
    global stage 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_0 = z3.Solver()
    #set the stack init
    solver__ingestTel_0.push()
    solver__ingestTel_0.add(And(d != cp, stage == 0))
    #getting the check result of the precondition
    _pre = solver__ingestTel_0.check()
    
    #remove the pre con to check the post or other precond
    solver__ingestTel_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "tem")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        tem  =  _tem
        solver__ingestTel_0.add(tem  == tem )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "hum")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        hum  =  _hum
        solver__ingestTel_0.add(hum  == hum )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "stage")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        stage  =  1
        solver__ingestTel_0.add(stage  == stage )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__ingestTel_0.add(And(_pre == z3.sat, Or(And(d != cp, stage == 0),And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Or(stage == 0, stage == 1, stage == 2))))
    return solver__ingestTel_0.check() == z3.sat
    

def _ingestTel_1(reset = False):
    global hum 
    global tem 
    global stage 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_1 = z3.Solver()
    #set the stack init
    solver__ingestTel_1.push()
    solver__ingestTel_1.add(And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))
    #getting the check result of the precondition
    _pre = solver__ingestTel_1.check()
    
    #remove the pre con to check the post or other precond
    solver__ingestTel_1.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "hum")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        hum  =  _hum
        solver__ingestTel_1.add(hum  == hum )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "tem")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        tem  =  _tem
        solver__ingestTel_1.add(tem  == tem )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "stage")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        stage  =  3
        solver__ingestTel_1.add(stage  == stage )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__ingestTel_1.add(And(_pre == z3.sat, Or(True)))
    return solver__ingestTel_1.check() == z3.sat
    



def _transResp_0(reset = False):
    global stage 
    global cp 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    
    
    #building the solver for the predancontion
    solver__transResp_0 = z3.Solver()
    #set the stack init
    solver__transResp_0.push()
    solver__transResp_0.add(Or(stage == 0, stage == 1, stage == 2))
    #getting the check result of the precondition
    _pre = solver__transResp_0.check()
    
    #remove the pre con to check the post or other precond
    solver__transResp_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "stage")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        stage  =  1
        solver__transResp_0.add(stage  == stage )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "cp")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        cp  =  _cp
        solver__transResp_0.add(cp  == cp )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__transResp_0.add(And(_pre == z3.sat, Or(And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),stage == 2)))
    return solver__transResp_0.check() == z3.sat
    



def _ingestTel_b_1_0(reset = False):
    global tem 
    global stage 
    global hum 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_b_1_0 = z3.Solver()
    #set the stack init
    solver__ingestTel_b_1_0.push()
    solver__ingestTel_b_1_0.add(And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))
    #getting the check result of the precondition
    _pre = solver__ingestTel_b_1_0.check()
    
    #remove the pre con to check the post or other precond
    solver__ingestTel_b_1_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "tem")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        tem  =  _tem
        solver__ingestTel_b_1_0.add(tem  == tem )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "stage")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        stage  =  2
        solver__ingestTel_b_1_0.add(stage  == stage )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "hum")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        hum  =  _hum
        solver__ingestTel_b_1_0.add(hum  == hum )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__ingestTel_b_1_0.add(And(_pre == z3.sat, Or(And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),stage == 2)))
    return solver__ingestTel_b_1_0.check() == z3.sat
    



def _ingestTel_b_2_0(reset = False):
    global tem 
    global stage 
    global hum 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_b_2_0 = z3.Solver()
    #set the stack init
    solver__ingestTel_b_2_0.push()
    solver__ingestTel_b_2_0.add(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))
    #getting the check result of the precondition
    _pre = solver__ingestTel_b_2_0.check()
    
    #remove the pre con to check the post or other precond
    solver__ingestTel_b_2_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "tem")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        tem  =  _tem
        solver__ingestTel_b_2_0.add(tem  == tem )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "stage")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        stage  =  3
        solver__ingestTel_b_2_0.add(stage  == stage )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "hum")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        hum  =  _hum
        solver__ingestTel_b_2_0.add(hum  == hum )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__ingestTel_b_2_0.add(And(_pre == z3.sat, Or(And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),stage == 2)))
    return solver__ingestTel_b_2_0.check() == z3.sat
    



def _complete_0(reset = False):
    global stage 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__complete_0 = z3.Solver()
    #set the stack init
    solver__complete_0.push()
    solver__complete_0.add(stage == 2)
    #getting the check result of the precondition
    _pre = solver__complete_0.check()
    
    #remove the pre con to check the post or other precond
    solver__complete_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "stage")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        stage  =  3
        solver__complete_0.add(stage  == stage )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__complete_0.add(And(_pre == z3.sat, Or(True)))
    return solver__complete_0.check() == z3.sat
    
check_resut = (_start_0(True) and _ingestTel_0(True) and _ingestTel_1(True) and _transResp_0(True) and _ingestTel_b_1_0(True) and _ingestTel_b_2_0(True) and _complete_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_ingestTel_0: ',_ingestTel_0(True))

print('_ingestTel_1: ',_ingestTel_1(True))

print('_transResp_0: ',_transResp_0(True))

print('_ingestTel_b_1_0: ',_ingestTel_b_1_0(True))

print('_ingestTel_b_2_0: ',_ingestTel_b_2_0(True))

print('_complete_0: ',_complete_0(True))