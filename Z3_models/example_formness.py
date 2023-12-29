from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *






def _start_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    
    solver__start_0.add(Implies(And(True,True), True))
    post_result = solver__start_0.check() == z3.sat
    
    #check determinism
    solver__start_0.pop()
    solver__start_0.push()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat

    #check participants
    solver__start_0.pop()
    solver__start_0.add(False) 
    part_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _start_0: ", simplify(Implies(And(True,True), True)), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "(False)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__start_02.add(Not(Implies(And(True,True), True)))
            print("\nSimplify of the Not Formula: ", simplify(Not(Implies(And(True,True), True))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    


check_resut = (_start_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
if not check_resut: 
    print('\nFunctions simplified formula and satisfiability results :')
    _start_0(True)