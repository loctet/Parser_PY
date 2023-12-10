from z3 import *
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

approvedOwners = Array('approvedOwners', IntSort(), StringSort())
pendingTransactions = Int('pendingTransactions')
transaction = String('transaction')
minApprNumber = Int('minApprNumber')
empty = Array('empty', IntSort(), StringSort())

solver = z3.Solver()
check = True
solver.push()
_min = Int('_min')


## initializeWallet

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "minApprNumber")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    minApprNumber  =  _min
    _tmp_ =  _min
    solver.add(minApprNumber  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_transaction = String('_transaction')


## submitTransaction

solver.add(pendingTransactions == 0)
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
    pendingTransactions  =  pendingTransactions_old + 1
    _tmp_ =  pendingTransactions_old + 1
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
match = re.search(pattern, "transaction")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    transaction  =  _transaction
    _tmp_ =  _transaction
    solver.add(transaction  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_transaction = String('_transaction')


## executeTransaction

solver.add(len(approvedOwners) >= minAppr)
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
    executedTransaction  =  _transaction
    _tmp_ =  _transaction
    solver.add(executedTransaction  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "pendingTransactions")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    pendingTransactions  =  0
    _tmp_ =  0
    solver.add(pendingTransactions  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


