from z3 import * 
from Z3.Extension import *

locked = Bool('locked')
requestedL = Bool('requestedL')


role_Owner = Array('Owner',IntSort() , StringSort())
Store(role_Owner, 0, String('Owner'))
role_BankAgent = Array('BankAgent',IntSort() , StringSort())
Store(role_BankAgent, 0, String('BankAgent'))
role_ThirdPartyRequestor = Array('ThirdPartyRequestor',IntSort() , StringSort())
Store(role_ThirdPartyRequestor, 0, String('ThirdPartyRequestor'))
role_CurrentAuthorizedUser = Array('CurrentAuthorizedUser',IntSort() , StringSort())
Store(role_CurrentAuthorizedUser, 0, String('CurrentAuthorizedUser'))



def _start_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.add(ForAll([locked,requestedL], Implies(True, Or(True))))
    result = solver__start_0.check() == z3.sat
    if minimize :
        print("--For _start_0: ", simplify(ForAll([locked,requestedL], Implies(True, Or(True)))), ":", result)
    return result
    





def _requestAvailability_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__requestAvailability_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__requestAvailability_0.add(ForAll([locked,requestedL], Implies(True, Or(True))))
    result = solver__requestAvailability_0.check() == z3.sat
    if minimize :
        print("--For _requestAvailability_0: ", simplify(ForAll([locked,requestedL], Implies(True, Or(True)))), ":", result)
    return result
    



def _reviewRequest_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__reviewRequest_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__reviewRequest_0.add(ForAll([locked,requestedL], Implies(True, Or(True))))
    result = solver__reviewRequest_0.check() == z3.sat
    if minimize :
        print("--For _reviewRequest_0: ", simplify(ForAll([locked,requestedL], Implies(True, Or(True)))), ":", result)
    return result
    



def _uploadDigitalAsset_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__uploadDigitalAsset_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__uploadDigitalAsset_0.add(ForAll([locked,requestedL], Implies(True, Or(True,locked == False,True))))
    result = solver__uploadDigitalAsset_0.check() == z3.sat
    if minimize :
        print("--For _uploadDigitalAsset_0: ", simplify(ForAll([locked,requestedL], Implies(True, Or(True,locked == False,True)))), ":", result)
    return result
    



def _ShareThirdPartyRequest_0(minimize = False):
    global locked 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__ShareThirdPartyRequest_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ShareThirdPartyRequest_0.add(ForAll([locked,requestedL], Implies(And(locked  ==  True), Or(locked == True,True))))
    result = solver__ShareThirdPartyRequest_0.check() == z3.sat
    if minimize :
        print("--For _ShareThirdPartyRequest_0: ", simplify(ForAll([locked,requestedL], Implies(And(locked  ==  True), Or(locked == True,True)))), ":", result)
    return result
    



def _requestAccessLocker_0(minimize = False):
    global locked 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__requestAccessLocker_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__requestAccessLocker_0.add(ForAll([locked,requestedL], Implies(And(locked  ==  False), Or(locked == False,locked == False,True))))
    result = solver__requestAccessLocker_0.check() == z3.sat
    if minimize :
        print("--For _requestAccessLocker_0: ", simplify(ForAll([locked,requestedL], Implies(And(locked  ==  False), Or(locked == False,locked == False,True)))), ":", result)
    return result
    



def _terminateSharing_0(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateSharing_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateSharing_0.add(ForAll([locked,requestedL], Implies(True, True)))
    result = solver__terminateSharing_0.check() == z3.sat
    if minimize :
        print("--For _terminateSharing_0: ", simplify(ForAll([locked,requestedL], Implies(True, True))), ":", result)
    return result
    

def _terminateSharing_1(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateSharing_1 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateSharing_1.add(ForAll([locked,requestedL], Implies(True, True)))
    result = solver__terminateSharing_1.check() == z3.sat
    if minimize :
        print("--For _terminateSharing_1: ", simplify(ForAll([locked,requestedL], Implies(True, True))), ":", result)
    return result
    

def _terminateSharing_2(minimize = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateSharing_2 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateSharing_2.add(ForAll([locked,requestedL], Implies(True, True)))
    result = solver__terminateSharing_2.check() == z3.sat
    if minimize :
        print("--For _terminateSharing_2: ", simplify(ForAll([locked,requestedL], Implies(True, True))), ":", result)
    return result
    



def _revokeThirdPartyRequest_0(minimize = False):
    global locked 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__revokeThirdPartyRequest_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__revokeThirdPartyRequest_0.add(ForAll([locked,requestedL], Implies(And(locked  ==  False), Or(True,locked == False,True))))
    result = solver__revokeThirdPartyRequest_0.check() == z3.sat
    if minimize :
        print("--For _revokeThirdPartyRequest_0: ", simplify(ForAll([locked,requestedL], Implies(And(locked  ==  False), Or(True,locked == False,True)))), ":", result)
    return result
    



def _revokeGrantAccessLocker_0(minimize = False):
    global locked 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__revokeGrantAccessLocker_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__revokeGrantAccessLocker_0.add(ForAll([locked,requestedL], Implies(And(locked  ==  False), Or(True,locked == False,True))))
    result = solver__revokeGrantAccessLocker_0.check() == z3.sat
    if minimize :
        print("--For _revokeGrantAccessLocker_0: ", simplify(ForAll([locked,requestedL], Implies(And(locked  ==  False), Or(True,locked == False,True)))), ":", result)
    return result
    



def _grantAccessLocker_0(minimize = False):
    global locked 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__grantAccessLocker_0 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__grantAccessLocker_0.add(ForAll([locked,requestedL], Implies(And(locked  ==  True), Or(locked == True,True))))
    result = solver__grantAccessLocker_0.check() == z3.sat
    if minimize :
        print("--For _grantAccessLocker_0: ", simplify(ForAll([locked,requestedL], Implies(And(locked  ==  True), Or(locked == True,True)))), ":", result)
    return result
    
check_resut = (_start_0() and _requestAvailability_0() and _reviewRequest_0() and _uploadDigitalAsset_0() and _ShareThirdPartyRequest_0() and _requestAccessLocker_0() and _terminateSharing_0() and _terminateSharing_1() and _terminateSharing_2() and _revokeThirdPartyRequest_0() and _revokeGrantAccessLocker_0() and _grantAccessLocker_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_requestAvailability_0(True)

_reviewRequest_0(True)

_uploadDigitalAsset_0(True)

_ShareThirdPartyRequest_0(True)

_requestAccessLocker_0(True)

_terminateSharing_0(True)

_terminateSharing_1(True)

_terminateSharing_2(True)

_revokeThirdPartyRequest_0(True)

_revokeGrantAccessLocker_0(True)

_grantAccessLocker_0(True)