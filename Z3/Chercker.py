import json
from z3 import *
from TempSolver import *


def save_infile(str_code, file_name = "str_code"):
    # Specify the file name with a .py extension
    file_name = f"{file_name}.py"

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

def execute_model_and_save(tempSolver, file_name):  
                  
    str_code = tempSolver.generate_solver_code("check_resut")

    
    str_code += tempSolver.dump_models()
    #save with models in file_name
    save_infile(str_code, file_name)
    #exec
    try:
        os.system(f'python {file_name}.py')
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        
    print(f"\n(Check the generated file  {file_name}.py to fine the z3 code generated)\n\n") 


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

grouped_transitions_copy = grouped_transitions.copy()
data = grouped_transitions_copy.pop("_", [])

while data:
    for transition in data:
        preC = transition['preCondition']
        to = transition['to']
        actionL = transition['actionLabel']
        postC = transition['postCondition']
        data = grouped_transitions.get(to, [])
        grouped_transitions_copy.pop(to)
        otherPreC = [item['preCondition'] for item in data]
        inputs = [item['input'] for item in data]
        inputs.append(transition['input'])
        inputs = [x for x in inputs if x != ""]
        temp.add_assertion(preC, otherPreC, actionL, inputs, postC)
        
        if to not in grouped_transitions and to not in fsm['finalStates']:
            print(f"Warning: {to} is not a final state but has no trasitions from {to}")
    
    data = grouped_transitions_copy.popitem() if len(grouped_transitions_copy) > 0 else {}

print("Checking the well formness of the model\n")
execute_model_and_save(temp, "str_code_1")


temp2 = TempSolver()
temp2.add_participants(fsm['rPAssociation'])
temp2.append(temp2.convert_to_z3_declarations(declarations_str))
##print(grouped_transitions)
for key in grouped_transitions:
    
    for transition in grouped_transitions[key]:
        preC = transition['preCondition']
        to = transition['to']
        ###print(transition['actionLabel'])
        actionL = transition['actionLabel']
        postC = transition['postCondition']
        data_ = grouped_transitions.get(to, [])
        otherPreC = [item['preCondition'] for item in data_]
        inputs = [item['input'] for item in data_]
        inputs.append(transition['input'])
        inputs = [x for x in inputs if x != ""]
        temp2.add_assertion(preC, otherPreC, actionL, inputs, postC)
        
        if to not in grouped_transitions and to not in fsm['finalStates']:
            print(f"Warning: {to} is not a final state but has no trasitions from {to}")
       

print("Checking independent statisfiability of the model\n")
execute_model_and_save(temp2, "str_code_2")