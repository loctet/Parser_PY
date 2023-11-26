from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

currentStage = Int('currentStage')
currentNumber = Int('currentNumber')


role_Counter = Array('Counter',IntSort() , StringSort())
Store(role_Counter, 0, String('Counter'))







def _initializeCounter_0(minimize = False):
    global currentNumber 
    # Declare variable before   
    _old = Int('_old')
    
    
    #building the solver for the predancontion
    solver__initializeCounter_0 = z3.Solver() 
    solver__initializeCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__initializeCounter_0.add(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True)))))
    result = solver__initializeCounter_0.check() == z3.sat
    if minimize :
        print("--For _initializeCounter_0: ", simplify(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True))))), " :: ", result)
        if not result: 
            solver__initializeCounter_02.add(Not(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True)))))), " :: ", solver__initializeCounter_02.check() == z3.sat)
            if solver__initializeCounter_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__initializeCounter_02.model() , "\n")
                
    return result
    



def _resetCounter_0(minimize = False):
    global currentNumber 
    # Declare variable before   
    _old = Int('_old')
    
    
    #building the solver for the predancontion
    solver__resetCounter_0 = z3.Solver() 
    solver__resetCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__resetCounter_0.add(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True)))))
    result = solver__resetCounter_0.check() == z3.sat
    if minimize :
        print("--For _resetCounter_0: ", simplify(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True))))), " :: ", result)
        if not result: 
            solver__resetCounter_02.add(Not(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentStage,currentNumber], Implies(And(currentNumber  ==  0), Or(Exists([_old], True)))))), " :: ", solver__resetCounter_02.check() == z3.sat)
            if solver__resetCounter_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__resetCounter_02.model() , "\n")
                
    return result
    



def _finalizeCounter_0(minimize = False):
    global currentNumber 
    # Declare variable before   
    _old = Int('_old')
    
    
    #building the solver for the predancontion
    solver__finalizeCounter_0 = z3.Solver() 
    solver__finalizeCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__finalizeCounter_0.add(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(True))))
    result = solver__finalizeCounter_0.check() == z3.sat
    if minimize :
        print("--For _finalizeCounter_0: ", simplify(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(True)))), " :: ", result)
        if not result: 
            solver__finalizeCounter_02.add(Not(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(True)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(True))))), " :: ", solver__finalizeCounter_02.check() == z3.sat)
            if solver__finalizeCounter_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__finalizeCounter_02.model() , "\n")
                
    return result
    



def _incrementCounter_0(minimize = False):
    global currentNumber 
    # Declare variable before   
    _old = Int('_old')
    _old = Int('_old')
    
    
    #building the solver for the predancontion
    solver__incrementCounter_0 = z3.Solver() 
    solver__incrementCounter_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__incrementCounter_0.add(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(Exists([_old], True)))))
    result = solver__incrementCounter_0.check() == z3.sat
    if minimize :
        print("--For _incrementCounter_0: ", simplify(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(Exists([_old], True))))), " :: ", result)
        if not result: 
            solver__incrementCounter_02.add(Not(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(Exists([_old], True))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([currentStage,currentNumber,_old], Implies(And(currentNumber  ==  _old + 1), Or(Exists([_old], True)))))), " :: ", solver__incrementCounter_02.check() == z3.sat)
            if solver__incrementCounter_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__incrementCounter_02.model() , "\n")
                
    return result
    
check_resut = (_initializeCounter_0() and _resetCounter_0() and _finalizeCounter_0() and _incrementCounter_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_initializeCounter_0(True)

_resetCounter_0(True)

_finalizeCounter_0(True)

_incrementCounter_0(True)