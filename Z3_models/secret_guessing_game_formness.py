from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

secret = String('secret')
gameWon = Bool('gameWon')


role_Owner = Array('Owner',IntSort() , StringSort())
Store(role_Owner, 0, String('Owner'))
role_Guesser = Array('Guesser',IntSort() , StringSort())
Store(role_Guesser, 0, String('Guesser'))







def _initializeGame_0(infos = False):
    global secret 
    global gameWon 
    # Declare variable before   
    _guess = String('_guess')
    _guess = String('_guess')
    _secret = String('_secret')
    
    
    #building the solver for the predancontion
    solver__initializeGame_0 = z3.Solver() 
    solver__initializeGame_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__initializeGame_0.push()
    #solver__initializeGame_0.add(True)
    solver__initializeGame_0.add(And(True, ForAll([secret,gameWon,_secret], Implies(And(True, And(secret.eq(_secret), gameWon == False)), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret))))))))
    post_result = solver__initializeGame_0.check() == z3.sat
    
    solver__initializeGame_0.pop()
    solver__initializeGame_0.add(And(ForAll([_guess], Implies(And(Not(gameWon), Not(_guess.eq(secret))),And(Not(And(Not(gameWon), _guess.eq(secret)))))),ForAll([_guess], Implies(And(Not(gameWon), _guess.eq(secret)),And(Not(And(Not(gameWon), Not(_guess.eq(secret))))))))) 
    eps_result = solver__initializeGame_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _initializeGame_0: ", simplify(ForAll([secret,gameWon,_secret], Implies(And(True, And(secret.eq(_secret), gameWon == False)), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret))))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_guess], Implies(And(Not(gameWon), Not(_guess.eq(secret))),And(Not(And(Not(gameWon), _guess.eq(secret)))))),ForAll([_guess], Implies(And(Not(gameWon), _guess.eq(secret)),And(Not(And(Not(gameWon), Not(_guess.eq(secret))))))))))
            
        if not result: 
            solver__initializeGame_02.add(Not(ForAll([secret,gameWon,_secret], Implies(And(True, And(secret.eq(_secret), gameWon == False)), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret))))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([secret,gameWon,_secret], Implies(And(True, And(secret.eq(_secret), gameWon == False)), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret)))))))), " :: ", solver__initializeGame_02.check() == z3.sat)
            
          
                   
    return result
    



def _makeGuess_0(infos = False):
    
    # Declare variable before   
    _guess = String('_guess')
    _guess = String('_guess')
    _guess = String('_guess')
    
    
    #building the solver for the predancontion
    solver__makeGuess_0 = z3.Solver() 
    solver__makeGuess_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__makeGuess_0.push()
    #solver__makeGuess_0.add(True)
    solver__makeGuess_0.add(And(True, ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), Not(_guess.eq(secret))), True), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret))))))))
    post_result = solver__makeGuess_0.check() == z3.sat
    
    solver__makeGuess_0.pop()
    solver__makeGuess_0.add(And(ForAll([_guess], Implies(And(Not(gameWon), Not(_guess.eq(secret))),And(Not(And(Not(gameWon), _guess.eq(secret)))))),ForAll([_guess], Implies(And(Not(gameWon), _guess.eq(secret)),And(Not(And(Not(gameWon), Not(_guess.eq(secret))))))))) 
    eps_result = solver__makeGuess_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _makeGuess_0: ", simplify(ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), Not(_guess.eq(secret))), True), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret))))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_guess], Implies(And(Not(gameWon), Not(_guess.eq(secret))),And(Not(And(Not(gameWon), _guess.eq(secret)))))),ForAll([_guess], Implies(And(Not(gameWon), _guess.eq(secret)),And(Not(And(Not(gameWon), Not(_guess.eq(secret))))))))))
            
        if not result: 
            solver__makeGuess_02.add(Not(ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), Not(_guess.eq(secret))), True), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret))))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), Not(_guess.eq(secret))), True), Or(Exists([_guess], And(Not(gameWon), Not(_guess.eq(secret)))),Exists([_guess], And(Not(gameWon), _guess.eq(secret)))))))), " :: ", solver__makeGuess_02.check() == z3.sat)
            
          
                   
    return result
    

def _makeGuess_1(infos = False):
    global gameWon 
    # Declare variable before   
    _guess = String('_guess')
    
    
    #building the solver for the predancontion
    solver__makeGuess_1 = z3.Solver() 
    solver__makeGuess_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__makeGuess_1.push()
    #solver__makeGuess_1.add(True)
    solver__makeGuess_1.add(And(True, ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), _guess.eq(secret)), And(gameWon == True)), True))))
    post_result = solver__makeGuess_1.check() == z3.sat
    
    solver__makeGuess_1.pop()
    solver__makeGuess_1.add(True) 
    eps_result = solver__makeGuess_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _makeGuess_1: ", simplify(ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), _guess.eq(secret)), And(gameWon == True)), True))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__makeGuess_12.add(Not(ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), _guess.eq(secret)), And(gameWon == True)), True))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([secret,gameWon,_guess], Implies(And(And(Not(gameWon), _guess.eq(secret)), And(gameWon == True)), True)))), " :: ", solver__makeGuess_12.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_initializeGame_0() and _makeGuess_0() and _makeGuess_1())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_initializeGame_0(True)

_makeGuess_0(True)

_makeGuess_1(True)