from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

approvedOwners = Array('approvedOwners', IntSort(), StringSort())
pendingTransactions = Int('pendingTransactions')
transaction = String('transaction')
minApprNumber = Int('minApprNumber')
empty = Array('empty', IntSort(), StringSort())
num_validator = Int('num_validator')


o_role = []
o_role.append('O')
O_role = []
O_role.append('o')







def _initializeWallet_0(infos = False):
    global minApprNumber 
    # Declare variable before   
    _transaction = String('_transaction')
    _min = Int('_min')
    
    
    #building the solver for the predancontion
    solver__initializeWallet_0 = z3.Solver() 
    solver__initializeWallet_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__initializeWallet_0.push()
    #solver__initializeWallet_0.add(True)
    solver__initializeWallet_0.add(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_min], Implies(And(True,And(minApprNumber == _min)), Or(Exists([_transaction], True))))))
    post_result = solver__initializeWallet_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_min], Implies(And(True,And(minApprNumber == _min)), Or(Exists([_transaction], True)))))), post_result)
    
    solver__initializeWallet_0.pop()
    solver__initializeWallet_0.add(True) 
    eps_result = solver__initializeWallet_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _initializeWallet_0: ", simplify(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_min], Implies(And(True,And(minApprNumber == _min)), Or(Exists([_transaction], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__initializeWallet_02.add(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_min], Implies(And(True,And(minApprNumber == _min)), Or(Exists([_transaction], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_min], Implies(And(True,And(minApprNumber == _min)), Or(Exists([_transaction], True))))))), " :: ", solver__initializeWallet_02.check() == z3.sat)
            
          
                   
    return result
    



def _resetWallet_0(infos = False):
    global pendingTransactions 
    global approvedOwners 
    # Declare variable before   
    _transaction = String('_transaction')
    
    
    #building the solver for the predancontion
    solver__resetWallet_0 = z3.Solver() 
    solver__resetWallet_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__resetWallet_0.push()
    #solver__resetWallet_0.add(True)
    solver__resetWallet_0.add(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True))))))
    post_result = solver__resetWallet_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True)))))), post_result)
    
    solver__resetWallet_0.pop()
    solver__resetWallet_0.add(True) 
    eps_result = solver__resetWallet_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _resetWallet_0: ", simplify(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__resetWallet_02.add(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True))))))), " :: ", solver__resetWallet_02.check() == z3.sat)
            
          
                   
    return result
    

def _resetWallet_1(infos = False):
    global pendingTransactions 
    global approvedOwners 
    # Declare variable before   
    _transaction = String('_transaction')
    
    
    #building the solver for the predancontion
    solver__resetWallet_1 = z3.Solver() 
    solver__resetWallet_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__resetWallet_1.push()
    #solver__resetWallet_1.add(True)
    solver__resetWallet_1.add(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True))))))
    post_result = solver__resetWallet_1.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True)))))), post_result)
    
    solver__resetWallet_1.pop()
    solver__resetWallet_1.add(True) 
    eps_result = solver__resetWallet_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _resetWallet_1: ", simplify(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__resetWallet_12.add(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator], Implies(And(True,And(pendingTransactions == 0, approvedOwners == empty)), Or(Exists([_transaction], True))))))), " :: ", solver__resetWallet_12.check() == z3.sat)
            
          
                   
    return result
    



def _executeTransaction_0(infos = False):
    global num_validator 
    global pendingTransactions 
    # Declare variable before   
    _transaction = String('_transaction')
    num_validator_old = Int('num_validator_old')
    
    
    #building the solver for the predancontion
    solver__executeTransaction_0 = z3.Solver() 
    solver__executeTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__executeTransaction_0.push()
    #solver__executeTransaction_0.add(num_validator_old >= minApprNumber)
    solver__executeTransaction_0.add(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,num_validator_old], Implies(And(num_validator_old >= minApprNumber,And(num_validator == 0, pendingTransactions == 0)), Or(True)))))
    post_result = solver__executeTransaction_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,num_validator_old], Implies(And(num_validator_old >= minApprNumber,And(num_validator == 0, pendingTransactions == 0)), Or(True))))), post_result)
    
    solver__executeTransaction_0.pop()
    solver__executeTransaction_0.add(True) 
    eps_result = solver__executeTransaction_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _executeTransaction_0: ", simplify(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,num_validator_old], Implies(And(num_validator_old >= minApprNumber,And(num_validator == 0, pendingTransactions == 0)), Or(True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__executeTransaction_02.add(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,num_validator_old], Implies(And(num_validator_old >= minApprNumber,And(num_validator == 0, pendingTransactions == 0)), Or(True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,num_validator_old], Implies(And(num_validator_old >= minApprNumber,And(num_validator == 0, pendingTransactions == 0)), Or(True)))))), " :: ", solver__executeTransaction_02.check() == z3.sat)
            
          
                   
    return result
    



def _approveTransaction_0(infos = False):
    global num_validator 
    # Declare variable before   
    _transaction = String('_transaction')
    num_validator_old = Int('num_validator_old')
    
    
    #building the solver for the predancontion
    solver__approveTransaction_0 = z3.Solver() 
    solver__approveTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__approveTransaction_0.push()
    #solver__approveTransaction_0.add('o' not in O_role)
    solver__approveTransaction_0.add(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,num_validator_old], Implies(And('o' not in O_role,And(num_validator == num_validator_old + 1)), Or(Exists([_transaction], num_validator >= minApprNumber),True)))))
    post_result = solver__approveTransaction_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,num_validator_old], Implies(And('o' not in O_role,And(num_validator == num_validator_old + 1)), Or(Exists([_transaction], num_validator >= minApprNumber),True))))), post_result)
    
    solver__approveTransaction_0.pop()
    solver__approveTransaction_0.add(True) 
    eps_result = solver__approveTransaction_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _approveTransaction_0: ", simplify(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,num_validator_old], Implies(And('o' not in O_role,And(num_validator == num_validator_old + 1)), Or(Exists([_transaction], num_validator >= minApprNumber),True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__approveTransaction_02.add(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,num_validator_old], Implies(And('o' not in O_role,And(num_validator == num_validator_old + 1)), Or(Exists([_transaction], num_validator >= minApprNumber),True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,num_validator_old], Implies(And('o' not in O_role,And(num_validator == num_validator_old + 1)), Or(Exists([_transaction], num_validator >= minApprNumber),True)))))), " :: ", solver__approveTransaction_02.check() == z3.sat)
            
          
                   
    return result
    



def _submitTransaction_0(infos = False):
    global pendingTransactions 
    global approvedOwners 
    global transaction 
    # Declare variable before   
    _transaction = String('_transaction')
    pendingTransactions_old = Int('pendingTransactions_old')
    
    
    #building the solver for the predancontion
    solver__submitTransaction_0 = z3.Solver() 
    solver__submitTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__submitTransaction_0.push()
    #solver__submitTransaction_0.add(True)
    solver__submitTransaction_0.add(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,pendingTransactions_old], Implies(And(True,And(pendingTransactions == pendingTransactions_old + 1, approvedOwners == empty, transaction.eq(_transaction))), Or('o' not in O_role)))))
    post_result = solver__submitTransaction_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,pendingTransactions_old], Implies(And(True,And(pendingTransactions == pendingTransactions_old + 1, approvedOwners == empty, transaction.eq(_transaction))), Or('o' not in O_role))))), post_result)
    
    solver__submitTransaction_0.pop()
    solver__submitTransaction_0.add(True) 
    eps_result = solver__submitTransaction_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _submitTransaction_0: ", simplify(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,pendingTransactions_old], Implies(And(True,And(pendingTransactions == pendingTransactions_old + 1, approvedOwners == empty, transaction.eq(_transaction))), Or('o' not in O_role))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__submitTransaction_02.add(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,pendingTransactions_old], Implies(And(True,And(pendingTransactions == pendingTransactions_old + 1, approvedOwners == empty, transaction.eq(_transaction))), Or('o' not in O_role))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([approvedOwners,pendingTransactions,transaction,minApprNumber,empty,num_validator,_transaction,pendingTransactions_old], Implies(And(True,And(pendingTransactions == pendingTransactions_old + 1, approvedOwners == empty, transaction.eq(_transaction))), Or('o' not in O_role)))))), " :: ", solver__submitTransaction_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_initializeWallet_0() and _resetWallet_0() and _resetWallet_1() and _executeTransaction_0() and _approveTransaction_0() and _submitTransaction_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_initializeWallet_0(True)

_resetWallet_0(True)

_resetWallet_1(True)

_executeTransaction_0(True)

_approveTransaction_0(True)

_submitTransaction_0(True)