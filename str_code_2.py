from z3 import * 
from Z3.Extension import *

price = Int('price')
state = Bool('state')
state =  False
M = []
M =  [1,2,3,4,5]
x = Int('x')
x = 0



role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, String('d'))

def reset_deploy_vars():
    global state, M, x
    state =  False
    M =  [1,2,3,4,5]
    x = 0
    




def _start_0(reset = False):
    
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _p = Int('_p')

    
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
    solver__start_0.add(And(_pre == z3.sat, Or(And(state == False, _p >0))))
    return solver__start_0.check() == z3.sat
    





def _makeoffer_0(reset = False):
    global price 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _p = Int('_p')

    
    #building the solver for the predancontion
    solver__makeoffer_0 = z3.Solver()
    #set the stack init
    solver__makeoffer_0.push()
    solver__makeoffer_0.add(And(state == False, _p >0))
    #getting the check result of the precondition
    _pre = solver__makeoffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__makeoffer_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "price")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        price  =  _p
        solver__makeoffer_0.add(price  == price )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__makeoffer_0.add(And(_pre == z3.sat, Or(And(state == False),state == False)))
    return solver__makeoffer_0.check() == z3.sat
    



def _acceptoffer_0(reset = False):
    global state 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__acceptoffer_0 = z3.Solver()
    #set the stack init
    solver__acceptoffer_0.push()
    solver__acceptoffer_0.add(And(state == False))
    #getting the check result of the precondition
    _pre = solver__acceptoffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__acceptoffer_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "state")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        state  =  True
        solver__acceptoffer_0.add(state  == state )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__acceptoffer_0.add(And(_pre == z3.sat, Or(True)))
    return solver__acceptoffer_0.check() == z3.sat
    



def _rejectoffer_0(reset = False):
    global state 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__rejectoffer_0 = z3.Solver()
    #set the stack init
    solver__rejectoffer_0.push()
    solver__rejectoffer_0.add(state == False)
    #getting the check result of the precondition
    _pre = solver__rejectoffer_0.check()
    
    #remove the pre con to check the post or other precond
    solver__rejectoffer_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "state")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        state  =  True
        solver__rejectoffer_0.add(state  == state )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__rejectoffer_0.add(And(_pre == z3.sat, Or(True)))
    return solver__rejectoffer_0.check() == z3.sat
    
check_resut = (_start_0(True) and _makeoffer_0(True) and _acceptoffer_0(True) and _rejectoffer_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_makeoffer_0: ',_makeoffer_0(True))

print('_acceptoffer_0: ',_acceptoffer_0(True))

print('_rejectoffer_0: ',_rejectoffer_0(True))