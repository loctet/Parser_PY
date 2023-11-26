from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

currentOwner = String('currentOwner')
previousOwner = String('previousOwner')
Counterparty = String('Counterparty')
owner = String('owner')


role_InitiatingCounterParty = Array('InitiatingCounterParty',IntSort() , StringSort())
Store(role_InitiatingCounterParty, 0, String('InitiatingCounterParty'))
role_Counterparty = Array('Counterparty',IntSort() , StringSort())
Store(role_Counterparty, 0, String('Counterparty'))
role_Owner = Array('Owner',IntSort() , StringSort())
Store(role_Owner, 0, String('Owner'))
role_Observer = Array('Observer',IntSort() , StringSort())
Store(role_Observer, 0, String('Observer'))



def _start_0(minimize = False):
    global currentOwner 
    global owner 
    # Declare variable before   
    _counterparty = String('_counterparty')
    _currentOwner = String('_currentOwner')
    _owner = String('_owner')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.add(ForAll([currentOwner,previousOwner,Counterparty,owner,_currentOwner,_owner], Implies(And(currentOwner  ==  _currentOwner ,  owner  ==  _owner), Or(Exists([_counterparty], True)))))
    result = solver__start_0.check() == z3.sat
    if minimize :
        print("--For _start_0: ", simplify(ForAll([currentOwner,previousOwner,Counterparty,owner,_currentOwner,_owner], Implies(And(currentOwner  ==  _currentOwner ,  owner  ==  _owner), Or(Exists([_counterparty], True))))), " :: ", result)
        if not result: 
            solver__start_02.add(Not(ForAll([currentOwner,previousOwner,Counterparty,owner,_currentOwner,_owner], Implies(And(currentOwner  ==  _currentOwner ,  owner  ==  _owner), Or(Exists([_counterparty], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentOwner,previousOwner,Counterparty,owner,_currentOwner,_owner], Implies(And(currentOwner  ==  _currentOwner ,  owner  ==  _owner), Or(Exists([_counterparty], True)))))), " :: ", solver__start_02.check() == z3.sat)
            if solver__start_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__start_02.model() , "\n")
                
    return result
    





def _assignResponsibility_0(minimize = False):
    global currentOwner 
    global previousOwner 
    # Declare variable before   
    _counterparty = String('_counterparty')
    _counterparty = String('_counterparty')
    
    
    #building the solver for the predancontion
    solver__assignResponsibility_0 = z3.Solver() 
    solver__assignResponsibility_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__assignResponsibility_0.add(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner))))
    result = solver__assignResponsibility_0.check() == z3.sat
    if minimize :
        print("--For _assignResponsibility_0: ", simplify(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner)))), " :: ", result)
        if not result: 
            solver__assignResponsibility_02.add(Not(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner))))), " :: ", solver__assignResponsibility_02.check() == z3.sat)
            if solver__assignResponsibility_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__assignResponsibility_02.model() , "\n")
                
    return result
    

def _assignResponsibility_1(minimize = False):
    global currentOwner 
    global previousOwner 
    # Declare variable before   
    _counterparty = String('_counterparty')
    _counterparty = String('_counterparty')
    
    
    #building the solver for the predancontion
    solver__assignResponsibility_1 = z3.Solver() 
    solver__assignResponsibility_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__assignResponsibility_1.add(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner))))
    result = solver__assignResponsibility_1.check() == z3.sat
    if minimize :
        print("--For _assignResponsibility_1: ", simplify(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner)))), " :: ", result)
        if not result: 
            solver__assignResponsibility_12.add(Not(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentOwner,previousOwner,Counterparty,owner,_counterparty], Implies(And(currentOwner  ==  _counterparty ,  previousOwner  ==  currentOwner), Or(Exists([_counterparty], And(currentOwner == _counterparty, currentOwner != owner)),currentOwner == owner))))), " :: ", solver__assignResponsibility_12.check() == z3.sat)
            if solver__assignResponsibility_12.check() == z3.sat :
                print("\nNot Formula Model: ",solver__assignResponsibility_12.model() , "\n")
                
    return result
    



def _reachDestination_0(minimize = False):
    global previousOwner 
    global currentOwner 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__reachDestination_0 = z3.Solver() 
    solver__reachDestination_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__reachDestination_0.add(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(And(previousOwner  ==  currentOwner ,  currentOwner  ==  owner), True)))
    result = solver__reachDestination_0.check() == z3.sat
    if minimize :
        print("--For _reachDestination_0: ", simplify(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(And(previousOwner  ==  currentOwner ,  currentOwner  ==  owner), True))), " :: ", result)
        if not result: 
            solver__reachDestination_02.add(Not(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(And(previousOwner  ==  currentOwner ,  currentOwner  ==  owner), True))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentOwner,previousOwner,Counterparty,owner], Implies(And(previousOwner  ==  currentOwner ,  currentOwner  ==  owner), True)))), " :: ", solver__reachDestination_02.check() == z3.sat)
            if solver__reachDestination_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__reachDestination_02.model() , "\n")
                
    return result
    
check_resut = (_start_0() and _assignResponsibility_0() and _assignResponsibility_1() and _reachDestination_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_assignResponsibility_0(True)

_assignResponsibility_1(True)

_reachDestination_0(True)