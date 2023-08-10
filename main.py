import json
from DataTypes.RolesParticipants import RolesParticipants
from parser_module import Parser, process_transitions

input_path = "./global_out.json"

with open(input_path, 'r') as file:
    input_text = file.readlines()

fsm = json.loads(''.join(input_text))
transitions = fsm['transitions']

role_set = RolesParticipants()
role_set.add_multiple_elements(fsm['rPAssociation'])

parser = Parser(role_set)
process_transitions(transitions, parser)

# Test cases
# ...
