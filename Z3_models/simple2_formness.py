from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

rbv = Int('rbv')


O_role = []
O_role.append('o')
B_role = []
B_role.append('b')



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
    
    solver__start_0.add(ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))
    post_result = solver__start_0.check() == z3.sat
    
    #check determinism
    solver__start_0.pop()
    solver__start_0.push()
    solver__start_0.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__start_0.check() == z3.sat

    #check participants
    solver__start_0.pop()
    solver__start_0.add( len(O_role) > 0 and 'b' in O_role) 
    part_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _start_0: ", simplify(ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "( len(O_role) > 0 and 'b' in O_role)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__start_02.add(Not(ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(True,True), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
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
    
    solver__check_color_0.add(ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))
    post_result = solver__check_color_0.check() == z3.sat
    
    #check determinism
    solver__check_color_0.pop()
    solver__check_color_0.push()
    solver__check_color_0.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__check_color_0.check() == z3.sat

    #check participants
    solver__check_color_0.pop()
    solver__check_color_0.add( len(B_role) > 0 and 'o' in B_role) 
    part_result = solver__check_color_0.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _check_color_0: ", simplify(ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "( len(B_role) > 0 and 'o' in B_role)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__check_color_02.add(Not(ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(And(_c > 0, _c < 100),And(rbv == 1)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", solver__check_color_02.check() == z3.sat)
            
          
                   
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
    
    solver__check_color_1.add(ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))
    post_result = solver__check_color_1.check() == z3.sat
    
    #check determinism
    solver__check_color_1.pop()
    solver__check_color_1.push()
    solver__check_color_1.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__check_color_1.check() == z3.sat

    #check participants
    solver__check_color_1.pop()
    solver__check_color_1.add( len(B_role) > 0 and 'o' in B_role) 
    part_result = solver__check_color_1.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _check_color_1: ", simplify(ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "( len(B_role) > 0 and 'o' in B_role)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__check_color_12.add(Not(ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(And(_c >= 100, _c < 180),And(rbv == 2)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", solver__check_color_12.check() == z3.sat)
            
          
                   
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
    
    solver__check_color_2.add(ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))
    post_result = solver__check_color_2.check() == z3.sat
    
    #check determinism
    solver__check_color_2.pop()
    solver__check_color_2.push()
    solver__check_color_2.add(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))) 
    eps_result = solver__check_color_2.check() == z3.sat

    #check participants
    solver__check_color_2.pop()
    solver__check_color_2.add( len(B_role) > 0 and 'o' in B_role) 
    part_result = solver__check_color_2.check() == z3.sat
    
    result = post_result and eps_result and part_result
    
    if infos :
        print()
        if not result:
            print("--For _check_color_2: ", simplify(ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))), " :: ", result)

        if not part_result :
            print(f"--- Participants       : {part_result}", "( len(B_role) > 0 and 'o' in B_role)")

        if  not eps_result :
            print ("--- Non Determinism  : ", simplify(And(ForAll([_c], Implies(And(_c > 0, _c < 100), And(Not(And(_c >= 100, _c < 180)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 100, _c < 180), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 180, _c < 255))))),ForAll([_c], Implies(And(_c >= 180, _c < 255), And(Not(And(_c > 0, _c < 100)) , Not(And(_c >= 100, _c < 180))))))))
            
        if not post_result: 
            print(f"--- Sat of o Prec-Conds: {post_result}")
            solver__check_color_22.add(Not(ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(ForAll([rbv,_c], Implies(And(And(_c >= 180, _c < 255),And(rbv == 3)), Or(Exists([_c], And(_c > 0, _c < 100)),Exists([_c], And(_c >= 100, _c < 180)),Exists([_c], And(_c >= 180, _c < 255))))))), " :: ", solver__check_color_22.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _check_color_0() and _check_color_1() and _check_color_2())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
if not check_resut: 
    print('\nFunctions simplified formula and satisfiability results :')
    _start_0(True)
    _check_color_0(True)
    _check_color_1(True)
    _check_color_2(True)