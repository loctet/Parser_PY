from z3 import * 

x = Int("x")
y = Int("y")
s = z3.Solver()

#s.add(x > 0)
#s.add(And(y < x -1, y > x))
#s.add(Implies(x > 10, x == 0))

solve((Implies((x == 10), x < 0)))
print(s.check())
"""
x => y 
x => z
x => k

s.add(x)
s.add(Or(y,z,k)) """



