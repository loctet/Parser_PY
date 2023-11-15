from z3 import * 
from Z3.Extension import *

currentOwner = String('currentOwner')
previousOwner = String('previousOwner')
Counterparty = String('Counterparty')
owner = String('owner')

solver = z3.Solver()
check = True
solver.push()
_currentOwner = String('_currentOwner')


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentOwner")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentOwner  =  _currentOwner
    solver.add(currentOwner  == currentOwner )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_counterparty = String('_counterparty')


## assignResponsibility

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentOwner")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentOwner  =  _counterparty
    solver.add(currentOwner  == currentOwner )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "previousOwner")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    previousOwner  =  currentOwner
    solver.add(previousOwner  == previousOwner )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## reachDestination

solver.add(currentOwner == owner)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "previousOwner")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    previousOwner  =  currentOwner
    solver.add(previousOwner  == previousOwner )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentOwner")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentOwner  =  owner
    solver.add(currentOwner  == currentOwner )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


