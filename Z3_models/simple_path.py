from z3 import *
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

x = Int('x')
y = Int('y')

solver = z3.Solver()
check = True
solver.push()


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## action1

solver.add(x<=9)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "y")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    y = 0
    _tmp_ = 0
    solver.add(y == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## action2

solver.add(x<=10)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()


print(f'=>{check}')


