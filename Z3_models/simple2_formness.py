from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

rbv = Int('rbv')


O_role = []
O_role.append('o')
O_role.append('b')
B_role = []
B_role.append('b')
B_role.append('o')



def _start_0(infos = False):
    
    # Declare variable before   
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.push()
    #solver__start_0.add(True)
    solver__start_0.add(And('O' in ['O'], ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
    post_result = solver__start_0.check() == z3.sat
    #print((And('O' in ['O'], ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(And('O' in ['O'], ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not result: 
            solver__start_02.add(Not(And('O' in ['O'], ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And('O' in ['O'], ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _check_color_0(infos = False):
    global rbv 
    # Declare variable before   
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    
    
    #building the solver for the predancontion
    solver__check_color_0 = z3.Solver() 
    solver__check_color_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__check_color_0.push()
    #solver__check_color_0.add(And(_c > 0, _c < 100))
    solver__check_color_0.add(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
    post_result = solver__check_color_0.check() == z3.sat
    #print((And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), post_result)
    
    solver__check_color_0.pop()
    solver__check_color_0.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__check_color_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _check_color_0: ", simplify(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not result: 
            solver__check_color_02.add(Not(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))), " :: ", solver__check_color_02.check() == z3.sat)
            
          
                   
    return result
    

def _check_color_1(infos = False):
    global rbv 
    # Declare variable before   
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    
    
    #building the solver for the predancontion
    solver__check_color_1 = z3.Solver() 
    solver__check_color_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__check_color_1.push()
    #solver__check_color_1.add(And(_c >= 100, _c < 180))
    solver__check_color_1.add(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
    post_result = solver__check_color_1.check() == z3.sat
    #print((And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), post_result)
    
    solver__check_color_1.pop()
    solver__check_color_1.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__check_color_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _check_color_1: ", simplify(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not result: 
            solver__check_color_12.add(Not(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))), " :: ", solver__check_color_12.check() == z3.sat)
            
          
                   
    return result
    

def _check_color_2(infos = False):
    global rbv 
    # Declare variable before   
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    _c = Int('_c')
    
    
    #building the solver for the predancontion
    solver__check_color_2 = z3.Solver() 
    solver__check_color_22 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__check_color_2.push()
    #solver__check_color_2.add(And(_c >= 180, _c < 255))
    solver__check_color_2.add(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
    post_result = solver__check_color_2.check() == z3.sat
    #print((And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), post_result)
    
    solver__check_color_2.pop()
    solver__check_color_2.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__check_color_2.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _check_color_2: ", simplify(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not result: 
            solver__check_color_22.add(Not(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And('B' in ['B'], ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))), " :: ", solver__check_color_22.check() == z3.sat)
            
          
                   
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