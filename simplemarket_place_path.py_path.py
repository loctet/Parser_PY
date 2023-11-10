from z3 import * 
from Z3.Extension import *

state = Int('state')
state = 0
price = Int('price')
price = 0
B = []
B =  []

solver = z3.Solver()
check = True
solver.push()
_price = Int('_price')


## start

solver.add(_price > 0)
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
    price  =  _price
    solver.add(price  == price )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_price = Int('_price')


## makeOffer

solver.add(And(Or(state == 0, state == 1), _price >= price))
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
    price  =  _price
    solver.add(price  == price )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "state")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    state  =  1
    solver.add(state  == state )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## rejectOffer

solver.add(state == 1)
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
    state  =  0
    solver.add(state  == state )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


