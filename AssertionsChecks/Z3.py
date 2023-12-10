from z3 import *
Tie, Shirt = Bools('Tie Shirt')
s = Solver()
s.add(Or(Tie, Shirt), 
    Or(Not(Tie), Shirt), 
    Or(Not(Tie), Not(Shirt)))
print(s.check())
print(s.model())

Z = IntSort()
f = Function('f', Z, Z)
x, y, z = Ints('x y z')
A = Array('A', Z, Z)
fml = Implies(x + 2 == y, f(Store(A, x, 3)[y - 2]) == f(y - x + 1))
solve(Not(fml))

x, y = Ints('x y')
s = Solver()
s.add((x % 4) + 3 * (y / 2) > x - y)
print(s.sexpr())


s = Solver()
A = DeclareSort("A")
B = DeclareSort("B")
R = Function('R', A, A, B)
x, y, z = Consts('x y z', A)
s.add(ForAll([x], R(x, x)))  
s.add(ForAll([x,y], Implies(And(R(x, y), R(y, x)), x == y)))
s.add(ForAll([x,y,z], Implies(And(R(x, y), R(y, z)), R(x, z))))


S = {1, 2, 3, 4}
b = x > 2

ForAll(x, S, b)  # False


def is_in_set(value, set):
  """
  Checks if the value is in the set.

  Args:
    value: The value to check.
    set: The set to check against.

  Returns:
    True if the value is in the set, False otherwise.
  """
  # Create a Z3 solver.
  solver = z3.Solver()

  # Create a Boolean variable for each element in the set.
  set_elements = [z3.Bool('set_element_%d' % i) for i in range(len(set))]

  # Create a constraint that the value is equal to one of the elements in the set.
  solver.add(z3.Or([value == set_element for set_element in set_elements]))

  # Check if the solver has a solution.
  if solver.check() == z3.sat:
    return True
  else:
    return False



def exist_in_set():
  # Create a Z3 solver instance
    solver = Solver()

    # Define the set S as a Z3 set of integers
    S = Array('S', IntSort())

    # Define the formula b in terms of a Z3 integer variable x
    x = Int('x')
    b = x >= 5  # Replace this with your specific formula

    # Add the constraint: There exists x in S such that b is true
    exists_x_satisfying_b = Exists(x, And(Member(x, S), b))

    # Add the constraint to the solver
    solver.add(exists_x_satisfying_b)

    # Check if the constraint is satisfiable
    if solver.check() == sat:
        print("There exists x in S such that b is true.")
        model = solver.model()
        # You can access the value of x that satisfies b from the model if needed.
        # satisfying_x = model[x]
    else:
        print("No such x exists in S that satisfies b.")
    


