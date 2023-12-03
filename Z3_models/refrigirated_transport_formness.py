from z3 import * 
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

stage = Int('stage')
MaxHum = Int('MaxHum')
MinHum = Int('MinHum')
MaxTem = Int('MaxTem')
MinTem = Int('MinTem')
d = String('d')
cp = String('cp')
hum = Int('hum')
tem = Int('tem')


O_role = []
O_role.append('o')
B_role = []
B_role.append('b')
D_role = []
D_role.append('d')
CP_role = []
CP_role.append('cp')



def _start_0(infos = False):
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
    solver__start_0.push()
    #solver__start_0.add(True)
    solver__start_0.add(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(True,And(d.eq(_d))), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True))))))
    post_result = solver__start_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(True,And(d.eq(_d))), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True)))))), post_result)
    
    solver__start_0.pop()
    solver__start_0.add(And(ForAll([_hum,_tem], Implies(d != cp, And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(d != cp)))))) 
    eps_result = solver__start_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _start_0: ", simplify(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(True,And(d.eq(_d))), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_hum,_tem], Implies(d != cp, And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(d != cp)))))))
            
        if not result: 
            solver__start_02.add(Not(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(True,And(d.eq(_d))), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_d], Implies(And(True,And(d.eq(_d))), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True))))))), " :: ", solver__start_02.check() == z3.sat)
            
          
                   
    return result
    





def _ingestTel_0(infos = False):
    global tem 
    global hum 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_0 = z3.Solver() 
    solver__ingestTel_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_0.push()
    #solver__ingestTel_0.add(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))
    solver__ingestTel_0.add(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True)))))
    post_result = solver__ingestTel_0.check() == z3.sat
    #print((And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))), post_result)
    
    solver__ingestTel_0.pop()
    solver__ingestTel_0.add(And(ForAll([_hum,_tem], Implies(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem), And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))))) 
    eps_result = solver__ingestTel_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _ingestTel_0: ", simplify(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_hum,_tem], Implies(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem), And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))))))
            
        if not result: 
            solver__ingestTel_02.add(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True)))))), " :: ", solver__ingestTel_02.check() == z3.sat)
            
          
                   
    return result
    

def _ingestTel_1(infos = False):
    global tem 
    global hum 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_1 = z3.Solver() 
    solver__ingestTel_12 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_1.push()
    #solver__ingestTel_1.add(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))
    solver__ingestTel_1.add(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True)))))
    post_result = solver__ingestTel_1.check() == z3.sat
    #print((And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))), post_result)
    
    solver__ingestTel_1.pop()
    solver__ingestTel_1.add(And(ForAll([_hum,_tem], Implies(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem), And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))))) 
    eps_result = solver__ingestTel_1.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _ingestTel_1: ", simplify(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_hum,_tem], Implies(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem), And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))))))
            
        if not result: 
            solver__ingestTel_12.add(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True)))))), " :: ", solver__ingestTel_12.check() == z3.sat)
            
          
                   
    return result
    

def _ingestTel_2(infos = False):
    global tem 
    global hum 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    _hum = Int('_hum')
    _tem = Int('_tem')
    _cp = String('_cp')
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_2 = z3.Solver() 
    solver__ingestTel_22 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_2.push()
    #solver__ingestTel_2.add(d != cp)
    solver__ingestTel_2.add(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(d != cp,And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True))))))
    post_result = solver__ingestTel_2.check() == z3.sat
    #print((And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(d != cp,And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True)))))), post_result)
    
    solver__ingestTel_2.pop()
    solver__ingestTel_2.add(And(ForAll([_hum,_tem], Implies(d != cp, And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(d != cp)))))) 
    eps_result = solver__ingestTel_2.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _ingestTel_2: ", simplify(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(d != cp,And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True)))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_hum,_tem], Implies(d != cp, And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(d != cp)))))))
            
        if not result: 
            solver__ingestTel_22.add(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(d != cp,And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True)))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(d != cp,And(tem == _tem, hum == _hum)), Or(Exists([_hum,_tem], d != cp),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),Exists([_cp], True))))))), " :: ", solver__ingestTel_22.check() == z3.sat)
            
          
                   
    return result
    

def _ingestTel_3(infos = False):
    global hum 
    global tem 
    # Declare variable before   
    _hum = Int('_hum')
    _tem = Int('_tem')
    
    
    #building the solver for the predancontion
    solver__ingestTel_3 = z3.Solver() 
    solver__ingestTel_32 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__ingestTel_3.push()
    #solver__ingestTel_3.add(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))
    solver__ingestTel_3.add(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(hum == _hum, tem == _tem)), True))))
    post_result = solver__ingestTel_3.check() == z3.sat
    #print((And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(hum == _hum, tem == _tem)), True)))), post_result)
    
    solver__ingestTel_3.pop()
    solver__ingestTel_3.add(True) 
    eps_result = solver__ingestTel_3.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _ingestTel_3: ", simplify(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(hum == _hum, tem == _tem)), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__ingestTel_32.add(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(hum == _hum, tem == _tem)), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('d' in D_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_hum,_tem], Implies(And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),And(hum == _hum, tem == _tem)), True))))), " :: ", solver__ingestTel_32.check() == z3.sat)
            
          
                   
    return result
    



def _complete_0(infos = False):
    
    # Declare variable before   
    
    
    #building the solver for the predancontion
    solver__complete_0 = z3.Solver() 
    solver__complete_02 = z3.Solver() 
    #check if post condition implies any pre precondition
    solver__complete_0.push()
    #solver__complete_0.add(True)
    solver__complete_0.add(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(True,True), True))))
    post_result = solver__complete_0.check() == z3.sat
    #print((And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(True,True), True)))), post_result)
    
    solver__complete_0.pop()
    solver__complete_0.add(True) 
    eps_result = solver__complete_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _complete_0: ", simplify(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(True,True), True)))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(True))
            
        if not result: 
            solver__complete_02.add(Not(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(True,True), True)))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('o' in O_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem], Implies(And(True,True), True))))), " :: ", solver__complete_02.check() == z3.sat)
            
          
                   
    return result
    



def _transResp_0(infos = False):
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
    solver__transResp_0.push()
    #solver__transResp_0.add(True)
    solver__transResp_0.add(And(Or('cp' in CP_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(True,And(cp.eq(_cp))), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True)))))
    post_result = solver__transResp_0.check() == z3.sat
    #print((And(Or('cp' in CP_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(True,And(cp.eq(_cp))), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))), post_result)
    
    solver__transResp_0.pop()
    solver__transResp_0.add(And(ForAll([_hum,_tem], Implies(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem), And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))))) 
    eps_result = solver__transResp_0.check() == z3.sat
    
    result = post_result and eps_result
    
    if infos :
        print("--For _transResp_0: ", simplify(And(Or('cp' in CP_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(True,And(cp.eq(_cp))), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))), " :: ", result)

        if  not eps_result :
            print ("Non deterministic: ", simplify(And(ForAll([_hum,_tem], Implies(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem), And(Not(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)))))),ForAll([_hum,_tem], Implies(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)), And(Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))))))))
            
        if not result: 
            solver__transResp_02.add(Not(And(Or('cp' in CP_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(True,And(cp.eq(_cp))), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True))))))
            print("\nSimplify of the Not Formula: ", simplify(Not(And(Or('cp' in CP_role), ForAll([stage,MaxHum,MinHum,MaxTem,MinTem,d,cp,hum,tem,_cp], Implies(And(True,And(cp.eq(_cp))), Or(Exists([_hum,_tem], And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem)),Exists([_hum,_tem], Not(And(_hum <= MaxHum, _hum >= MinHum, _tem <= MaxTem, _tem >= MinTem))),True)))))), " :: ", solver__transResp_02.check() == z3.sat)
            
          
                   
    return result
    
check_resut = (_start_0() and _ingestTel_0() and _ingestTel_1() and _ingestTel_2() and _ingestTel_3() and _complete_0() and _transResp_0())

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
print('\nFuntions minimized formula and satisfiability result :')

_start_0(True)

_ingestTel_0(True)

_ingestTel_1(True)

_ingestTel_2(True)

_ingestTel_3(True)

_complete_0(True)

_transResp_0(True)