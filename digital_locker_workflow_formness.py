from z3 import * 
from Z3.Extension import *

locked = Int('locked')
requestedL = Int('requestedL')




role_Owner = Array('Owner',IntSort() , StringSort())
Store(role_Owner, 0, String('Owner'))
role_BankAgent = Array('BankAgent',IntSort() , StringSort())
Store(role_BankAgent, 0, String('BankAgent'))
role_ThirdPartyRequestor = Array('ThirdPartyRequestor',IntSort() , StringSort())
Store(role_ThirdPartyRequestor, 0, String('ThirdPartyRequestor'))
role_CurrentAuthorizedUser = Array('CurrentAuthorizedUser',IntSort() , StringSort())
Store(role_CurrentAuthorizedUser, 0, String('CurrentAuthorizedUser'))

def reset_deploy_vars():
    1 == 1
    
    global locked , requestedL 
    locked = Int('locked')
    requestedL = Int('requestedL')
    
    




def _start_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
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
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__start_0.add(And(_pre == z3.sat, Or(True)))
    return solver__start_0.check() == z3.sat
    





def _revokeGrantAccessLocker_0(reset = False):
    global locked 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__revokeGrantAccessLocker_0 = z3.Solver()
    #set the stack init
    solver__revokeGrantAccessLocker_0.push()
    solver__revokeGrantAccessLocker_0.add(locked == False)
    #getting the check result of the precondition
    _pre = solver__revokeGrantAccessLocker_0.check()
    
    #remove the pre con to check the post or other precond
    solver__revokeGrantAccessLocker_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "locked")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        locked  =  False
        solver__revokeGrantAccessLocker_0.add(locked  == locked )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__revokeGrantAccessLocker_0.add(And(_pre == z3.sat, Or(True,locked == False,True)))
    return solver__revokeGrantAccessLocker_0.check() == z3.sat
    



def _grantAccessLocker_0(reset = False):
    global locked 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__grantAccessLocker_0 = z3.Solver()
    #set the stack init
    solver__grantAccessLocker_0.push()
    solver__grantAccessLocker_0.add(locked == False)
    #getting the check result of the precondition
    _pre = solver__grantAccessLocker_0.check()
    
    #remove the pre con to check the post or other precond
    solver__grantAccessLocker_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "locked")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        locked  =  True
        solver__grantAccessLocker_0.add(locked  == locked )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__grantAccessLocker_0.add(And(_pre == z3.sat, Or(locked == True,True)))
    return solver__grantAccessLocker_0.check() == z3.sat
    



def _terminateSharing_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__terminateSharing_0 = z3.Solver()
    #set the stack init
    solver__terminateSharing_0.push()
    solver__terminateSharing_0.add(True)
    #getting the check result of the precondition
    _pre = solver__terminateSharing_0.check()
    
    #remove the pre con to check the post or other precond
    solver__terminateSharing_0.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__terminateSharing_0.add(And(_pre == z3.sat, Or(True)))
    return solver__terminateSharing_0.check() == z3.sat
    

def _terminateSharing_1(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__terminateSharing_1 = z3.Solver()
    #set the stack init
    solver__terminateSharing_1.push()
    solver__terminateSharing_1.add(True)
    #getting the check result of the precondition
    _pre = solver__terminateSharing_1.check()
    
    #remove the pre con to check the post or other precond
    solver__terminateSharing_1.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__terminateSharing_1.add(And(_pre == z3.sat, Or(True)))
    return solver__terminateSharing_1.check() == z3.sat
    

def _terminateSharing_2(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__terminateSharing_2 = z3.Solver()
    #set the stack init
    solver__terminateSharing_2.push()
    solver__terminateSharing_2.add(True)
    #getting the check result of the precondition
    _pre = solver__terminateSharing_2.check()
    
    #remove the pre con to check the post or other precond
    solver__terminateSharing_2.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__terminateSharing_2.add(And(_pre == z3.sat, Or(True)))
    return solver__terminateSharing_2.check() == z3.sat
    



def _revokeThirdPartyRequest_0(reset = False):
    global locked 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__revokeThirdPartyRequest_0 = z3.Solver()
    #set the stack init
    solver__revokeThirdPartyRequest_0.push()
    solver__revokeThirdPartyRequest_0.add(locked == True)
    #getting the check result of the precondition
    _pre = solver__revokeThirdPartyRequest_0.check()
    
    #remove the pre con to check the post or other precond
    solver__revokeThirdPartyRequest_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "locked")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        locked  =  False
        solver__revokeThirdPartyRequest_0.add(locked  == locked )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__revokeThirdPartyRequest_0.add(And(_pre == z3.sat, Or(True,locked == False,True)))
    return solver__revokeThirdPartyRequest_0.check() == z3.sat
    



def _ShareThirdPartyRequest_0(reset = False):
    global locked 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__ShareThirdPartyRequest_0 = z3.Solver()
    #set the stack init
    solver__ShareThirdPartyRequest_0.push()
    solver__ShareThirdPartyRequest_0.add(True)
    #getting the check result of the precondition
    _pre = solver__ShareThirdPartyRequest_0.check()
    
    #remove the pre con to check the post or other precond
    solver__ShareThirdPartyRequest_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "locked")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        locked  =  True
        solver__ShareThirdPartyRequest_0.add(locked  == locked )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__ShareThirdPartyRequest_0.add(And(_pre == z3.sat, Or(locked == True,True)))
    return solver__ShareThirdPartyRequest_0.check() == z3.sat
    



def _requestAccessLocker_0(reset = False):
    global locked 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__requestAccessLocker_0 = z3.Solver()
    #set the stack init
    solver__requestAccessLocker_0.push()
    solver__requestAccessLocker_0.add(locked == False)
    #getting the check result of the precondition
    _pre = solver__requestAccessLocker_0.check()
    
    #remove the pre con to check the post or other precond
    solver__requestAccessLocker_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "locked")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        locked  =  False
        solver__requestAccessLocker_0.add(locked  == locked )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__requestAccessLocker_0.add(And(_pre == z3.sat, Or(locked == False,locked == False,True)))
    return solver__requestAccessLocker_0.check() == z3.sat
    



def _uploadDigitalAsset_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__uploadDigitalAsset_0 = z3.Solver()
    #set the stack init
    solver__uploadDigitalAsset_0.push()
    solver__uploadDigitalAsset_0.add(True)
    #getting the check result of the precondition
    _pre = solver__uploadDigitalAsset_0.check()
    
    #remove the pre con to check the post or other precond
    solver__uploadDigitalAsset_0.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__uploadDigitalAsset_0.add(And(_pre == z3.sat, Or(True,locked == False,True)))
    return solver__uploadDigitalAsset_0.check() == z3.sat
    



def _reviewRequest_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__reviewRequest_0 = z3.Solver()
    #set the stack init
    solver__reviewRequest_0.push()
    solver__reviewRequest_0.add(True)
    #getting the check result of the precondition
    _pre = solver__reviewRequest_0.check()
    
    #remove the pre con to check the post or other precond
    solver__reviewRequest_0.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__reviewRequest_0.add(And(_pre == z3.sat, Or(True)))
    return solver__reviewRequest_0.check() == z3.sat
    



def _requestAvailability_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__requestAvailability_0 = z3.Solver()
    #set the stack init
    solver__requestAvailability_0.push()
    solver__requestAvailability_0.add(True)
    #getting the check result of the precondition
    _pre = solver__requestAvailability_0.check()
    
    #remove the pre con to check the post or other precond
    solver__requestAvailability_0.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__requestAvailability_0.add(And(_pre == z3.sat, Or(True)))
    return solver__requestAvailability_0.check() == z3.sat
    
check_resut = (_start_0(True) and _revokeGrantAccessLocker_0(True) and _grantAccessLocker_0(True) and _terminateSharing_0(True) and _terminateSharing_1(True) and _terminateSharing_2(True) and _revokeThirdPartyRequest_0(True) and _ShareThirdPartyRequest_0(True) and _requestAccessLocker_0(True) and _uploadDigitalAsset_0(True) and _reviewRequest_0(True) and _requestAvailability_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_revokeGrantAccessLocker_0: ',_revokeGrantAccessLocker_0(True))

print('_grantAccessLocker_0: ',_grantAccessLocker_0(True))

print('_terminateSharing_0: ',_terminateSharing_0(True))

print('_terminateSharing_1: ',_terminateSharing_1(True))

print('_terminateSharing_2: ',_terminateSharing_2(True))

print('_revokeThirdPartyRequest_0: ',_revokeThirdPartyRequest_0(True))

print('_ShareThirdPartyRequest_0: ',_ShareThirdPartyRequest_0(True))

print('_requestAccessLocker_0: ',_requestAccessLocker_0(True))

print('_uploadDigitalAsset_0: ',_uploadDigitalAsset_0(True))

print('_reviewRequest_0: ',_reviewRequest_0(True))

print('_requestAvailability_0: ',_requestAvailability_0(True))