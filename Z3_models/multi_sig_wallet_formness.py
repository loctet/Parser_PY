from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

owners = Array('owners', IntSort(), StringSort())
pendingTransactions = Array('pendingTransactions', IntSort(), StringSort())
approvedOwners = Array('approvedOwners', IntSort(), StringSort())
executedTransaction = String('executedTransaction')
empty = Array('empty', IntSort(), StringSort())


role_Owner = Array('Owner',IntSort() , StringSort())
Store(role_Owner, 0, String('Owner'))







def _initializeWallet_0(minimize = False):
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
    solver__initializeWallet_0.add(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True)))))
    result = solver__initializeWallet_0.check() == z3.sat
    if minimize :
        print("--For _initializeWallet_0: ", simplify(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True))))), " :: ", result)
        if not result: 
            solver__initializeWallet_02.add(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True)))))), " :: ", solver__initializeWallet_02.check() == z3.sat)
            if solver__initializeWallet_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__initializeWallet_02.model() , "\n")
                
    return result
    



def _resetWallet_0(minimize = False):
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
    solver__resetWallet_0.add(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True)))))
    result = solver__resetWallet_0.check() == z3.sat
    if minimize :
        print("--For _resetWallet_0: ", simplify(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True))))), " :: ", result)
        if not result: 
            solver__resetWallet_02.add(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(pendingTransactions  ==  empty ,  approvedOwners  ==  empty ,  executedTransaction  ==  None), Or(Exists([_transaction], True)))))), " :: ", solver__resetWallet_02.check() == z3.sat)
            if solver__resetWallet_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__resetWallet_02.model() , "\n")
                
    return result
    



def _executeTransaction_0(minimize = False):
    global executedTransaction 
    # Declare variable before   
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__executeTransaction_0 = z3.Solver() 
    solver__executeTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__executeTransaction_0.add(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty], Implies(And(executedTransaction  ==  pendingTransactions[-1]), Or(Exists([_owner], True)))))
    result = solver__executeTransaction_0.check() == z3.sat
    if minimize :
        print("--For _executeTransaction_0: ", simplify(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty], Implies(And(executedTransaction  ==  pendingTransactions[-1]), Or(Exists([_owner], True))))), " :: ", result)
        if not result: 
            solver__executeTransaction_02.add(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty], Implies(And(executedTransaction  ==  pendingTransactions[-1]), Or(Exists([_owner], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty], Implies(And(executedTransaction  ==  pendingTransactions[-1]), Or(Exists([_owner], True)))))), " :: ", solver__executeTransaction_02.check() == z3.sat)
            if solver__executeTransaction_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__executeTransaction_02.model() , "\n")
                
    return result
    

def _executeTransaction_1(minimize = False):
    global executedTransaction 
    # Declare variable before   
    _owner = String('_owner')
    _transaction = String('_transaction')
    
    
    #building the solver for the predancontion
    solver__executeTransaction_1 = z3.Solver() 
    solver__executeTransaction_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__executeTransaction_1.add(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(executedTransaction  ==  _transaction), Or(Exists([_owner], True)))))
    result = solver__executeTransaction_1.check() == z3.sat
    if minimize :
        print("--For _executeTransaction_1: ", simplify(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(executedTransaction  ==  _transaction), Or(Exists([_owner], True))))), " :: ", result)
        if not result: 
            solver__executeTransaction_12.add(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(executedTransaction  ==  _transaction), Or(Exists([_owner], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(executedTransaction  ==  _transaction), Or(Exists([_owner], True)))))), " :: ", solver__executeTransaction_12.check() == z3.sat)
            if solver__executeTransaction_12.check() == z3.sat :
                print("\nNot Formula Model: ",solver__executeTransaction_12.model() , "\n")
                
    return result
    



def _approveTransaction_0(minimize = False):
    global approvedOwners 
    # Declare variable before   
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__approveTransaction_0 = z3.Solver() 
    solver__approveTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__approveTransaction_0.add(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(approvedOwners  ==  approvedOwners), Or(len(approvedOwners) >= 2))))
    result = solver__approveTransaction_0.check() == z3.sat
    if minimize :
        print("--For _approveTransaction_0: ", simplify(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(approvedOwners  ==  approvedOwners), Or(len(approvedOwners) >= 2)))), " :: ", result)
        if not result: 
            solver__approveTransaction_02.add(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(approvedOwners  ==  approvedOwners), Or(len(approvedOwners) >= 2)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_owner], Implies(And(approvedOwners  ==  approvedOwners), Or(len(approvedOwners) >= 2))))), " :: ", solver__approveTransaction_02.check() == z3.sat)
            if solver__approveTransaction_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__approveTransaction_02.model() , "\n")
                
    return result
    



def _submitTransaction_0(minimize = False):
    global pendingTransactions 
    global approvedOwners 
    # Declare variable before   
    _owner = String('_owner')
    _transaction = String('_transaction')
    _transaction = String('_transaction')
    
    
    #building the solver for the predancontion
    solver__submitTransaction_0 = z3.Solver() 
    solver__submitTransaction_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__submitTransaction_0.add(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(pendingTransactions  ==  pendingTransactions,  approvedOwners  ==  empty), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= 2)))))
    result = solver__submitTransaction_0.check() == z3.sat
    if minimize :
        print("--For _submitTransaction_0: ", simplify(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(pendingTransactions  ==  pendingTransactions,  approvedOwners  ==  empty), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= 2))))), " :: ", result)
        if not result: 
            solver__submitTransaction_02.add(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(pendingTransactions  ==  pendingTransactions,  approvedOwners  ==  empty), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= 2))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([owners,pendingTransactions,approvedOwners,executedTransaction,empty,_transaction], Implies(And(pendingTransactions  ==  pendingTransactions,  approvedOwners  ==  empty), Or(Exists([_owner], _owner not in approvedOwners),Exists([_transaction], len(approvedOwners) >= 2)))))), " :: ", solver__submitTransaction_02.check() == z3.sat)
            if solver__submitTransaction_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__submitTransaction_02.model() , "\n")
                
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