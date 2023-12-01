from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

rbv = Int('rbv')
_c = Int('_c')


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))



def _start_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    #solver__start_0.add(True)
    solver__start_0.add(ForAll([rbv,_c], Implies(True, Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))
    post_result = solver__start_0.check() == z3.sat
    #print((ForAll([rbv,_c], Implies(True, Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(True) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(ForAll([rbv,_c], Implies(True, Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__start_02.add(Not(ForAll([rbv,_c], Implies(True, Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(True, Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _check_color_0(infos = False):
    global rbv 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__check_color_0 = z3.Solver() 
    solver__check_color_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__check_color_0.push()
    #solver__check_color_0.add(And(_c > 0, _c < 100))
    solver__check_color_0.add(ForAll([rbv,_c], Implies(And(rbv == 1), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))
    post_result = solver__check_color_0.check() == z3.sat
    #print((ForAll([rbv,_c], Implies(And(rbv == 1), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), post_result)
    
    solver__check_color_0.pop()
    solver__check_color_0.add(True) 
    eps_result = solver__check_color_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _check_color_0: ", simplify(ForAll([rbv,_c], Implies(And(rbv == 1), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__check_color_02.add(Not(ForAll([rbv,_c], Implies(And(rbv == 1), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(rbv == 1), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))), " :: ", solver__check_color_02.check() == z3.sat)
            
          
                   
    return result
    

def _check_color_1(infos = False):
    global rbv 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__check_color_1 = z3.Solver() 
    solver__check_color_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__check_color_1.push()
    #solver__check_color_1.add(And(_c >= 100, _c < 180))
    solver__check_color_1.add(ForAll([rbv,_c], Implies(And(rbv == 2), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))
    post_result = solver__check_color_1.check() == z3.sat
    #print((ForAll([rbv,_c], Implies(And(rbv == 2), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), post_result)
    
    solver__check_color_1.pop()
    solver__check_color_1.add(True) 
    eps_result = solver__check_color_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _check_color_1: ", simplify(ForAll([rbv,_c], Implies(And(rbv == 2), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__check_color_12.add(Not(ForAll([rbv,_c], Implies(And(rbv == 2), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(rbv == 2), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))), " :: ", solver__check_color_12.check() == z3.sat)
            
          
                   
    return result
    

def _check_color_2(infos = False):
    global rbv 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__check_color_2 = z3.Solver() 
    solver__check_color_22 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__check_color_2.push()
    #solver__check_color_2.add(And(_c >= 180, _c < 255))
    solver__check_color_2.add(ForAll([rbv,_c], Implies(And(rbv == 3), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))
    post_result = solver__check_color_2.check() == z3.sat
    #print((ForAll([rbv,_c], Implies(And(rbv == 3), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), post_result)
    
    solver__check_color_2.pop()
    solver__check_color_2.add(True) 
    eps_result = solver__check_color_2.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _check_color_2: ", simplify(ForAll([rbv,_c], Implies(And(rbv == 3), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__check_color_22.add(Not(ForAll([rbv,_c], Implies(And(rbv == 3), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(rbv == 3), Or(And(_c > 0, _c < 100),And(_c >= 100, _c < 180),And(_c >= 180, _c < 255)))))), " :: ", solver__check_color_22.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _check_color_0() and _check_color_1() and _check_color_2())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_check_color_0(True)

_check_color_1(True)

_check_color_2(True)