from z3 import *
# setting path
sys.path.append('../') 
from Parser_PY.Z3.Extension import *

secret = String('secret')
gameWon = Bool('gameWon')

solver = z3.Solver()
check = True
solver.push()
_secret = String('_secret')


## initializeGame

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "secret")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    secret  =  _secret
    _tmp_ =  _secret
    solver.add(secret  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "gameWon")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    gameWon  =  False
    _tmp_ =  False
    solver.add(gameWon  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")

_guess = String('_guess')


## makeGuess

solver.add(And(Not(gameWon), _guess.eq(secret)))
check = check and solver.check() == z3.sat
solver.pop()
solver.push()

# Define a regular expression pattern to match variable names inside brackets or parentheses
pattern = r'[^\[\]{}()]*[^\[\]{}()\s]'
# Use re.search to find the first match in the expression
match = re.search(pattern, "gameWon")

# Check if the variable exists in locals() or globals()
if match.group(0) in globals():
    # If the variable exists, create a valid assignment
    gameWon  =  True
    _tmp_ =  True
    solver.add(gameWon  == _tmp_)
else:
    raise NameError(f"State Variable '{match.group(0)}' does not exist")


print(f'=>{check}')


