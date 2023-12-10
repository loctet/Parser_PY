from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *



O_role = []
O_role.append('o')
B_role = []
B_role.append('b')



def _start_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    #solver__start_0.add(True)
    solver__start_0.add(And(Or('o' in O_role), Implies(And(True,True), Or(True,False))))
    post_result = solver__start_0.check() == z3.sat
    #print((And(Or('o' in O_role), Implies(And(True,True), Or(True,False)))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(And(Or('o' in O_role), Implies(And(True,True), Or(True,False)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__start_02.add(Not(And(Or('o' in O_role), Implies(And(True,True), Or(True,False)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), Implies(And(True,True), Or(True,False))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _action1_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__action1_0 = z3.Solver() 
    solver__action1_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action1_0.push()
    #solver__action1_0.add(True)
    solver__action1_0.add(And(True, Implies(And(True,True), Or(True,False))))
    post_result = solver__action1_0.check() == z3.sat
    #print((And(True, Implies(And(True,True), Or(True,False)))), post_result)
    
    solver__action1_0.pop()
    solver__action1_0.add(True) 
    eps_result = solver__action1_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _action1_0: ", simplify(And(True, Implies(And(True,True), Or(True,False)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action1_02.add(Not(And(True, Implies(And(True,True), Or(True,False)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, Implies(And(True,True), Or(True,False))))), " :: ", solver__action1_02.check() == z3.sat)
            
          
                   
    return result
    



def _action2_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__action2_0 = z3.Solver() 
    solver__action2_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action2_0.push()
    #solver__action2_0.add(False)
    solver__action2_0.add(And(True, Implies(And(False,True), Or(True))))
    post_result = solver__action2_0.check() == z3.sat
    #print((And(True, Implies(And(False,True), Or(True)))), post_result)
    
    solver__action2_0.pop()
    solver__action2_0.add(True) 
    eps_result = solver__action2_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _action2_0: ", simplify(And(True, Implies(And(False,True), Or(True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action2_02.add(Not(And(True, Implies(And(False,True), Or(True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, Implies(And(False,True), Or(True))))), " :: ", solver__action2_02.check() == z3.sat)
            
          
                   
    return result
    



def _action3_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__action3_0 = z3.Solver() 
    solver__action3_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action3_0.push()
    #solver__action3_0.add(True)
    solver__action3_0.add(And(True, Implies(And(True,True), True)))
    post_result = solver__action3_0.check() == z3.sat
    #print((And(True, Implies(And(True,True), True))), post_result)
    
    solver__action3_0.pop()
    solver__action3_0.add(True) 
    eps_result = solver__action3_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _action3_0: ", simplify(And(True, Implies(And(True,True), True))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action3_02.add(Not(And(True, Implies(And(True,True), True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, Implies(And(True,True), True)))), " :: ", solver__action3_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _action1_0() and _action2_0() and _action3_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_action1_0(True)

_action2_0(True)

_action3_0(True)