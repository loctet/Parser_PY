from z3 import * 
from Z3.Extension import *


solver = z3.Solver()
check = True
solver.push()


## initializeWallet

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "pendingTransactions")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    pendingTransactions  =  empty
    _tmp_ =  empty
    solver.add(pendingTransactions  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "approvedOwners")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    approvedOwners  =  empty
    _tmp_ =  empty
    solver.add(approvedOwners  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "executedTransaction")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    executedTransaction  =  None
    _tmp_ =  None
    solver.add(executedTransaction  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## submitTransaction

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "pendingTransactions")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    pendingTransactions  =  pendingTransactions
    _tmp_ =  pendingTransactions
    solver.add(pendingTransactions  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "approvedOwners")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    approvedOwners  =  empty
    _tmp_ =  empty
    solver.add(approvedOwners  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## approveTransaction

solver.add(_owner not in approvedOwners)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "approvedOwners")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    approvedOwners  =  approvedOwners
    _tmp_ =  approvedOwners
    solver.add(approvedOwners  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")



## executeTransaction

solver.add(len(approvedOwners) >= 2)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "executedTransaction")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    executedTransaction  =  pendingTransactions[-1]
    _tmp_ =  pendingTransactions[-1]
    solver.add(executedTransaction  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


