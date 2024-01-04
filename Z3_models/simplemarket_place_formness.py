from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

state = Int('state')
offer = Int('offer')


O_role = []
O_role.append('o')
B_role = []
B_role.append('b')



def _start_0(infos = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    
    solver__start_0.add(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))
    post_result = solver__start_0.check() == z3.sat
    
    #check determinism
    solver__start_0.pop()
    solver__start_0.push()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat

    #check participants
    solver__start_0.pop()
    solver__start_0.add( len(O_role) > 0 and 'o' in O_role) 
    part_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _start_0: ", simplify(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "( len(O_role) > 0 and 'o' in O_role)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__start_02.add(Not(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _acceptOffer_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__acceptOffer_0 = z3.Solver() 
    solver__acceptOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__acceptOffer_0.push()
    
    solver__acceptOffer_0.add(ForAll([state,offer], Implies(And(True,True), True)))
    post_result = solver__acceptOffer_0.check() == z3.sat
    
    #check determinism
    solver__acceptOffer_0.pop()
    solver__acceptOffer_0.push()
    solver__acceptOffer_0.add(True) 
    eps_result = solver__acceptOffer_0.check() == z3.sat

    #check participants
    solver__acceptOffer_0.pop()
    solver__acceptOffer_0.add(Or('b' in O_role,'b' in B_role)) 
    part_result = solver__acceptOffer_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _acceptOffer_0: ", simplify(ForAll([state,offer], Implies(And(True,True), True))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "(Or('b' in O_role,'b' in B_role))")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__acceptOffer_02.add(Not(ForAll([state,offer], Implies(And(True,True), True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer], Implies(And(True,True), True)))), " :: ", solver__acceptOffer_02.check() == z3.sat)
            
          
                   
    return result
    



def _rejectOffer_0(infos = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__rejectOffer_0 = z3.Solver() 
    solver__rejectOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__rejectOffer_0.push()
    
    solver__rejectOffer_0.add(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))
    post_result = solver__rejectOffer_0.check() == z3.sat
    
    #check determinism
    solver__rejectOffer_0.pop()
    solver__rejectOffer_0.push()
    solver__rejectOffer_0.add(True) 
    eps_result = solver__rejectOffer_0.check() == z3.sat

    #check participants
    solver__rejectOffer_0.pop()
    solver__rejectOffer_0.add(Or('o' in O_role,'o' in B_role)) 
    part_result = solver__rejectOffer_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _rejectOffer_0: ", simplify(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "(Or('o' in O_role,'o' in B_role))")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__rejectOffer_02.add(Not(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))), " :: ", solver__rejectOffer_02.check() == z3.sat)
            
          
                   
    return result
    



def _makeOffer_0(infos = False):
    global offer  
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__makeOffer_0 = z3.Solver() 
    solver__makeOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__makeOffer_0.push()
    
    solver__makeOffer_0.add(ForAll([state,offer,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True))))
    post_result = solver__makeOffer_0.check() == z3.sat
    
    #check determinism
    solver__makeOffer_0.pop()
    solver__makeOffer_0.push()
    solver__makeOffer_0.add(True) 
    eps_result = solver__makeOffer_0.check() == z3.sat

    #check participants
    solver__makeOffer_0.pop()
    solver__makeOffer_0.add(Or('b' in O_role,'b' in B_role)) 
    part_result = solver__makeOffer_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _makeOffer_0: ", simplify(ForAll([state,offer,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True)))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "(Or('b' in O_role,'b' in B_role))")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(True))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__makeOffer_02.add(Not(ForAll([state,offer,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True))))), " :: ", solver__makeOffer_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _acceptOffer_0() and _rejectOffer_0() and _makeOffer_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
if not check_resut: 
    print('\nFunctions simplified formula and satisfiability results :')
    _start_0(True)
    _acceptOffer_0(True)
    _rejectOffer_0(True)
    _makeOffer_0(True)