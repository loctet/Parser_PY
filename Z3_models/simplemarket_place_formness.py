from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

state = Int('state')
offer = Int('offer')
B = Array('B', IntSort(), IntSort())


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
    #solver__start_0.add(True)
    solver__start_0.add(And('O' in ['O'], ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))))
    post_result = solver__start_0.check() == z3.sat
    #print((And('O' in ['O'], ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(And('O' in ['O'], ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__start_02.add(Not(And('O' in ['O'], ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And('O' in ['O'], ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _acceptOffer_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__acceptOffer_0 = z3.Solver() 
    solver__acceptOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__acceptOffer_0.push()
    #solver__acceptOffer_0.add(True)
    solver__acceptOffer_0.add(And(Or('b' in B_role), ForAll([state,offer,B], Implies(And(True,True), True))))
    post_result = solver__acceptOffer_0.check() == z3.sat
    #print((And(Or('b' in B_role), ForAll([state,offer,B], Implies(And(True,True), True)))), post_result)
    
    solver__acceptOffer_0.pop()
    solver__acceptOffer_0.add(True) 
    eps_result = solver__acceptOffer_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _acceptOffer_0: ", simplify(And(Or('b' in B_role), ForAll([state,offer,B], Implies(And(True,True), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__acceptOffer_02.add(Not(And(Or('b' in B_role), ForAll([state,offer,B], Implies(And(True,True), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('b' in B_role), ForAll([state,offer,B], Implies(And(True,True), True))))), " :: ", solver__acceptOffer_02.check() == z3.sat)
            
          
                   
    return result
    



def _rejectOffer_0(infos = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__rejectOffer_0 = z3.Solver() 
    solver__rejectOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__rejectOffer_0.push()
    #solver__rejectOffer_0.add(True)
    solver__rejectOffer_0.add(And(Or('o' in O_role), ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))))
    post_result = solver__rejectOffer_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))), post_result)
    
    solver__rejectOffer_0.pop()
    solver__rejectOffer_0.add(True) 
    eps_result = solver__rejectOffer_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _rejectOffer_0: ", simplify(And(Or('o' in O_role), ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__rejectOffer_02.add(Not(And(Or('o' in O_role), ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([state,offer,B], Implies(And(True,True), Or(Exists([_offer], _offer  > 0))))))), " :: ", solver__rejectOffer_02.check() == z3.sat)
            
          
                   
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
    #solver__makeOffer_0.add(_offer  > 0)
    solver__makeOffer_0.add(And(Or('b' in B_role), ForAll([state,offer,B,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True)))))
    post_result = solver__makeOffer_0.check() == z3.sat
    #print((And(Or('b' in B_role), ForAll([state,offer,B,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True))))), post_result)
    
    solver__makeOffer_0.pop()
    solver__makeOffer_0.add(True) 
    eps_result = solver__makeOffer_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _makeOffer_0: ", simplify(And(Or('b' in B_role), ForAll([state,offer,B,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__makeOffer_02.add(Not(And(Or('b' in B_role), ForAll([state,offer,B,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('b' in B_role), ForAll([state,offer,B,_offer], Implies(And(_offer  > 0,And(offer == _offer)), Or(True,True)))))), " :: ", solver__makeOffer_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _acceptOffer_0() and _rejectOffer_0() and _makeOffer_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_acceptOffer_0(True)

_rejectOffer_0(True)

_makeOffer_0(True)