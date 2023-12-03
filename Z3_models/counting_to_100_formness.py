from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

count = Int('count')


Operator_role = []
Operator_role.append('Operator')







def _startCounting_0(infos = False):
    global count 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__startCounting_0 = z3.Solver() 
    solver__startCounting_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__startCounting_0.push()
    #solver__startCounting_0.add(True)
    solver__startCounting_0.add(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(True,And(count == 0)), Or(count < 100,count >= 100)))))
    post_result = solver__startCounting_0.check() == z3.sat
    #print((And(Or('Operator' in Operator_role), ForAll([count], Implies(And(True,And(count == 0)), Or(count < 100,count >= 100))))), post_result)
    
    solver__startCounting_0.pop()
    solver__startCounting_0.add(True) 
    eps_result = solver__startCounting_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _startCounting_0: ", simplify(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(True,And(count == 0)), Or(count < 100,count >= 100))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__startCounting_02.add(Not(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(True,And(count == 0)), Or(count < 100,count >= 100))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(True,And(count == 0)), Or(count < 100,count >= 100)))))), " :: ", solver__startCounting_02.check() == z3.sat)
            
          
                   
    return result
    



def _incrementCounter_0(infos = False):
    global count 
    # Declare variable before   
    count_old = Int('count_old')
    count_old = Int('count_old')
    
    
    #building the solver for the predancontion
    solver__incrementCounter_0 = z3.Solver() 
    solver__incrementCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__incrementCounter_0.push()
    #solver__incrementCounter_0.add(count_old < 100)
    solver__incrementCounter_0.add(And(Or('Operator' in Operator_role), ForAll([count,count_old], Implies(And(count_old < 100,And(count == count_old + 1)), Or(count < 100,count >= 100)))))
    post_result = solver__incrementCounter_0.check() == z3.sat
    #print((And(Or('Operator' in Operator_role), ForAll([count,count_old], Implies(And(count_old < 100,And(count == count_old + 1)), Or(count < 100,count >= 100))))), post_result)
    
    solver__incrementCounter_0.pop()
    solver__incrementCounter_0.add(True) 
    eps_result = solver__incrementCounter_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _incrementCounter_0: ", simplify(And(Or('Operator' in Operator_role), ForAll([count,count_old], Implies(And(count_old < 100,And(count == count_old + 1)), Or(count < 100,count >= 100))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__incrementCounter_02.add(Not(And(Or('Operator' in Operator_role), ForAll([count,count_old], Implies(And(count_old < 100,And(count == count_old + 1)), Or(count < 100,count >= 100))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('Operator' in Operator_role), ForAll([count,count_old], Implies(And(count_old < 100,And(count == count_old + 1)), Or(count < 100,count >= 100)))))), " :: ", solver__incrementCounter_02.check() == z3.sat)
            
          
                   
    return result
    



def _terminateCounting_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateCounting_0 = z3.Solver() 
    solver__terminateCounting_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateCounting_0.push()
    #solver__terminateCounting_0.add(count >= 100)
    solver__terminateCounting_0.add(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(count >= 100,True), True))))
    post_result = solver__terminateCounting_0.check() == z3.sat
    #print((And(Or('Operator' in Operator_role), ForAll([count], Implies(And(count >= 100,True), True)))), post_result)
    
    solver__terminateCounting_0.pop()
    solver__terminateCounting_0.add(True) 
    eps_result = solver__terminateCounting_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _terminateCounting_0: ", simplify(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(count >= 100,True), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__terminateCounting_02.add(Not(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(count >= 100,True), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('Operator' in Operator_role), ForAll([count], Implies(And(count >= 100,True), True))))), " :: ", solver__terminateCounting_02.check() == z3.sat)
            
          
                   
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