from z3 import * 
from Z3.Extension import *

state = Int('state')
offer = Int('offer')
B = Array('B', IntSort(), IntSort())

solver = z3.Solver()
check = True
solver.push()


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

_offer = Int('_offer')


## makeOffer

solver.add(_offer  > 0)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "offer")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    offer   =  _offer
    _tmp_ =  _offer
    solver.add(offer   == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## acceptOffer

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()


print(f'=>{check}')


