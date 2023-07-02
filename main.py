from fsm_parser import generate_fsm_json
from fsm_graph import generate_fsm_graph, draw_fsm_graph

# Example usage:
input_text = """N1 c:C>start(c) S0
_S0 b:B>c.makeoffer(p) S1
S1 o>c.acceptoffer() S2+
S1 o>c.rejectoffer() S3
S3 b|b:B>c.makeOffer(p) S1
"""

fsm = generate_fsm_json(input_text)
graph = generate_fsm_graph(fsm)
draw_fsm_graph(graph)
file_path = "data.json"

# Dump the data into the file
with open(file_path, "w") as file:
    file.writelines(fsm)
