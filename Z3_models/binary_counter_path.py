from z3 import *
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

currentStage = Int('currentStage')
currentNumber = Int('currentNumber')

solver = z3.Solver()
check = True
solver.push()


## initializeCounter

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentNumber")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentNumber  =  0
    _tmp_ =  0
    solver.add(currentNumber  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentStage")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentStage  =  0
    _tmp_ =  0
    solver.add(currentStage  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_old = Int('_old')


## incrementCounter

solver.add(currentStage == 0)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "_old")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    _old  =  currentNumber + 1
    _tmp_ =  currentNumber + 1
    solver.add(_old  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentNumber")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentNumber  =  _old
    _tmp_ =  _old
    solver.add(currentNumber  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentStage")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentStage  =  1
    _tmp_ =  1
    solver.add(currentStage  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_old = Int('_old')


## finalizeCounter

solver.add(currentStage == 1)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "_old")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    _old  =  currentNumber + 1
    _tmp_ =  currentNumber + 1
    solver.add(_old  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentNumber")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentNumber  =  _old
    _tmp_ =  _old
    solver.add(currentNumber  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "currentStage")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    currentStage  =  2
    _tmp_ =  2
    solver.add(currentStage  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


