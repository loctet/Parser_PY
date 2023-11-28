from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

count = Int('count')
count_old_1 = Int('count_old_1')


role_Operator = Array('Operator',IntSort() , StringSort())
Store(role_Operator, 0, String('Operator'))







def _startCounting_0(minimize = False):
    global count 
    # Declare variable before   
    count_old = Int('count_old')
    
    
    #building the solver for the predancontion
    solver__startCounting_0 = z3.Solver() 
    solver__startCounting_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__startCounting_0.push()
    solver__startCounting_0.add(ForAll([count,count_old_1], Implies(And(count == 0), Or(Exists([count_old], count_old < 100),count >= 100))))
    result = solver__startCounting_0.check() == z3.sat
    
    
    if minimize :
        print("--For _startCounting_0: ", simplify(ForAll([count,count_old_1], Implies(And(count == 0), Or(Exists([count_old], count_old < 100),count >= 100)))), " :: ", result)
        if not result: 
            solver__startCounting_02.add(Not(ForAll([count,count_old_1], Implies(And(count == 0), Or(Exists([count_old], count_old < 100),count >= 100)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([count,count_old_1], Implies(And(count == 0), Or(Exists([count_old], count_old < 100),count >= 100))))), " :: ", solver__startCounting_02.check() == z3.sat)
            
    solver__startCounting_0.pop()
    solver__startCounting_0.add(ForAll([count,count_old_1], Implies(And(count == 0), True))) 
    if  solver__startCounting_0.check() != z3.sat :
        print ("Non deperministic")          
    return result
    



def _incrementCounter_0(minimize = False):
    global count 
    # Declare variable before   
    count_old = Int('count_old')
    count_old = Int('count_old')
    
    
    #building the solver for the predancontion
    solver__incrementCounter_0 = z3.Solver() 
    solver__incrementCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__incrementCounter_0.push()
    solver__incrementCounter_0.add(ForAll([count,count_old_1,count_old], Implies(And(count == count_old + 1), Or(Exists([count_old], count_old < 100),count >= 100))))
    result = solver__incrementCounter_0.check() == z3.sat
    
    
    if minimize :
        print("--For _incrementCounter_0: ", simplify(ForAll([count,count_old_1,count_old], Implies(And(count == count_old + 1), Or(Exists([count_old], count_old < 100),count >= 100)))), " :: ", result)
        if not result: 
            solver__incrementCounter_02.add(Not(ForAll([count,count_old_1,count_old], Implies(And(count == count_old + 1), Or(Exists([count_old], count_old < 100),count >= 100)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([count,count_old_1,count_old], Implies(And(count == count_old + 1), Or(Exists([count_old], count_old < 100),count >= 100))))), " :: ", solver__incrementCounter_02.check() == z3.sat)
            
    solver__incrementCounter_0.pop()
    solver__incrementCounter_0.add(ForAll([count,count_old_1,count_old], Implies(And(count == count_old + 1), True))) 
    if  solver__incrementCounter_0.check() != z3.sat :
        print ("Non deperministic")          
    return result
    



def _terminateCounting_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateCounting_0 = z3.Solver() 
    solver__terminateCounting_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateCounting_0.push()
    solver__terminateCounting_0.add(ForAll([count,count_old_1], Implies(True, True)))
    result = solver__terminateCounting_0.check() == z3.sat
    
    
    if minimize :
        print("--For _terminateCounting_0: ", simplify(ForAll([count,count_old_1], Implies(True, True))), " :: ", result)
        if not result: 
            solver__terminateCounting_02.add(Not(ForAll([count,count_old_1], Implies(True, True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([count,count_old_1], Implies(True, True)))), " :: ", solver__terminateCounting_02.check() == z3.sat)
            
    solver__terminateCounting_0.pop()
    solver__terminateCounting_0.add(ForAll([count,count_old_1], Implies(True, True))) 
    if  solver__terminateCounting_0.check() != z3.sat :
        print ("Non deperministic")          
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