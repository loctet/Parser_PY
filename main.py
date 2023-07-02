from fsm_parser import generate_fsm_json
from fsm_graph import generate_fsm_graph, draw_fsm_graph

input_path = "./input.txt"

with open(input_path) as file:
    input_text = file.readlines()

fsm = generate_fsm_json(input_text)
graph = generate_fsm_graph(fsm)
draw_fsm_graph(graph)
file_path = "data.json"

# Dump the data into the file
with open(file_path, "w") as file:
    file.writelines(fsm)
