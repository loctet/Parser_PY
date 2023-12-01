from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

x = Int('x')
y = Int('y')


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))



def _start_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    solver__start_0.add(True)
    
    solver__start_0.add(ForAll([x,y], Implies(True, Or(x<=9))))
    post_result = solver__start_0.check() == z3.sat
    #print((ForAll([x,y], Implies(True, Or(x<=9)))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(ForAll([x,y], Implies(True, Or(x<=9)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__start_02.add(Not(ForAll([x,y], Implies(True, Or(x<=9)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([x,y], Implies(True, Or(x<=9))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _action2_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__action2_0 = z3.Solver() 
    solver__action2_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action2_0.push()
    solver__action2_0.add(x<=10)
    
    solver__action2_0.add(ForAll([x,y], Implies(True, True)))
    post_result = solver__action2_0.check() == z3.sat
    #print((ForAll([x,y], Implies(True, True))), post_result)
    
    solver__action2_0.pop()
    solver__action2_0.add(True) 
    eps_result = solver__action2_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _action2_0: ", simplify(ForAll([x,y], Implies(True, True))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action2_02.add(Not(ForAll([x,y], Implies(True, True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([x,y], Implies(True, True)))), " :: ", solver__action2_02.check() == z3.sat)
            
          
                   
    return result
    



def _action1_0(infos = False):
    global y
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__action1_0 = z3.Solver() 
    solver__action1_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action1_0.push()
    solver__action1_0.add(x<=9)
    
    solver__action1_0.add(ForAll([x,y], Implies(And(y == 0), Or(x<=10))))
    post_result = solver__action1_0.check() == z3.sat
    #print((ForAll([x,y], Implies(And(y == 0), Or(x<=10)))), post_result)
    
    solver__action1_0.pop()
    solver__action1_0.add(True) 
    eps_result = solver__action1_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _action1_0: ", simplify(ForAll([x,y], Implies(And(y == 0), Or(x<=10)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action1_02.add(Not(ForAll([x,y], Implies(And(y == 0), Or(x<=10)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([x,y], Implies(And(y == 0), Or(x<=10))))), " :: ", solver__action1_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _action2_0() and _action1_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_action2_0(True)

_action1_0(True)