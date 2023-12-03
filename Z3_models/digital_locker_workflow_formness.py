from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

locked = Bool('locked')
requestedL = Bool('requestedL')


Owner_role = []
Owner_role.append('Owner')
BankAgent_role = []
BankAgent_role.append('BankAgent')
ThirdPartyRequestor_role = []
ThirdPartyRequestor_role.append('ThirdPartyRequestor')
CurrentAuthorizedUser_role = []
CurrentAuthorizedUser_role.append('CurrentAuthorizedUser')



def _start_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    #solver__start_0.add(True)
    solver__start_0.add(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True)))))
    post_result = solver__start_0.check() == z3.sat
    #print((And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__start_02.add(Not(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True)))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _revokeGrantAccessLocker_0(infos = False):
    global locked 
    # Declare variable before   
    locked_old = Bool('locked_old')
    
    
    #building the solver for the predancontion
    solver__revokeGrantAccessLocker_0 = z3.Solver() 
    solver__revokeGrantAccessLocker_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__revokeGrantAccessLocker_0.push()
    #solver__revokeGrantAccessLocker_0.add(locked_old == False)
    solver__revokeGrantAccessLocker_0.add(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(True,locked == False,True)))))
    post_result = solver__revokeGrantAccessLocker_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(True,locked == False,True))))), post_result)
    
    solver__revokeGrantAccessLocker_0.pop()
    solver__revokeGrantAccessLocker_0.add(True) 
    eps_result = solver__revokeGrantAccessLocker_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _revokeGrantAccessLocker_0: ", simplify(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(True,locked == False,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__revokeGrantAccessLocker_02.add(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(True,locked == False,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(True,locked == False,True)))))), " :: ", solver__revokeGrantAccessLocker_02.check() == z3.sat)
            
          
                   
    return result
    



def _grantAccessLocker_0(infos = False):
    global locked 
    # Declare variable before   
    locked_old = Bool('locked_old')
    
    
    #building the solver for the predancontion
    solver__grantAccessLocker_0 = z3.Solver() 
    solver__grantAccessLocker_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__grantAccessLocker_0.push()
    #solver__grantAccessLocker_0.add(locked_old == False)
    solver__grantAccessLocker_0.add(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == True)), Or(locked == True,True)))))
    post_result = solver__grantAccessLocker_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == True)), Or(locked == True,True))))), post_result)
    
    solver__grantAccessLocker_0.pop()
    solver__grantAccessLocker_0.add(True) 
    eps_result = solver__grantAccessLocker_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _grantAccessLocker_0: ", simplify(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == True)), Or(locked == True,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__grantAccessLocker_02.add(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == True)), Or(locked == True,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == True)), Or(locked == True,True)))))), " :: ", solver__grantAccessLocker_02.check() == z3.sat)
            
          
                   
    return result
    



def _terminateSharing_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateSharing_0 = z3.Solver() 
    solver__terminateSharing_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateSharing_0.push()
    #solver__terminateSharing_0.add(True)
    solver__terminateSharing_0.add(And(True, ForAll([locked,requestedL], Implies(And(True,True), True))))
    post_result = solver__terminateSharing_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))), post_result)
    
    solver__terminateSharing_0.pop()
    solver__terminateSharing_0.add(True) 
    eps_result = solver__terminateSharing_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _terminateSharing_0: ", simplify(And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__terminateSharing_02.add(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), True))))), " :: ", solver__terminateSharing_02.check() == z3.sat)
            
          
                   
    return result
    

def _terminateSharing_1(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateSharing_1 = z3.Solver() 
    solver__terminateSharing_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateSharing_1.push()
    #solver__terminateSharing_1.add(True)
    solver__terminateSharing_1.add(And(True, ForAll([locked,requestedL], Implies(And(True,True), True))))
    post_result = solver__terminateSharing_1.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))), post_result)
    
    solver__terminateSharing_1.pop()
    solver__terminateSharing_1.add(True) 
    eps_result = solver__terminateSharing_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _terminateSharing_1: ", simplify(And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__terminateSharing_12.add(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), True))))), " :: ", solver__terminateSharing_12.check() == z3.sat)
            
          
                   
    return result
    

def _terminateSharing_2(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__terminateSharing_2 = z3.Solver() 
    solver__terminateSharing_22 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__terminateSharing_2.push()
    #solver__terminateSharing_2.add(True)
    solver__terminateSharing_2.add(And(True, ForAll([locked,requestedL], Implies(And(True,True), True))))
    post_result = solver__terminateSharing_2.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))), post_result)
    
    solver__terminateSharing_2.pop()
    solver__terminateSharing_2.add(True) 
    eps_result = solver__terminateSharing_2.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _terminateSharing_2: ", simplify(And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__terminateSharing_22.add(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), True))))), " :: ", solver__terminateSharing_22.check() == z3.sat)
            
          
                   
    return result
    



def _revokeThirdPartyRequest_0(infos = False):
    global locked 
    # Declare variable before   
    locked_old = Bool('locked_old')
    
    
    #building the solver for the predancontion
    solver__revokeThirdPartyRequest_0 = z3.Solver() 
    solver__revokeThirdPartyRequest_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__revokeThirdPartyRequest_0.push()
    #solver__revokeThirdPartyRequest_0.add(locked_old == True)
    solver__revokeThirdPartyRequest_0.add(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == True,And(locked == False)), Or(True,locked == False,True)))))
    post_result = solver__revokeThirdPartyRequest_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == True,And(locked == False)), Or(True,locked == False,True))))), post_result)
    
    solver__revokeThirdPartyRequest_0.pop()
    solver__revokeThirdPartyRequest_0.add(True) 
    eps_result = solver__revokeThirdPartyRequest_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _revokeThirdPartyRequest_0: ", simplify(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == True,And(locked == False)), Or(True,locked == False,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__revokeThirdPartyRequest_02.add(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == True,And(locked == False)), Or(True,locked == False,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == True,And(locked == False)), Or(True,locked == False,True)))))), " :: ", solver__revokeThirdPartyRequest_02.check() == z3.sat)
            
          
                   
    return result
    



def _ShareThirdPartyRequest_0(infos = False):
    global locked 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__ShareThirdPartyRequest_0 = z3.Solver() 
    solver__ShareThirdPartyRequest_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ShareThirdPartyRequest_0.push()
    #solver__ShareThirdPartyRequest_0.add(True)
    solver__ShareThirdPartyRequest_0.add(And(True, ForAll([locked,requestedL], Implies(And(True,And(locked == True)), Or(locked == True,True)))))
    post_result = solver__ShareThirdPartyRequest_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL], Implies(And(True,And(locked == True)), Or(locked == True,True))))), post_result)
    
    solver__ShareThirdPartyRequest_0.pop()
    solver__ShareThirdPartyRequest_0.add(True) 
    eps_result = solver__ShareThirdPartyRequest_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _ShareThirdPartyRequest_0: ", simplify(And(True, ForAll([locked,requestedL], Implies(And(True,And(locked == True)), Or(locked == True,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__ShareThirdPartyRequest_02.add(Not(And(True, ForAll([locked,requestedL], Implies(And(True,And(locked == True)), Or(locked == True,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL], Implies(And(True,And(locked == True)), Or(locked == True,True)))))), " :: ", solver__ShareThirdPartyRequest_02.check() == z3.sat)
            
          
                   
    return result
    



def _requestAccessLocker_0(infos = False):
    global locked 
    # Declare variable before   
    locked_old = Bool('locked_old')
    
    
    #building the solver for the predancontion
    solver__requestAccessLocker_0 = z3.Solver() 
    solver__requestAccessLocker_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__requestAccessLocker_0.push()
    #solver__requestAccessLocker_0.add(locked_old == False)
    solver__requestAccessLocker_0.add(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(locked == False,locked == False,True)))))
    post_result = solver__requestAccessLocker_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(locked == False,locked == False,True))))), post_result)
    
    solver__requestAccessLocker_0.pop()
    solver__requestAccessLocker_0.add(True) 
    eps_result = solver__requestAccessLocker_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _requestAccessLocker_0: ", simplify(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(locked == False,locked == False,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__requestAccessLocker_02.add(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(locked == False,locked == False,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL,locked_old], Implies(And(locked_old == False,And(locked == False)), Or(locked == False,locked == False,True)))))), " :: ", solver__requestAccessLocker_02.check() == z3.sat)
            
          
                   
    return result
    



def _uploadDigitalAsset_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__uploadDigitalAsset_0 = z3.Solver() 
    solver__uploadDigitalAsset_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__uploadDigitalAsset_0.push()
    #solver__uploadDigitalAsset_0.add(True)
    solver__uploadDigitalAsset_0.add(And(True, ForAll([locked,requestedL], Implies(And(True,True), Or(True,locked == False,True)))))
    post_result = solver__uploadDigitalAsset_0.check() == z3.sat
    #print((And(True, ForAll([locked,requestedL], Implies(And(True,True), Or(True,locked == False,True))))), post_result)
    
    solver__uploadDigitalAsset_0.pop()
    solver__uploadDigitalAsset_0.add(True) 
    eps_result = solver__uploadDigitalAsset_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _uploadDigitalAsset_0: ", simplify(And(True, ForAll([locked,requestedL], Implies(And(True,True), Or(True,locked == False,True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__uploadDigitalAsset_02.add(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), Or(True,locked == False,True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(True, ForAll([locked,requestedL], Implies(And(True,True), Or(True,locked == False,True)))))), " :: ", solver__uploadDigitalAsset_02.check() == z3.sat)
            
          
                   
    return result
    



def _reviewRequest_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__reviewRequest_0 = z3.Solver() 
    solver__reviewRequest_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__reviewRequest_0.push()
    #solver__reviewRequest_0.add(True)
    solver__reviewRequest_0.add(And(Or('BankAgent' in BankAgent_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True)))))
    post_result = solver__reviewRequest_0.check() == z3.sat
    #print((And(Or('BankAgent' in BankAgent_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))), post_result)
    
    solver__reviewRequest_0.pop()
    solver__reviewRequest_0.add(True) 
    eps_result = solver__reviewRequest_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _reviewRequest_0: ", simplify(And(Or('BankAgent' in BankAgent_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__reviewRequest_02.add(Not(And(Or('BankAgent' in BankAgent_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('BankAgent' in BankAgent_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True)))))), " :: ", solver__reviewRequest_02.check() == z3.sat)
            
          
                   
    return result
    



def _requestAvailability_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__requestAvailability_0 = z3.Solver() 
    solver__requestAvailability_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__requestAvailability_0.push()
    #solver__requestAvailability_0.add(True)
    solver__requestAvailability_0.add(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True)))))
    post_result = solver__requestAvailability_0.check() == z3.sat
    #print((And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))), post_result)
    
    solver__requestAvailability_0.pop()
    solver__requestAvailability_0.add(True) 
    eps_result = solver__requestAvailability_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _requestAvailability_0: ", simplify(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__requestAvailability_02.add(Not(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('Owner' in Owner_role), ForAll([locked,requestedL], Implies(And(True,True), Or(True)))))), " :: ", solver__requestAvailability_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _revokeGrantAccessLocker_0() and _grantAccessLocker_0() and _terminateSharing_0() and _terminateSharing_1() and _terminateSharing_2() and _revokeThirdPartyRequest_0() and _ShareThirdPartyRequest_0() and _requestAccessLocker_0() and _uploadDigitalAsset_0() and _reviewRequest_0() and _requestAvailability_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_revokeGrantAccessLocker_0(True)

_grantAccessLocker_0(True)

_terminateSharing_0(True)

_terminateSharing_1(True)

_terminateSharing_2(True)

_revokeThirdPartyRequest_0(True)

_ShareThirdPartyRequest_0(True)

_requestAccessLocker_0(True)

_uploadDigitalAsset_0(True)

_reviewRequest_0(True)

_requestAvailability_0(True)