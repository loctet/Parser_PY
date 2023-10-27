from z3 import *

def is_in_set(value, set):
  value = str(value)
  # Create a Z3 solver.
  solver = z3.Solver()

  # Create a strins variable for each element in the set and add rule it must be equal to value in array.
  set_elements = [z3.String('set_element_%d' % i) for i in range(len(set))]
  for i in range(len(set_elements)):
    solver.add(set_elements[i] == str(set[i]))

  # Create a constraint that the value is equal to one of the elements in the set.
  solver.add(z3.Or([value == set_element for set_element in set_elements]))

  # Check if the solver has a solution.
  return solver.check() == z3.sat
  
def exist_in_set(formula, set):
  solver = z3.Solver()
  # Create a strins variable for each element in the set and add rule it must be equal to value in array.
  set_elements = [z3.String('set_element_%d' % i) for i in range(len(set))]
  for i in range(len(set_elements)):
    solver.add(set_elements[i] == str(set[i]))

  # Create a constraint that the value is equal to one of the elements in the set.
  solver.add(z3.Or([formula(set_element) for set_element in set]))

  # Check if the solver has a solution.
  return solver.check() == z3.sat
  
def forall_in_set(formula, set):
  solver = z3.Solver()
  # Create a strins variable for each element in the set and add rule it must be equal to value in array.
  set_elements = [z3.String('set_element_%d' % i) for i in range(len(set))]
  for i in range(len(set_elements)):
    solver.add(set_elements[i] == str(set[i]))

  # Create a constraint that the value is equal to one of the elements in the set.
  solver.add(z3.And([formula(set_element) for set_element in set]))

  # Check if the solver has a solution.
  return solver.check() == z3.sat
