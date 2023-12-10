from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

owners = Array('owners', IntSort(), StringSort())
pendingTransactions = Array('pendingTransactions', IntSort(), StringSort())
approvedOwners = Array('approvedOwners', IntSort(), StringSort())
executedTransaction = String('executedTransaction')
empty = Array('empty', IntSort(), StringSort())
minAppr = Int('minAppr')


o_role = []
o_role.append('O')
O_role = []
O_role.append('o')
Owner_role = []
Owner_role.append('Owner')







def _initializeWallet_0(infos = False):
    global pendingTransactions 
    global approvedOwners 
    global executedTransaction 
    # Declare variable before   
    _transaction = String('_transaction')
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__initializeWallet_0 = z3.Solver() 
    solver__initializeWallet_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__initializeWallet_0.push()
    #solver__initializeWallet_0.add(True)
    solver__initializeWallet_0.add(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True))))))
    post_result = solver__initializeWallet_0.check() == z3.sat
    #print((And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True)))))), post_result)
    
    solver__initializeWallet_0.pop()
    solver__initializeWallet_0.add(True) 
    eps_result = solver__initializeWallet_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _initializeWallet_0: ", simplify(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__initializeWallet_02.add(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True))))))), " :: ", solver__initializeWallet_02.check() == z3.sat)
            
          
                   
    return result
    



def _resetWallet_0(infos = False):
    global pendingTransactions 
    global approvedOwners 
    global executedTransaction 
    # Declare variable before   
    _transaction = String('_transaction')
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__resetWallet_0 = z3.Solver() 
    solver__resetWallet_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__resetWallet_0.push()
    #solver__resetWallet_0.add(True)
    solver__resetWallet_0.add(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True))))))
    post_result = solver__resetWallet_0.check() == z3.sat
    #print((And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True)))))), post_result)
    
    solver__resetWallet_0.pop()
    solver__resetWallet_0.add(True) 
    eps_result = solver__resetWallet_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _resetWallet_0: ", simplify(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__resetWallet_02.add(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(True,And(pendingTransactions == empty, approvedOwners == empty, executedTransaction.eq(None))), Or(Exists([_transaction], True))))))), " :: ", solver__resetWallet_02.check() == z3.sat)
            
          
                   
    return result
    



def _executeTransaction_0(infos = False):
    global executedTransaction 
    # Declare variable before   
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__executeTransaction_0 = z3.Solver() 
    solver__executeTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__executeTransaction_0.push()
    #solver__executeTransaction_0.add(len(approvedOwners) >= minAppr)
    solver__executeTransaction_0.add(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(pendingTransactions[-1]))), Or(Exists([_owner], True))))))
    post_result = solver__executeTransaction_0.check() == z3.sat
    #print((And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(pendingTransactions[-1]))), Or(Exists([_owner], True)))))), post_result)
    
    solver__executeTransaction_0.pop()
    solver__executeTransaction_0.add(True) 
    eps_result = solver__executeTransaction_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _executeTransaction_0: ", simplify(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(pendingTransactions[-1]))), Or(Exists([_owner], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__executeTransaction_02.add(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(pendingTransactions[-1]))), Or(Exists([_owner], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(pendingTransactions[-1]))), Or(Exists([_owner], True))))))), " :: ", solver__executeTransaction_02.check() == z3.sat)
            
          
                   
    return result
    

def _executeTransaction_1(infos = False):
    global executedTransaction 
    # Declare variable before   
    _owner = String('_owner')
    _transaction = String('_transaction')
    
    
    #building the solver for the predancontion
    solver__executeTransaction_1 = z3.Solver() 
    solver__executeTransaction_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__executeTransaction_1.push()
    #solver__executeTransaction_1.add(len(approvedOwners) >= minAppr)
    solver__executeTransaction_1.add(And(Or('' in O_role,'' in Owner_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(_transaction))), Or(Exists([_owner], True))))))
    post_result = solver__executeTransaction_1.check() == z3.sat
    #print((And(Or('' in O_role,'' in Owner_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(_transaction))), Or(Exists([_owner], True)))))), post_result)
    
    solver__executeTransaction_1.pop()
    solver__executeTransaction_1.add(True) 
    eps_result = solver__executeTransaction_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _executeTransaction_1: ", simplify(And(Or('' in O_role,'' in Owner_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(_transaction))), Or(Exists([_owner], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__executeTransaction_12.add(Not(And(Or('' in O_role,'' in Owner_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(_transaction))), Or(Exists([_owner], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('' in O_role,'' in Owner_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(len(approvedOwners) >= minAppr,And(executedTransaction.eq(_transaction))), Or(Exists([_owner], True))))))), " :: ", solver__executeTransaction_12.check() == z3.sat)
            
          
                   
    return result
    



def _approveTransaction_0(infos = False):
    global approvedOwners[len(approvedOwners)] 
    # Declare variable before   
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__approveTransaction_0 = z3.Solver() 
    solver__approveTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__approveTransaction_0.push()
    #solver__approveTransaction_0.add(_owner not in approvedOwners)
    solver__approveTransaction_0.add(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(_owner not in approvedOwners,And(approvedOwners[len(approvedOwners)] == _owner)), Or(len(approvedOwners) >= minAppr)))))
    post_result = solver__approveTransaction_0.check() == z3.sat
    #print((And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(_owner not in approvedOwners,And(approvedOwners[len(approvedOwners)] == _owner)), Or(len(approvedOwners) >= minAppr))))), post_result)
    
    solver__approveTransaction_0.pop()
    solver__approveTransaction_0.add(True) 
    eps_result = solver__approveTransaction_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _approveTransaction_0: ", simplify(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(_owner not in approvedOwners,And(approvedOwners[len(approvedOwners)] == _owner)), Or(len(approvedOwners) >= minAppr))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__approveTransaction_02.add(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(_owner not in approvedOwners,And(approvedOwners[len(approvedOwners)] == _owner)), Or(len(approvedOwners) >= minAppr))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_owner], Implies(And(_owner not in approvedOwners,And(approvedOwners[len(approvedOwners)] == _owner)), Or(len(approvedOwners) >= minAppr)))))), " :: ", solver__approveTransaction_02.check() == z3.sat)
            
          
                   
    return result
    



def _submitTransaction_0(infos = False):
    global pendingTransactions[len(pendingTransactions)] 
    global approvedOwners 
    # Declare variable before   
    _owner = String('_owner')
    _transaction = String('_transaction')
    _transaction = String('_transaction')
    
    
    #building the solver for the predancontion
    solver__submitTransaction_0 = z3.Solver() 
    solver__submitTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__submitTransaction_0.push()
    #solver__submitTransaction_0.add(True)
    solver__submitTransaction_0.add(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(True,And(pendingTransactions[len(pendingTransactions)] == _transaction, approvedOwners == empty)), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= minAppr))))))
    post_result = solver__submitTransaction_0.check() == z3.sat
    #print((And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(True,And(pendingTransactions[len(pendingTransactions)] == _transaction, approvedOwners == empty)), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= minAppr)))))), post_result)
    
    solver__submitTransaction_0.pop()
    solver__submitTransaction_0.add(True) 
    eps_result = solver__submitTransaction_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _submitTransaction_0: ", simplify(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(True,And(pendingTransactions[len(pendingTransactions)] == _transaction, approvedOwners == empty)), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= minAppr)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__submitTransaction_02.add(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(True,And(pendingTransactions[len(pendingTransactions)] == _transaction, approvedOwners == empty)), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= minAppr)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('' in O_role), ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,minAppr,_transaction], Implies(And(True,And(pendingTransactions[len(pendingTransactions)] == _transaction, approvedOwners == empty)), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= minAppr))))))), " :: ", solver__submitTransaction_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_initializeWallet_0() and _resetWallet_0() and _executeTransaction_0() and _executeTransaction_1() and _approveTransaction_0() and _submitTransaction_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_initializeWallet_0(True)

_resetWallet_0(True)

_executeTransaction_0(True)

_executeTransaction_1(True)

_approveTransaction_0(True)

_submitTransaction_0(True)