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

_hum = Int('_hum')
_tem = Int('_tem')
_hum = Int('_hum')
_tem = Int('_tem')
_cp = String('_cp')
_d = String('_d')

d =  _d


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))

def reset_deploy_vars():
    1 == 1
    global stage, MaxHum, MinHum, MaxTem, MinTem, d, cp, hum, tem
    global stage , MaxHum , MinHum , MaxTem , MinTem , d , cp , hum , tem 
    stage = Int('stage')
    MaxHum = Int('MaxHum')
    MinHum = Int('MinHum')
    MaxTem = Int('MaxTem')
    MinTem = Int('MinTem')
    d = String('d')
    cp = String('cp')
    hum = Int('hum')
    tem = Int('tem')
    




def _start_0(reset = False):
    global d 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _d = String('_d')
    
    
    #building the solver for the predancontion
    solver__start_0 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__start_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d], And(d  ==  _d)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp], Or(stage == 0, stage == 1, stage == 2))))))
    return solver__start_0.check() == z3.sat
    





def _ingestTel_b_1_0(reset = False):
    global tem 
    global stage 
    global hum 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_b_1_0 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__ingestTel_b_1_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem], And(tem  ==  _tem ,  stage  ==  2 ,  hum  ==  _hum)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], stage == 2)))))
    return solver__ingestTel_b_1_0.check() == z3.sat
    



def _ingestTel_b_2_0(reset = False):
    global tem 
    global stage 
    global hum 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_b_2_0 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__ingestTel_b_2_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], And(tem  ==  _tem ,  stage  ==  3 ,  hum  ==  _hum)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], stage == 2)))))
    return solver__ingestTel_b_2_0.check() == z3.sat
    



def _complete_0(reset = False):
    global stage 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    
    
    #building the solver for the predancontion
    solver__complete_0 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__complete_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], And(stage  ==  3)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem], True)))))
    return solver__complete_0.check() == z3.sat
    



def _ingestTel_0(reset = False):
    global tem 
    global hum 
    global stage 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_0 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__ingestTel_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem], And(tem  ==  _tem ,  hum  ==  _hum ,  stage  ==  1)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem], And(d != cp, stage == 0)),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem], And(stage == 0, Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp], Or(stage == 0, stage == 1, stage == 2))))))
    return solver__ingestTel_0.check() == z3.sat
    

def _ingestTel_1(reset = False):
    global hum 
    global tem 
    global stage 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_1 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__ingestTel_1.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem], And(hum  ==  _hum ,  tem  ==  _tem ,  stage  ==  3)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem], True)))))
    return solver__ingestTel_1.check() == z3.sat
    



def _transResp_0(reset = False):
    global stage 
    global cp 
    #reset global var to execute functions independenly
    if reset:
        reset_deploy_vars()
    # Declare variable before checking the precondition    
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    
    
    #building the solver for the predancontion
    solver__transResp_0 = z3.Solver()
    
    
    #check if post condition implies any pre precondition
    
    solver__transResp_0.add(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp], And(stage  ==  1 ,  cp  ==  _cp)), Or(Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem], And(Or(stage == 1, stage == 2), And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_hum,_tem,_hum,_tem,_cp,_d,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem,_hum,_tem,_hum,_tem,_cp,_hum,_tem,_hum,_tem], stage == 2)))))
    return solver__transResp_0.check() == z3.sat
    
check_resut = (_start_0(True) and _ingestTel_b_1_0(True) and _ingestTel_b_2_0(True) and _complete_0(True) and _ingestTel_0(True) and _ingestTel_1(True) and _transResp_0(True))

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        


print('_start_0: ',_start_0(True))

print('_ingestTel_b_1_0: ',_ingestTel_b_1_0(True))

print('_ingestTel_b_2_0: ',_ingestTel_b_2_0(True))

print('_complete_0: ',_complete_0(True))

print('_ingestTel_0: ',_ingestTel_0(True))

print('_ingestTel_1: ',_ingestTel_1(True))

print('_transResp_0: ',_transResp_0(True))