from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

x = Int('x')
y = Int('y')


O_role = []
O_role.append('o')
B_role = []
B_role.append('b')



def _start_0(infos = False):
    global x
    global y
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    
    solver__start_0.add(ForAll([x,y], Implies(And(True,And(x == 0, y == 0)), Or(x<=9))))
    post_result = solver__start_0.check() == z3.sat
    
    solver__start_0.pop()
    solver__start_0.push()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat

    solver__start_0.pop()
    solver__start_0.add(Or('o' in O_role)) 
    part_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        print("--For _start_0: ", simplify(ForAll([x,y], Implies(And(True,And(x == 0, y == 0)), Or(x<=9)))), " :: ", result)
        print(f"--- Participants       : {part_result}")
        print(f"--- Determinism        : {eps_result}")
        print(f"--- Sat of o Prec-Conds: {post_result}")

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__start_02.add(Not(ForAll([x,y], Implies(And(True,And(x == 0, y == 0)), Or(x<=9)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([x,y], Implies(And(True,And(x == 0, y == 0)), Or(x<=9))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _action2_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__action2_0 = z3.Solver() 
    solver__action2_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action2_0.push()
    
    solver__action2_0.add(ForAll([x,y], Implies(And(x<=10,True), True)))
    post_result = solver__action2_0.check() == z3.sat
    
    solver__action2_0.pop()
    solver__action2_0.push()
    solver__action2_0.add(True) 
    eps_result = solver__action2_0.check() == z3.sat

    solver__action2_0.pop()
    solver__action2_0.add(Or('b' in B_role)) 
    part_result = solver__action2_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        print("--For _action2_0: ", simplify(ForAll([x,y], Implies(And(x<=10,True), True))), " :: ", result)
        print(f"--- Participants       : {part_result}")
        print(f"--- Determinism        : {eps_result}")
        print(f"--- Sat of o Prec-Conds: {post_result}")

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action2_02.add(Not(ForAll([x,y], Implies(And(x<=10,True), True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([x,y], Implies(And(x<=10,True), True)))), " :: ", solver__action2_02.check() == z3.sat)
            
          
                   
    return result
    



def _action1_0(infos = False):
    global x
    # Declare variable before   
    x_old = Int('x_old')
    x_old = Int('x_old')
    
    
    #building the solver for the predancontion
    solver__action1_0 = z3.Solver() 
    solver__action1_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__action1_0.push()
    
    solver__action1_0.add(ForAll([x,y,x_old], Implies(And(x_old<=9,And(x == x_old + 1)), Or(x<=10))))
    post_result = solver__action1_0.check() == z3.sat
    
    solver__action1_0.pop()
    solver__action1_0.push()
    solver__action1_0.add(True) 
    eps_result = solver__action1_0.check() == z3.sat

    solver__action1_0.pop()
    solver__action1_0.add(Or('b' in B_role)) 
    part_result = solver__action1_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        print("--For _action1_0: ", simplify(ForAll([x,y,x_old], Implies(And(x_old<=9,And(x == x_old + 1)), Or(x<=10)))), " :: ", result)
        print(f"--- Participants       : {part_result}")
        print(f"--- Determinism        : {eps_result}")
        print(f"--- Sat of o Prec-Conds: {post_result}")

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__action1_02.add(Not(ForAll([x,y,x_old], Implies(And(x_old<=9,And(x == x_old + 1)), Or(x<=10)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([x,y,x_old], Implies(And(x_old<=9,And(x == x_old + 1)), Or(x<=10))))), " :: ", solver__action1_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _action2_0() and _action1_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFunctions simplified formula and satisfiability results :')

_start_0(True)

_action2_0(True)

_action1_0(True)