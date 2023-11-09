from z3 import * 
from Z3.Extension import *

price = Int('price')
state = Bool('state')
state =  False
M = []
M =  [1,2,3,4,5]
x = Int('x')
x = 0

solver = z3.Solver()
check = True
solver.push()


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

_p = Int('_p')


## makeoffer

solver.add(And(state == False, _p >0))
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "price")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    price  =  _p
    solver.add(price  == price )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## rejectoffer

solver.add(state == False)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "state")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    state  =  True
    solver.add(state  == state )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


