from z3 import * 
from Z3.Extension import *

locked = Bool('locked')
requestedL = Bool('requestedL')

solver = z3.Solver()
check = True
solver.push()


## start

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## requestAvailability

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## reviewRequest

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## uploadDigitalAsset

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()



## ShareThirdPartyRequest

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "locked")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    locked  =  True
    _tmp_ =  True
    solver.add(locked  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## terminateSharing

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()


print(f'=>{check}')


