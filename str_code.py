from z3 import * 
from Z3.Extension import *

price = Int('price')
state = Bool('state')
M = []
M = [1,2,3,4,5]
x = Int('x')
x = 0



def formula_0(item):
  solver = z3.Solver()
  solver.add(item > 0)
  return solver.check() == z3.sat
  

def formula_1(item):
  solver = z3.Solver()
  solver.add(item > 0)
  return solver.check() == z3.sat
  
role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, String('d'))

def reset_deploy_vars():
    M = [1,2,3,4,5]
    x = 0






def _start_0(reset = True):
    if reset:
        reset_deploy_vars()
    
    
    solver__start_0 = z3.Solver()
    solver__start_0.push()
    solver__start_0.add(True)
    _pre = solver__start_0.check()
    solver__start_0.pop()
    solver__start_0.add(And(_pre == z3.sat, state==True))
    return solver__start_0.check() == z3.sat
                            



def _makeoffer_0(reset = True):
    if reset:
        reset_deploy_vars()
    _p = Int('_p')

    
    solver__makeoffer_0 = z3.Solver()
    solver__makeoffer_0.push()
    solver__makeoffer_0.add(And(_p > 0, state == True))
    _pre = solver__makeoffer_0.check()
    solver__makeoffer_0.pop()
    solver__makeoffer_0.add(And(_pre == z3.sat, price == _p))
    return solver__makeoffer_0.check() == z3.sat
                            



def _acceptoffer_0(reset = True):
    if reset:
        reset_deploy_vars()
    
    
    solver__acceptoffer_0 = z3.Solver()
    solver__acceptoffer_0.push()
    solver__acceptoffer_0.add(state)
    _pre = solver__acceptoffer_0.check()
    solver__acceptoffer_0.pop()
    solver__acceptoffer_0.add(And(_pre == z3.sat, Not(state)))
    return solver__acceptoffer_0.check() == z3.sat
                            



def _OK_0(reset = True):
    if reset:
        reset_deploy_vars()
    
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "M[-1]")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        M[-1]  =  -5
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    solver__OK_0 = z3.Solver()
    solver__OK_0.push()
    solver__OK_0.add(True)
    _pre = solver__OK_0.check()
    solver__OK_0.pop()
    solver__OK_0.add(And(_pre == z3.sat, And(Not(state), And(forall_in_set(formula_0, M), exist_in_set(formula_1, M)))))
    return solver__OK_0.check() == z3.sat
                            



def _NOK_0(reset = True):
    if reset:
        reset_deploy_vars()
    
    
    # Define a regular expression pattern to match variable names inside brackets or parentheses
    pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
    # Use re.search to find the first match in the expression
    match = re.search(pattern, "x")
    
    # Check if the variable exists in locals() or globals()
    if match.group(0) in globals():
        # If the variable exists, create a valid assignment
        x  =  0
    else:
        raise NameError(f"State Variable '{match.group(0)}' does not exist")

    solver__NOK_0 = z3.Solver()
    solver__NOK_0.push()
    solver__NOK_0.add(True)
    _pre = solver__NOK_0.check()
    solver__NOK_0.pop()
    solver__NOK_0.add(And(_pre == z3.sat, And(state, x <= 10)))
    return solver__NOK_0.check() == z3.sat
                            



def _rejectoffer_0(reset = True):
    if reset:
        reset_deploy_vars()
    
    
    solver__rejectoffer_0 = z3.Solver()
    solver__rejectoffer_0.push()
    solver__rejectoffer_0.add(state)
    _pre = solver__rejectoffer_0.check()
    solver__rejectoffer_0.pop()
    solver__rejectoffer_0.add(And(_pre == z3.sat, Not(state)))
    return solver__rejectoffer_0.check() == z3.sat
                            
check_resut = (_start_0() and _makeoffer_0() and _acceptoffer_0() and _OK_0() and _NOK_0() and _rejectoffer_0())
