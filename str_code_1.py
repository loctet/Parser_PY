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
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, String('d'))

def reset_deploy_vars():
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
    


check_resut = (_start_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))