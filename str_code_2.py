from z3 import * 
from Z3.Extension import *

price = Int('price')
state = Bool('state')
M = []
M = [1,2,3,4,5]
x = Int('x')
x = 0


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))
Store(role_B, 0, String('b'))
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, String('d'))
Store(role_D, 0, String('d'))

def reset_deploy_vars():
    M = [1,2,3,4,5]
    x = 0
    M = [1,2,3,4,5]
    x = 0




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
    solver__start_0.add(And(_pre == z3.sat, Or(x >= 0,x > 0)))
    return solver__start_0.check() == z3.sat
    





def _f1_0(reset = False):
    global price 
    global x 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__f1_0 = z3.Solver()
    #set the stack init
    solver__f1_0.push()
    solver__f1_0.add(x >= 0)
    #getting the check result of the precondition
    _pre = solver__f1_0.check()
    
    #remove the pre con to check the post or other precond
    solver__f1_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "price")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        price  =  0
        solver__f1_0.add(price  == price )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")


    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "x")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        x  =  x + 1
        solver__f1_0.add(x  == x )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__f1_0.add(And(_pre == z3.sat, Or(True)))
    return solver__f1_0.check() == z3.sat
    



def _f2_0(reset = False):
    global price 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__f2_0 = z3.Solver()
    #set the stack init
    solver__f2_0.push()
    solver__f2_0.add(x > 0)
    #getting the check result of the precondition
    _pre = solver__f2_0.check()
    
    #remove the pre con to check the post or other precond
    solver__f2_0.pop()
    
    #update the states variable 
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "price")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        price  =  0
        solver__f2_0.add(price  == price )
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    
    #check if precondition condition and the or of all direived preconditions id true 
    solver__f2_0.add(And(_pre == z3.sat, Or(True)))
    return solver__f2_0.check() == z3.sat
    
check_resut = (_start_0(True) and _f1_0(True) and _f2_0(True))

if  check_resut == True:
    print("satisfiable")
else:
    print("unSatisfiable")
       
        


print('_start_0: ',_start_0(True))

print('_f1_0: ',_f1_0(True))

print('_f2_0: ',_f2_0(True))