import json
from fsm_graph import *

input_path = "./examples/simplemarket_place.json"

with open(input_path, 'r') as file:
    input_text = file.readlines()

draw_fsm_graph(generate_fsm_graph(''.join(input_text)))