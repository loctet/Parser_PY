from z3 import *

a = Int('a')
a = 10
c = Bool('c')
c = True
B = Array('B', IntSort(), IntSort())
M = Array('M', IntSort(), IntSort())
v = String('v')
v = "'elvis'"

role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, String('d'))
solver_starts = z3.Solver()

solver_starts.add(True)
solver_starts.add(And(Or(False,True),True))
solver_f1 = z3.Solver()

solver_f1.add(And(Or(False,True),True))
solver_f1.add()
solver_OK = z3.Solver()

solver_OK.add(And(Or(False,True),a >= 10))
solver_OK.add(True)
check_resut = (solver_starts.check() == z3.sat and solver_f1.check() == z3.sat and solver_OK.check() == z3.sat)
