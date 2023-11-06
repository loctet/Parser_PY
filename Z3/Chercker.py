import json
from z3 import *
from TempSolver import *

def save_infile(str_code):
    # Specify the file name with a .py extension
    file_name = "str_code.py"

    # Open the file for writing and write the code
    with open(file_name, "w") as file:
        file.write(f"from z3 import * \nfrom Z3.Extension import *\n\n{str_code}")

def group_transactions(transitions):
    # Create a dictionary to store transitions grouped by "to" state
    transitions_by_to_state = {}
    # Group transitions by "to" state
    for transition in transitions:
        to_state = transition["from"]
        if to_state not in transitions_by_to_state:
            transitions_by_to_state[to_state] = []
        transitions_by_to_state[to_state].append(transition)
    return transitions_by_to_state


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

grouped_transitions = group_transactions(transitions)

for key in grouped_transitions:
    for transition in grouped_transitions[key]:
        preC = transition['preCondition']
        to = transition['to']
        actionL = transition['actionLabel']
        varUpdate = transition['varUpdate']
        postCs = [item['preCondition'] for item in grouped_transitions.get(to, [])]
        inputs = [item['input'] for item in grouped_transitions.get(to, [])]
        inputs.append(transition['input'])
        inputs = [x for x in inputs if x != ""]
        temp.add_assertion(preC, postCs, actionL, inputs, varUpdate)
        
        if to not in grouped_transitions and to not in fsm['finalStates']:
            print(f"Warning: {to} is not a final state but has no trasitions from {to}")
        
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
