import json
from z3 import *
from TempSolver import *

def save_infile(str_code):
    # Specify the file name with a .py extension
    file_name = "str_code.py"

    # Open the file for writing and write the code
    with open(file_name, "w") as file:
        file.write(f"from z3 import * \nfrom Z3.Extension import *\n\n{str_code}")

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

#save before sexecute
save_infile(str_code)
exec(str_code)

if  check_resut == True:
    print("satisfiable")
else:
    print("unSatisfiable")

print("(Check the generated file str_code.py to fine the z3 code generated)")

str_code += temp.dump_models()
#save with models in case it executes
save_infile(str_code)

