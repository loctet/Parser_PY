import json
from z3 import *
from PathGenerator import PathGenerator
from SolverGenerator import SolverGenerator
from VariableDeclarationConverter import VariableDeclarationConverter 


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
        
    print(f"\n(Check the generated file  {file_name}.py to fine the z3 code generated)\n") 

def get_json_from_file(file_name = "simplemarket_place"):

    input_path = f"./examples/{file_name}.json"
    with open(input_path, 'r') as file:
        input_text = file.readlines()
    fsm = json.loads(''.join(input_text))
    
    return [fsm, input_text]

def get_grouped_transaction(transitions):
    grouped_transitions = group_transactions(transitions)
    grouped_transitions_copy = grouped_transitions.copy()
    return [grouped_transitions, grouped_transitions_copy ]   

def check_well_formness(fsm, file_name):
    transitions = fsm['transitions']
    # Example usage
    declarations_str = fsm['statesDeclaration']
    print("Checking the well formness of the model----\n")
    temp = SolverGenerator()
    temp.paticipants.add_participants(fsm['rPAssociation'])
    result, deploy_init_var_val, var_names = VariableDeclarationConverter.convert_to_z3_declarations(declarations_str, temp.deploy_init_var_val, temp.var_names)
    
    setattr(temp, 'deploy_init_var_val', deploy_init_var_val)
    setattr(temp, 'var_names', var_names)
    
    temp.append(result)
    grouped_transitions, grouped_transitions_copy = get_grouped_transaction(transitions)
    data = grouped_transitions_copy.pop("_", [])

    while data:
        for transition in data:
            preC = transition['preCondition']
            to = transition['to']
            actionL = transition['actionLabel']
            postC = transition['postCondition']
            data = grouped_transitions.get(to, [])
            otherPreC = [item['preCondition'] for item in data]
            inputs = [item['input'] for item in data]
            
            temp.add_assertion(preC, otherPreC, (transition['input'],inputs), actionL, postC)
            
            if to not in grouped_transitions and to not in fsm['finalStates']:
                print(f"Warning: {to} is not a final state but has no trasitions from {to}")
        
        key, data = grouped_transitions_copy.popitem() if len(grouped_transitions_copy) > 0 else ["", []]


    execute_model_and_save(temp, f"{file_name}_formness")
    print("End----\n\n")


def check_independant_sat(fsm, file_name):
    transitions = fsm['transitions']
    # Example usage
    declarations_str = fsm['statesDeclaration']
    print("Checking independent statisfiability of the model----\n\n")
    temp = SolverGenerator()
    temp.paticipants.add_participants(fsm['rPAssociation'])
    result, deploy_init_var_val, var_names = VariableDeclarationConverter.convert_to_z3_declarations(declarations_str, temp.deploy_init_var_val, temp.var_names)

    setattr(temp, 'deploy_init_var_val', deploy_init_var_val)
    setattr(temp, 'var_names', var_names)
    temp.append(result)
    
    grouped_transitions, grouped_transitions_copy = get_grouped_transaction(transitions)
    
    for key in grouped_transitions:
        
        for transition in grouped_transitions[key]:
            preC = transition['preCondition']
            to = transition['to']
            actionL = transition['actionLabel']
            postC = transition['postCondition']
            data_ = grouped_transitions.get(to, [])
            otherPreC = [item['preCondition'] for item in data_]
            inputs = [item['input'] for item in data_]
            temp.add_assertion(preC, otherPreC, (transition['input'],inputs), actionL, postC)
            
            if to not in grouped_transitions and to not in fsm['finalStates']:
                print(f"Warning: {to} is not a final state but has no trasitions from {to}")
                
    execute_model_and_save(temp, f"{file_name}_indep_sat")
    print("End----\n\n")

def check_path_sat(fsm, file_name = ""):
    print("Checking Path statisfiability of the model----\n\n")
    PathGenerator.check_path_satisfiability(fsm, file_name)

    print("End----\n\n")