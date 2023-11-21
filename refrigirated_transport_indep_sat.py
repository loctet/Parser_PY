from z3 import * 
from Z3.Extension import *

stage = Int('stage')
MaxHum = Int('MaxHum')
MinHum = Int('MinHum')
MaxTem = Int('MaxTem')
MinTem = Int('MinTem')
d = String('d')
cp = String('cp')
hum = Int('hum')
tem = Int('tem')


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))



def _start_0(minimize = False):
    global d 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _d = String('_d')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver() 
    solver__start_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__start_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(d  ==  _d), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2))))))
    result = solver__start_0.check() == z3.sat
    if minimize :
        print("--For _start_0: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(d  ==  _d), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2)))))), " :: ", result)
        if not result: 
            solver__start_02.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(d  ==  _d), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2)))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(d  ==  _d), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2))))))), " :: ", solver__start_02.check() == z3.sat)
            if solver__start_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__start_02.model() , "\n")
                
    return result
    





def _ingestTel_0(minimize = False):
    global tem 
    global hum 
    global stage 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_0 = z3.Solver() 
    solver__ingestTel_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  hum  ==  _hum ,  stage  ==  1), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2))))))
    result = solver__ingestTel_0.check() == z3.sat
    if minimize :
        print("--For _ingestTel_0: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  hum  ==  _hum ,  stage  ==  1), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2)))))), " :: ", result)
        if not result: 
            solver__ingestTel_02.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  hum  ==  _hum ,  stage  ==  1), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2)))))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  hum  ==  _hum ,  stage  ==  1), Or(Exists([_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_cp], Or(stage == 0, stage == 1, stage == 2))))))), " :: ", solver__ingestTel_02.check() == z3.sat)
            if solver__ingestTel_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__ingestTel_02.model() , "\n")
                
    return result
    

def _ingestTel_1(minimize = False):
    global hum 
    global tem 
    global stage 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_1 = z3.Solver() 
    solver__ingestTel_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_1.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(hum  ==  _hum ,  tem  ==  _tem ,  stage  ==  3), True)))
    result = solver__ingestTel_1.check() == z3.sat
    if minimize :
        print("--For _ingestTel_1: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(hum  ==  _hum ,  tem  ==  _tem ,  stage  ==  3), True))), " :: ", result)
        if not result: 
            solver__ingestTel_12.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(hum  ==  _hum ,  tem  ==  _tem ,  stage  ==  3), True))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(hum  ==  _hum ,  tem  ==  _tem ,  stage  ==  3), True)))), " :: ", solver__ingestTel_12.check() == z3.sat)
            if solver__ingestTel_12.check() == z3.sat :
                print("\nNot Formula Model: ",solver__ingestTel_12.model() , "\n")
                
    return result
    



def _transResp_0(minimize = False):
    global stage 
    global cp 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    
    
    #building the solver for the predancontion
    solver__transResp_0 = z3.Solver() 
    solver__transResp_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__transResp_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(stage  ==  1 ,  cp  ==  _cp), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2))))
    result = solver__transResp_0.check() == z3.sat
    if minimize :
        print("--For _transResp_0: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(stage  ==  1 ,  cp  ==  _cp), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2)))), " :: ", result)
        if not result: 
            solver__transResp_02.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(stage  ==  1 ,  cp  ==  _cp), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(stage  ==  1 ,  cp  ==  _cp), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2))))), " :: ", solver__transResp_02.check() == z3.sat)
            if solver__transResp_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__transResp_02.model() , "\n")
                
    return result
    



def _ingestTel_b_1_0(minimize = False):
    global tem 
    global stage 
    global hum 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_b_1_0 = z3.Solver() 
    solver__ingestTel_b_1_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_b_1_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  2 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2))))
    result = solver__ingestTel_b_1_0.check() == z3.sat
    if minimize :
        print("--For _ingestTel_b_1_0: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  2 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2)))), " :: ", result)
        if not result: 
            solver__ingestTel_b_1_02.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  2 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  2 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2))))), " :: ", solver__ingestTel_b_1_02.check() == z3.sat)
            if solver__ingestTel_b_1_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__ingestTel_b_1_02.model() , "\n")
                
    return result
    



def _ingestTel_b_2_0(minimize = False):
    global tem 
    global stage 
    global hum 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_b_2_0 = z3.Solver() 
    solver__ingestTel_b_2_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_b_2_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  3 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2))))
    result = solver__ingestTel_b_2_0.check() == z3.sat
    if minimize :
        print("--For _ingestTel_b_2_0: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  3 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2)))), " :: ", result)
        if not result: 
            solver__ingestTel_b_2_02.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  3 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2)))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(tem  ==  _tem ,  stage  ==  3 ,  hum  ==  _hum), Or(Exists([_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),stage == 2))))), " :: ", solver__ingestTel_b_2_02.check() == z3.sat)
            if solver__ingestTel_b_2_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__ingestTel_b_2_02.model() , "\n")
                
    return result
    



def _complete_0(minimize = False):
    global stage 
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__complete_0 = z3.Solver() 
    solver__complete_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__complete_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(stage  ==  3), True)))
    result = solver__complete_0.check() == z3.sat
    if minimize :
        print("--For _complete_0: ", simplify(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(stage  ==  3), True))), " :: ", result)
        if not result: 
            solver__complete_02.add(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(stage  ==  3), True))))
            print("\nMinify of the Not Formula: ", simplify(Not(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(stage  ==  3), True)))), " :: ", solver__complete_02.check() == z3.sat)
            if solver__complete_02.check() == z3.sat :
                print("\nNot Formula Model: ",solver__complete_02.model() , "\n")
                
    return result
    
check_resut = (_start_0() and _ingestTel_0() and _ingestTel_1() and _transResp_0() and _ingestTel_b_1_0() and _ingestTel_b_2_0() and _complete_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_ingestTel_0(True)

_ingestTel_1(True)

_transResp_0(True)

_ingestTel_b_1_0(True)

_ingestTel_b_2_0(True)

_complete_0(True)