from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

state = Int('state')
offer = Int('offer')
B = Array('B', IntSort(), IntSort())


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))



def _start_0(infos = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    solver__start_0.add(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0)))))
    post_result = solver__start_0.check() == z3.sat
    
    solver__start_0.pop()
    solver__start_0.add(And(ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))),ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))))) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))),ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))))))
            
        if not result: 
            solver__start_02.add(Not(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0)))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _acceptOffer_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__acceptOffer_0 = z3.Solver() 
    solver__acceptOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__acceptOffer_0.push()
    solver__acceptOffer_0.add(ForAll([state,offer,B], Implies(True, True)))
    post_result = solver__acceptOffer_0.check() == z3.sat
    
    solver__acceptOffer_0.pop()
    solver__acceptOffer_0.add(True) 
    eps_result = solver__acceptOffer_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _acceptOffer_0: ", simplify(ForAll([state,offer,B], Implies(True, True))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__acceptOffer_02.add(Not(ForAll([state,offer,B], Implies(True, True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer,B], Implies(True, True)))), " :: ", solver__acceptOffer_02.check() == z3.sat)
            
          
                   
    return result
    



def _rejectOffer_0(infos = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__rejectOffer_0 = z3.Solver() 
    solver__rejectOffer_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__rejectOffer_0.push()
    solver__rejectOffer_0.add(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0)))))
    post_result = solver__rejectOffer_0.check() == z3.sat
    
    solver__rejectOffer_0.pop()
    solver__rejectOffer_0.add(And(ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))),ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))))) 
    eps_result = solver__rejectOffer_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _rejectOffer_0: ", simplify(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))),ForAll([_offer], Implies(_offer  > 0,And(Not(_offer  > 0)))))))
            
        if not result: 
            solver__rejectOffer_02.add(Not(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0),Exists([_offer], _offer  > 0)))))), " :: ", solver__rejectOffer_02.check() == z3.sat)
            
          
                   
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
    solver__makeOffer_0.add(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True))))
    post_result = solver__makeOffer_0.check() == z3.sat
    
    solver__makeOffer_0.pop()
    solver__makeOffer_0.add(True) 
    eps_result = solver__makeOffer_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _makeOffer_0: ", simplify(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__makeOffer_02.add(Not(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True))))), " :: ", solver__makeOffer_02.check() == z3.sat)
            
          
                   
    return result
    

def _makeOffer_1(infos = False):
    global offer  
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__makeOffer_1 = z3.Solver() 
    solver__makeOffer_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__makeOffer_1.push()
    solver__makeOffer_1.add(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True))))
    post_result = solver__makeOffer_1.check() == z3.sat
    
    solver__makeOffer_1.pop()
    solver__makeOffer_1.add(True) 
    eps_result = solver__makeOffer_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _makeOffer_1: ", simplify(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__makeOffer_12.add(Not(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([state,offer,B,_offer], Implies(And(offer == _offer), Or(True,True))))), " :: ", solver__makeOffer_12.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _acceptOffer_0() and _rejectOffer_0() and _makeOffer_0() and _makeOffer_1())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_acceptOffer_0(True)

_rejectOffer_0(True)

_makeOffer_0(True)

_makeOffer_1(True)