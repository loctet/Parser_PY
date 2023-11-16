from z3 import * 
from Z3.Extension import *

currentOwner = String('currentOwner')
previousOwner = String('previousOwner')
Counterparty = String('Counterparty')
owner = String('owner')

_counterparty = String('_counterparty')
_currentOwner = String('_currentOwner')

currentOwner =  _currentOwner


role_InitiatingCounterParty = Array('InitiatingCounterParty',IntSort() , StringSort())
Store(role_InitiatingCounterParty, 0, String('InitiatingCounterParty'))
role_Counterparty = Array('Counterparty',IntSort() , StringSort())
Store(role_Counterparty, 0, String('Counterparty'))
role_Owner = Array('Owner',IntSort() , StringSort())
Store(role_Owner, 0, String('Owner'))
role_Observer = Array('Observer',IntSort() , StringSort())
Store(role_Observer, 0, String('Observer'))

def reset_deploy_vars():
    1 == 1
    global currentOwner, previousOwner, Counterparty, owner
    global currentOwner , previousOwner , Counterparty , owner 
    currentOwner = String('currentOwner')
    previousOwner = String('previousOwner')
    Counterparty = String('Counterparty')
    owner = String('owner')
    
    currentOwner =  _currentOwner





def _start_0(reset = False):
    global currentOwner 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _counterparty = String('_counterparty')
    _currentOwner = String('_currentOwner')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver()
    #set the stack init
    """solver__start_0.push()
    solver__start_0.add(True)
    #getting the check result of the precondition
    _pre = solver__start_0.check()
    
    #remove the pre con to check the post or other precond
    solver__start_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "currentOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        currentOwner  =  _currentOwner
        _tmp_ =  _currentOwner
        solver__start_0.add(currentOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")
"""
    
    #check if precondition condition and the or of all direived preconditions id true 
    
    solver__start_0.add(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner], And(currentOwner  ==  _currentOwner)), Or(Exists([_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty], True)))))
    return solver__start_0.check() == z3.sat
    





def _assignResponsibility_0(reset = False):
    global currentOwner 
    global previousOwner 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _counterparty = String('_counterparty')
    _counterparty = String('_counterparty')
    
    
    #building the solver for the predancontion
    solver__assignResponsibility_0 = z3.Solver()
    #set the stack init
    """solver__assignResponsibility_0.push()
    solver__assignResponsibility_0.add(True)
    #getting the check result of the precondition
    _pre = solver__assignResponsibility_0.check()
    
    #remove the pre con to check the post or other precond
    solver__assignResponsibility_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "currentOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        currentOwner  =  _counterparty
        _tmp_ =  _counterparty
        solver__assignResponsibility_0.add(currentOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "previousOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        previousOwner  =  currentOwner
        _tmp_ =  currentOwner
        solver__assignResponsibility_0.add(previousOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")
"""
    
    #check if precondition condition and the or of all direived preconditions id true 
    
    solver__assignResponsibility_0.add(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty], And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner)), Or(Exists([_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),Exists([_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty], currentOwner == owner)))))
    return solver__assignResponsibility_0.check() == z3.sat
    

def _assignResponsibility_1(reset = False):
    global currentOwner 
    global previousOwner 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _counterparty = String('_counterparty')
    _counterparty = String('_counterparty')
    
    
    #building the solver for the predancontion
    solver__assignResponsibility_1 = z3.Solver()
    #set the stack init
    """solver__assignResponsibility_1.push()
    solver__assignResponsibility_1.add(And(currentOwner == _counterparty, currentOwner != owner))
    #getting the check result of the precondition
    _pre = solver__assignResponsibility_1.check()
    
    #remove the pre con to check the post or other precond
    solver__assignResponsibility_1.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "currentOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        currentOwner  =  _counterparty
        _tmp_ =  _counterparty
        solver__assignResponsibility_1.add(currentOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "previousOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        previousOwner  =  currentOwner
        _tmp_ =  currentOwner
        solver__assignResponsibility_1.add(previousOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")
"""
    
    #check if precondition condition and the or of all direived preconditions id true 
    
    solver__assignResponsibility_1.add(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty], And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner)), Or(Exists([_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),Exists([_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty], currentOwner == owner)))))
    return solver__assignResponsibility_1.check() == z3.sat
    



def _reachDestination_0(reset = False):
    global previousOwner 
    global currentOwner 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__reachDestination_0 = z3.Solver()
    #set the stack init
    """solver__reachDestination_0.push()
    solver__reachDestination_0.add(currentOwner == owner)
    #getting the check result of the precondition
    _pre = solver__reachDestination_0.check()
    
    #remove the pre con to check the post or other precond
    solver__reachDestination_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "previousOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        previousOwner  =  currentOwner
        _tmp_ =  currentOwner
        solver__reachDestination_0.add(previousOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "currentOwner")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        currentOwner  =  owner
        _tmp_ =  owner
        solver__reachDestination_0.add(currentOwner  == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")
"""
    
    #check if precondition condition and the or of all direived preconditions id true 
    
    solver__reachDestination_0.add(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty], And(previousOwner  ==  currentOwner ,  currentOwner  ==  owner)), Or(Exists([_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_currentOwner,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty,_counterparty], True)))))
    return solver__reachDestination_0.check() == z3.sat
    
check_resut = (_start_0(True) and _assignResponsibility_0(True) and _assignResponsibility_1(True) and _reachDestination_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_assignResponsibility_0: ',_assignResponsibility_0(True))

print('_assignResponsibility_1: ',_assignResponsibility_1(True))

print('_reachDestination_0: ',_reachDestination_0(True))