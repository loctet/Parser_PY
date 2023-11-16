from z3 import * 
from Z3.Extension import *

state = Int('state')
state = 0
offer = Int('offer')
offer = 0
B = []
B =  []

_offer = Int('_offer')



role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))

def reset_deploy_vars():
    1 == 1
    global state, offer, B
    state = 0
    offer = 0
    B =  []
    




def _start_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _offer = Int('_offer')
    
    
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
    #solver__start_0.add(And(_pre == z3.sat, solver__start_0.add(And(_pre == z3.sat, Or(_offer  > 0))))
    s_check = False 
    _otherPrecs = [_offer  > 0]
    for _prec in _otherPrecs: 
        solver__start_0.push()
        solver__start_0.add(Implies(True, _prec))
        s_check = s_check and solver__start_0.check() == z3.sat
        solver__start_0.pop()
    solver__start_0.add(s_check)
    return solver__start_0.check() == z3.sat
    





def _acceptOffer_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__acceptOffer_0 = z3.Solver()
    #set the stack init
    solver__acceptOffer_0.push()
    solver__acceptOffer_0.add(True)
    #getting the check result of the precondition
    _pre = solver__acceptOffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__acceptOffer_0.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    #solver__acceptOffer_0.add(And(_pre == z3.sat, solver__acceptOffer_0.add(And(_pre == z3.sat, Or(True))))
    s_check = False 
    _otherPrecs = [True]
    for _prec in _otherPrecs: 
        solver__acceptOffer_0.push()
        solver__acceptOffer_0.add(Implies(True, _prec))
        s_check = s_check and solver__acceptOffer_0.check() == z3.sat
        solver__acceptOffer_0.pop()
    solver__acceptOffer_0.add(s_check)
    return solver__acceptOffer_0.check() == z3.sat
    



def _rejectOffer_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__rejectOffer_0 = z3.Solver()
    #set the stack init
    solver__rejectOffer_0.push()
    solver__rejectOffer_0.add(True)
    #getting the check result of the precondition
    _pre = solver__rejectOffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__rejectOffer_0.pop()
    
    #update the states variable 
    
    
    #check if precondition condition and the or of all direived preconditions id true 
    #solver__rejectOffer_0.add(And(_pre == z3.sat, solver__rejectOffer_0.add(And(_pre == z3.sat, Or(_offer  > 0))))
    s_check = False 
    _otherPrecs = [_offer  > 0]
    for _prec in _otherPrecs: 
        solver__rejectOffer_0.push()
        solver__rejectOffer_0.add(Implies(True, _prec))
        s_check = s_check and solver__rejectOffer_0.check() == z3.sat
        solver__rejectOffer_0.pop()
    solver__rejectOffer_0.add(s_check)
    return solver__rejectOffer_0.check() == z3.sat
    



def _makeOffer_0(reset = False):
    global offer  
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__makeOffer_0 = z3.Solver()
    #set the stack init
    solver__makeOffer_0.push()
    solver__makeOffer_0.add(_offer  > 0)
    #getting the check result of the precondition
    _pre = solver__makeOffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__makeOffer_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "offer")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        offer   =  _offer
        _tmp_ =  _offer
        solver__makeOffer_0.add(offer   == _tmp_)
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    #solver__makeOffer_0.add(And(_pre == z3.sat, solver__makeOffer_0.add(And(_pre == z3.sat, Or(True,True))))
    s_check = False 
    _otherPrecs = [True, True]
    for _prec in _otherPrecs: 
        solver__makeOffer_0.push()
        solver__makeOffer_0.add(Implies(_offer  > 0, _prec))
        s_check = s_check and solver__makeOffer_0.check() == z3.sat
        solver__makeOffer_0.pop()
    solver__makeOffer_0.add(s_check)
    return solver__makeOffer_0.check() == z3.sat
    
check_resut = (_start_0(True) and _acceptOffer_0(True) and _rejectOffer_0(True) and _makeOffer_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_acceptOffer_0: ',_acceptOffer_0(True))

print('_rejectOffer_0: ',_rejectOffer_0(True))

print('_makeOffer_0: ',_makeOffer_0(True))