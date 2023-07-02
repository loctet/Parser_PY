import json
import numpy as np


def generate_fsm_table(fsm):
    fsm = json.loads(fsm)

    states = fsm['states']
    transitions = fsm['transitions']

    table = [[''] + states]  # Table header row

    for state in states:
        row = [state]  # Add state as the first element in each row
        for transition in transitions:
            if transition['from'] == state:
                row.append(transition['to'])
            else:
                row.append('')
        table.append(row)

    return table


# def generate_fsm_table_json(text):
#     fsm = generate_fsm_json(text)
#     fsm_table = generate_fsm_table(fsm)
#     return json.dumps(fsm_table, indent=4)


def generate_transition_table(fsm):
    states = fsm['states']
    transitions = fsm['transitions']

    # Create an empty boolean table filled with False
    table = np.zeros((len(states), len(states)), dtype=bool)

    for transition in transitions:
        from_state = transition['from']
        to_state = transition['to']

        # Get the indices of the states in the table
        from_index = states.index(from_state)
        to_index = states.index(to_state)

        # Set the corresponding entry to True
        table[from_index, to_index] = True

    return table

def generate_transition_name_table(fsm):
    states = fsm['states']
    transitions = fsm['transitions']

    # Create an empty table filled with empty strings
    table = np.empty((len(states), len(states)), dtype='U50')
    table.fill('')

    for transition in transitions:
        from_state = transition['from']
        to_state = transition['to']
        action_called = transition['actionCalled']

        # Get the indices of the states in the table
        from_index = states.index(from_state)
        to_index = states.index(to_state)

        # Set the corresponding entry to the transition name
        table[from_index, to_index] = action_called

    return table

def check_reachable_states(transition_table, initial_states, final_states):
    num_states = transition_table.shape[0]

    # Initialize a list to keep track of reachable states
    reachable_states = []

    # Perform a depth-first search (DFS) from each initial state
    for initial_state in initial_states:
        visited = np.zeros(num_states, dtype=bool)
        dfs(initial_state, transition_table, visited, reachable_states)

    # Find unreachable states by subtracting reachable states from all states
    unreachable_states = set(range(num_states)) - set(reachable_states)

    return list(reachable_states), list(unreachable_states)

def dfs(state, transition_table, visited, reachable_states):
    visited[state] = True
    reachable_states.append(state)

    # Find the next states reachable from the current state
    next_states = np.where(transition_table[state])[0]

    for next_state in next_states:
        if not visited[next_state]:
            dfs(next_state, transition_table, visited, reachable_states)
