import os
from Extension import replace_assertion
from SafeVariableAssignment import SafeVariableAssignment
from SolverGenerator import SolverGenerator
from VariableDeclarationConverter import VariableDeclarationConverter


class PathGenerator :
    
    @staticmethod
    def find_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]['to']:
            if node not in path:
                new_paths = PathGenerator.find_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    @staticmethod
    def group_transactions(transition_json):
        graph = {}
        for transition in transition_json['transitions']:
            from_state = transition['from']
            to_state = transition['to']
            if from_state not in graph:
                graph[from_state] = {'to': []}
            graph[from_state]['to'].append(to_state)

        initial_state = transition_json['transitions'][0]['from']
        final_states = transition_json['finalStates']

        grouped_transactions = {}
        for final_state in final_states:
            paths = PathGenerator.find_paths(graph, initial_state, final_state)
            for path in paths:
                path_str = ' -> '.join(path)
                formatted_transitions = []
                for i in range(len(path) - 1):
                    from_state = path[i]
                    to_state = path[i + 1]
                    transition = PathGenerator.find_transition(transition_json['transitions'], from_state, to_state)
                    #formatted_transition = PathGenerator.format_transition(transition)
                    formatted_transitions.append(transition)

                grouped_transactions[path_str] = formatted_transitions

        return grouped_transactions

    @staticmethod
    def find_transition(transitions, from_state, to_state):
        for transition in transitions:
            if transition['from'] == from_state and transition['to'] == to_state:
                return transition
        return None

    @staticmethod
    def format_transition(transition):
        pre_condition = transition['preCondition']
        input_params = transition['input']
        action_label = transition['actionLabel']
        post_condition = transition['postCondition']

        formatted_transition = f"{pre_condition}|{input_params}|{action_label} -> {post_condition}"
        return formatted_transition
    
    @staticmethod
    def check_path_satisfiability(fsm, file_name):
        result = PathGenerator.group_transactions(fsm)
        for path, transitions in result.items():
            print(f"Path: {path}")
            code = "from z3 import * \nfrom Z3.Extension import *\n\n "
            temp = SolverGenerator()
            temp.paticipants.add_participants(fsm['rPAssociation'])
            result, deploy_init_var_val, var_names = VariableDeclarationConverter.convert_to_z3_declarations(fsm['statesDeclaration'], temp.deploy_init_var_val, temp.var_names)
            setattr(temp, 'deploy_init_var_val', deploy_init_var_val)
            setattr(temp, 'var_names', var_names)
            temp.append(result)
            temp.append("solver = z3.Solver()\ncheck = True\nsolver.push()")
            
            for transition in transitions:
                pre = replace_assertion(transition['preCondition'])
                sVarUpdate, global_vars  = SafeVariableAssignment.safe_variable_assignment(transition['postCondition'], 'solver')
                sparams, init_var_val, var_names = VariableDeclarationConverter.convert_to_z3_declarations(transition['input'], [])
                temp.append(f"{sparams}\n\n## {transition['actionLabel']}\n\nsolver.add({pre})\ncheck = check and solver.check() == z3.sat\nsolver.pop()\nsolver.push()\n{sVarUpdate}")
                
            temp.append("\nprint(f'=>{check}')\n\n")    
            temp.str_code = temp.str_code.replace("        ", "____").replace("    ",'').replace("____", "    ")
            # Specify the file name with a .py extension
            file_name = f"{file_name}_path.py"

            # Open the file for writing and write the code
            with open(file_name, "w") as file:
                file.write(f"from z3 import * \nfrom Z3.Extension import *\n\n{temp.str_code}")
            #exec
            try:
                os.system(f'python {file_name}')
            except FileNotFoundError:
                print(f"Error: The file '{file_name}' does not exist.")
            
        print(f"\n(Check the generated file  {file_name}_path.py to fine the z3 code generated)\n") 
            
            

"""



result = PathGenerator.group_transactions(transition_json)
for path, transitions in result.items():
    print(f"Path: {path}")
    for transition in transitions:
        print(f"  {transition}")
    print()
"""