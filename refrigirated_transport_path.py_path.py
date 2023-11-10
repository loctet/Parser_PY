from z3 import * 
from Z3.Extension import *

stage = Int('stage')
stage = 0
MaxHum = Int('MaxHum')
MinHum = Int('MinHum')
MaxTem = Int('MaxTem')
MinTem = Int('MinTem')
d = String('d')
cp = String('cp')
hum = Int('hum')
tem = Int('tem')

solver = z3.Solver()
check = True
solver.push()
_d = String('_d')


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "d")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    d  =  _d
    solver.add(d  == d )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_cp = String('_cp')


## transResp

solver.add(Or(stage == 1, stage == 2))
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "stage")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    stage  =  1
    solver.add(stage  == stage )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "cp")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    cp  =  _cp
    solver.add(cp  == cp )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## complete

solver.add(stage == 2)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "stage")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    stage  =  3
    solver.add(stage  == stage )
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


