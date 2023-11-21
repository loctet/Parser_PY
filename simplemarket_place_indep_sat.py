from z3 import * 
from Z3.Extension import *

state = Int('state')
offer = Int('offer')
B = Array('B', IntSort(), IntSort())


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))



def _start_0(minimize = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.add(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0)))))
    result = solver__start_0.check() == z3.sat
    if minimize :
        print("--For _start_0: ", simplify(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0))))), ":", result)
    return result
    





def _makeOffer_0(minimize = False):
    global offer  
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__makeOffer_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__makeOffer_0.add(ForAll([state,offer,B,_offer], Implies(And(offer   ==  _offer), Or(True,True))))
    result = solver__makeOffer_0.check() == z3.sat
    if minimize :
        print("--For _makeOffer_0: ", simplify(ForAll([state,offer,B,_offer], Implies(And(offer   ==  _offer), Or(True,True)))), ":", result)
    return result
    



def _acceptOffer_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__acceptOffer_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__acceptOffer_0.add(ForAll([state,offer,B], Implies(True, True)))
    result = solver__acceptOffer_0.check() == z3.sat
    if minimize :
        print("--For _acceptOffer_0: ", simplify(ForAll([state,offer,B], Implies(True, True))), ":", result)
    return result
    



def _rejectOffer_0(minimize = False):
    
    # Declare variable before   
    _offer = Int('_offer')
    
    
    #building the solver for the predancontion
    solver__rejectOffer_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__rejectOffer_0.add(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0)))))
    result = solver__rejectOffer_0.check() == z3.sat
    if minimize :
        print("--For _rejectOffer_0: ", simplify(ForAll([state,offer,B], Implies(True, Or(Exists([_offer], _offer  > 0))))), ":", result)
    return result
    
check_resut = (_start_0() and _makeOffer_0() and _acceptOffer_0() and _rejectOffer_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_makeOffer_0(True)

_acceptOffer_0(True)

_rejectOffer_0(True)