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



## terminateSharing

solver.add(True)
check = check and solver.check() == z3.sat
solver.pop()
solver.push()


print(f'=>{check}')


