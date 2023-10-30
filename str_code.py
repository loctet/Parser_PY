from z3 import * 
from Z3.Extension import *

price = Int('price')
state = Bool('state')
M = [1,2,3,4,5]



def formula_0(item):
  solver = z3.Solver()
  solver.add(item > 0)
  return solver.check() == z3.sat
  

def formula_1(item):
  solver = z3.Solver()
  solver.add(item > 0)
  return solver.check() == z3.sat
  
role_O = Array('O',IntSort() , StringSort())
Store(role_O, 0, String('o'))
role_B = Array('B',IntSort() , StringSort())
Store(role_B, 0, String('b'))
role_D = Array('D',IntSort() , StringSort())
Store(role_D, 0, String('d'))




solver_start = z3.Solver()
solver_start_pr = z3.Solver()
solver_start_po = z3.Solver()

solver_start_pr.add(True)
solver_start_po.add(state==True)
solver_start.add(And(solver_start_pr.check() == z3.sat, solver_start_po.check() == z3.sat))


solver_makeoffer = z3.Solver()
solver_makeoffer_pr = z3.Solver()
solver_makeoffer_po = z3.Solver()
_p = Int('_p')

solver_makeoffer_pr.add(And(_p > 0, state == True))
solver_makeoffer_po.add(price == _p)
solver_makeoffer.add(And(solver_makeoffer_pr.check() == z3.sat, solver_makeoffer_po.check() == z3.sat))


solver_acceptoffer = z3.Solver()
solver_acceptoffer_pr = z3.Solver()
solver_acceptoffer_po = z3.Solver()

solver_acceptoffer_pr.add(state)
solver_acceptoffer_po.add(Not(state))
solver_acceptoffer.add(And(solver_acceptoffer_pr.check() == z3.sat, solver_acceptoffer_po.check() == z3.sat))


solver_OK = z3.Solver()
solver_OK_pr = z3.Solver()
solver_OK_po = z3.Solver()

solver_OK_pr.add(True)
solver_OK_po.add(And(Not(state), Or(forall_in_set(formula_0, M), exist_in_set(formula_1, M))))
solver_OK.add(And(solver_OK_pr.check() == z3.sat, solver_OK_po.check() == z3.sat))


solver_NOK = z3.Solver()
solver_NOK_pr = z3.Solver()
solver_NOK_po = z3.Solver()

solver_NOK_pr.add(True)
solver_NOK_po.add(state)
solver_NOK.add(And(solver_NOK_pr.check() == z3.sat, solver_NOK_po.check() == z3.sat))


solver_rejectoffer = z3.Solver()
solver_rejectoffer_pr = z3.Solver()
solver_rejectoffer_po = z3.Solver()

solver_rejectoffer_pr.add(state)
solver_rejectoffer_po.add(Not(state))
solver_rejectoffer.add(And(solver_rejectoffer_pr.check() == z3.sat, solver_rejectoffer_po.check() == z3.sat))
check_resut = (solver_start.check() == z3.sat and solver_makeoffer.check() == z3.sat and solver_acceptoffer.check() == z3.sat and solver_OK.check() == z3.sat and solver_NOK.check() == z3.sat and solver_rejectoffer.check() == z3.sat)
print(solver_start_pr.model()) if solver_start_pr.check() == z3.sat else print('solver_start_pr')
print(solver_start_po.model()) if solver_start_po.check() == z3.sat else print('solver_start_po')
print(solver_makeoffer_pr.model()) if solver_makeoffer_pr.check() == z3.sat else print('solver_makeoffer_pr')
print(solver_makeoffer_po.model()) if solver_makeoffer_po.check() == z3.sat else print('solver_makeoffer_po')
print(solver_acceptoffer_pr.model()) if solver_acceptoffer_pr.check() == z3.sat else print('solver_acceptoffer_pr')
print(solver_acceptoffer_po.model()) if solver_acceptoffer_po.check() == z3.sat else print('solver_acceptoffer_po')
print(solver_OK_pr.model()) if solver_OK_pr.check() == z3.sat else print('solver_OK_pr')
print(solver_OK_po.model()) if solver_OK_po.check() == z3.sat else print('solver_OK_po')
print(solver_NOK_pr.model()) if solver_NOK_pr.check() == z3.sat else print('solver_NOK_pr')
print(solver_NOK_po.model()) if solver_NOK_po.check() == z3.sat else print('solver_NOK_po')
print(solver_rejectoffer_pr.model()) if solver_rejectoffer_pr.check() == z3.sat else print('solver_rejectoffer_pr')
print(solver_rejectoffer_po.model()) if solver_rejectoffer_po.check() == z3.sat else print('solver_rejectoffer_po')
