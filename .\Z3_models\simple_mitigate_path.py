from z3 import *
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *


solver = z3.Solver()
check = True
solver.push()


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## action2

solver.add(False)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## action3

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()


print(f'=>{check}')


