from z3 import *

a = Int('a')
a = 10
c = Bool('c')
c = True
B = Array('B', IntSort(), IntSort())
M = Array('M', IntSort(), IntSort())

role_O = Array('role_O',IntSort(),  StringSort())
o_ = String('o')
Store(role_O, 0, o_)
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, 'b')
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, 'd')
solver_starts = z3.Solver()

solver_starts.add(True)
solver_starts.add(And(Or(False,True),True))
print(solver_starts.check())
solver_f1 = z3.Solver()

solver_f1.add(And(Or(False,True),True))
solver_f1.add()
print(solver_f1.check())
solver_OK = z3.Solver()