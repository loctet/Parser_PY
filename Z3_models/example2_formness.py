from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *



O_role = []
O_role.append('o')



def _start_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    
    solver__start_0.add(Implies(And(True,True), Or(True)))
    post_result = solver__start_0.check() == z3.sat
    
    #check determinism
    solver__start_0.pop()
    solver__start_0.push()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat

    #check participants
    solver__start_0.pop()
    solver__start_0.add(Or('o' in O_role)) 
    part_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _start_0: ", simplify(Implies(And(True,True), Or(True))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "(Or('o' in O_role))")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__start_02.add(Not(Implies(And(True,True), Or(True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(Implies(And(True,True), Or(True)))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    

def _start_1(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_1 = z3.Solver() 
    solver__start_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_1.push()
    
    solver__start_1.add(Implies(And(True,True), True))
    post_result = solver__start_1.check() == z3.sat
    
    #check determinism
    solver__start_1.pop()
    solver__start_1.push()
    solver__start_1.add(True) 
    eps_result = solver__start_1.check() == z3.sat

    #check participants
    solver__start_1.pop()
    solver__start_1.add('o' in O_role) 
    part_result = solver__start_1.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _start_1: ", simplify(Implies(And(True,True), True)), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "('o' in O_role)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__start_12.add(Not(Implies(And(True,True), True)))
            print("\nSimplify of the Not Formula: ", simplify(Not(Implies(And(True,True), True))), " :: ", solver__start_12.check() == z3.sat)
            
          
                   
    return result
    


check_resut = (_start_0() and _start_1())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
if not check_resut: 
    print('\nFunctions simplified formula and satisfiability results :')
    _start_0(True)
    _start_1(True)