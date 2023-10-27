import json
from z3 import *
from TempSolver import *

check_resut = None 

input_path = "./examples/simplemarket_place.json"

with open(input_path, 'r') as file:
    input_text = file.readlines()

fsm = json.loads(''.join(input_text))
transitions = fsm['transitions']


# Example usage
declarations_str = fsm['statesDeclaration']

temp = TempSolver()
temp.add_participants(fsm['rPAssociation'])
temp.append(temp.convert_to_z3_declarations(declarations_str))

for transition in transitions:
    preC = transition['preCondition']
    postC = transition['postCondition']
    temp.add_assertion(preC, postC, transition['actionLabel'], transition['input'])

str_code = temp.generate_solver_code("check_resut")
print(str_code)
exec(str_code)

if  check_resut == True:
   print("satisfiable")

"""
solver = z3.Solver()
a = Int('a')
a = 10
c = Bool('c')
c = True
B = Array('B', IntSort(), IntSort())
M = Array('M', IntSort(), IntSort())

solver.add(a >= 10)
print(solver.check())

x = Int('x')
y = Int('y')
print (simplify(x + y + 2*x + 3))
print (simplify(x < y + x + 2))
print (simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))

x = Int('x')
y = Int('y')
n = x + y >= 3
print ("num args: ", n.num_args())
print ("children: ", n.children())
print ("1st child:", n.arg(0))
print ("2nd child:", n.arg(1))
print ("operator: ", n.decl())
print ("op name:  ", n.decl().name())

p = Bool('p')
q = Bool('q')
print (And(p, q, True))
print (simplify(And(p, q, True)))
print (simplify(And(p, False)))

x = Real('x')
y = Real('y')
s = Solver()
s.add(x > 1, y > 1, Or(x + y > 3, x - y < 2))
print ("asserted constraints...")
for c in s.assertions():
    print (c)

print (".......")    
x = Int('x')
y = Int('y')
f = Function('f', IntSort(), IntSort())
s = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)
print (s.check())
m = s.model()
print ("f(f(x)) =", m.evaluate(f(f(x))))
print ("f(x)    =", m.evaluate(f(x)))

# Create list [1, ..., 5] 
print ([ x + 1 for x in range(5) ])

# Create two lists containing 5 integer variables
X = [ Int('x%s' % i) for i in range(5) ]
Y = [ Int('y%s' % i) for i in range(5) ]
print (X)

# Create a list containing X[i]+Y[i]
X_plus_Y = [ X[i] + Y[i] for i in range(5) ]
print (X_plus_Y)

# Create a list containing X[i] > Y[i]
X_gt_Y = [ X[i] > Y[i] for i in range(5) ]
print (X_gt_Y)

print (And(X_gt_Y))

# Create a 3x3 "matrix" (list of lists) of integer variables
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(3) ]
      for i in range(3) ]
pp(X)


#Declare a List of integers
List = Datatype('List')
# Constructor cons: (Int, List) -> List
List.declare('cons', ('car', IntSort()), ('cdr', List))
# Constructor nil: List
List.declare('nil')
# Create the datatype
List = List.create()
print (is_sort(List))
cons = List.cons
car  = List.car
cdr  = List.cdr
nil  = List.nil
# cons, car and cdr are function declarations, and nil a constant
print (is_func_decl(cons))
print (is_expr(nil))

l1 = cons(10, cons(20, nil))
print (l1)
print (simplify(cdr(l1)))
print (simplify(car(l1)))
print (simplify(l1 == nil))
"""