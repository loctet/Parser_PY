from z3 import * 
from Z3.Extension import *

state = Int('state')
state = 0
price = Int('price')
price = 0
B = []
B =  []

_price = Int('_price')
_price = Int('_price')

price =  _price


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))

def reset_deploy_vars():
    global state, price, B
    state = 0
    price = 0
    B =  []
    global state , state , price , price , B , B 
    state = Int('state')
    state = 0
    price = Int('price')
    price = 0
    B = []
    B =  []
    
    price =  _price





def _start_0(reset = False):
    global price 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _price = Int('_price')
    _price = Int('_price')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver()
    #set the stack init
    solver__start_0.push()
    solver__start_0.add(_price > 0)
    #getting the check result of the precondition
    _pre = solver__start_0.check()
    
    #remove the pre con to check the post or other precond
    solver__start_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "price")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        price  =  _price
        solver__start_0.add(price  == price )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__start_0.add(And(_pre == z3.sat, Or(And(Or(state == 0, state == 1), _price >= price))))
    return solver__start_0.check() == z3.sat
    





def _acceptOffer_0(reset = False):
    global state 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__acceptOffer_0 = z3.Solver()
    #set the stack init
    solver__acceptOffer_0.push()
    solver__acceptOffer_0.add(state == 1)
    #getting the check result of the precondition
    _pre = solver__acceptOffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__acceptOffer_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "state")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        state  =  2
        solver__acceptOffer_0.add(state  == state )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__acceptOffer_0.add(And(_pre == z3.sat, Or(True)))
    return solver__acceptOffer_0.check() == z3.sat
    



def _rejectOffer_0(reset = False):
    global state 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__rejectOffer_0 = z3.Solver()
    #set the stack init
    solver__rejectOffer_0.push()
    solver__rejectOffer_0.add(state == 1)
    #getting the check result of the precondition
    _pre = solver__rejectOffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__rejectOffer_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "state")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        state  =  0
        solver__rejectOffer_0.add(state  == state )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__rejectOffer_0.add(And(_pre == z3.sat, Or(True)))
    return solver__rejectOffer_0.check() == z3.sat
    
check_resut = (_start_0(True) and _acceptOffer_0(True) and _rejectOffer_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_acceptOffer_0: ',_acceptOffer_0(True))

print('_rejectOffer_0: ',_rejectOffer_0(True))