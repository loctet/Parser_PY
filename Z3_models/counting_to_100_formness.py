from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

count = Int('count')


role_Operator = Array('Operator',IntSort() , StringSort())
Store(role_Operator, 0, String('Operator'))







def _startCounting_0(minimize = False):
    global count 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__startCounting_0 = z3.Solver() 
    solver__startCounting_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__startCounting_0.add(ForAll([count], Implies(And(count == 0), Or(count < 100,count >= 100))))
    result = solver__startCounting_0.check() == z3.sat
    if minimize :
        print("--For _startCounting_0: ", simplify(ForAll([count], Implies(And(count == 0), Or(count < 100,count >= 100)))), " :: ", result)
        if not result: 
            solver__startCounting_02.add(Not(ForAll([count], Implies(And(count == 0), Or(count < 100,count >= 100)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([count], Implies(And(count == 0), Or(count < 100,count >= 100))))), " :: ", solver__startCounting_02.check() == z3.sat)
            
                
    return result
    



def _incrementCounter_0(minimize = False):
    global count 
    # Declare variable before   
    count_old = Int('count_old')
    
    
    #building the solver for the predancontion
    solver__incrementCounter_0 = z3.Solver() 
    solver__incrementCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__incrementCounter_0.add(ForAll([count,count_old], Implies(And(count == count_old + 1), Or(count < 100,count >= 100))))
    result = solver__incrementCounter_0.check() == z3.sat
    if minimize :
        print("--For _incrementCounter_0: ", simplify(ForAll([count,count_old], Implies(And(count == count_old + 1), Or(count < 100,count >= 100)))), " :: ", result)
        if not result: 
            solver__incrementCounter_02.add(Not(ForAll([count,count_old], Implies(And(count == count_old + 1), Or(count < 100,count >= 100)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([count,count_old], Implies(And(count == count_old + 1), Or(count < 100,count >= 100))))), " :: ", solver__incrementCounter_02.check() == z3.sat)
            
                
    return result
    



def _terminateCounting_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateCounting_0 = z3.Solver() 
    solver__terminateCounting_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateCounting_0.add(ForAll([count], Implies(True, True)))
    result = solver__terminateCounting_0.check() == z3.sat
    if minimize :
        print("--For _terminateCounting_0: ", simplify(ForAll([count], Implies(True, True))), " :: ", result)
        if not result: 
            solver__terminateCounting_02.add(Not(ForAll([count], Implies(True, True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([count], Implies(True, True)))), " :: ", solver__terminateCounting_02.check() == z3.sat)
            
                
    return result
    
check_resut = (_startCounting_0() and _incrementCounter_0() and _terminateCounting_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_startCounting_0(True)

_incrementCounter_0(True)

_terminateCounting_0(True)