from z3 import * 
from Z3.Extension import *

stage = Int('stage')
stage = 0
MaxHum = Int('MaxHum')
MinHum = Int('MinHum')
MaxTem = Int('MaxTem')
MinTem = Int('MinTem')
d = String('d')
hum = Int('hum')
tem = Int('tem')


role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))

def reset_deploy_vars():
    global stage
    stage = 0





check_resut = ()

if  check_resut == True:
    print("satisfy")
else:
    print("unSatisfy")
        
