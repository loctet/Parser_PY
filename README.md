
```markdown
# Finite State Machine (FSM) Parser and Visualization

This project contains a Python implementation to parse a description of a Finite State Machine (FSM) and visualize it as a transition graph.

## Prerequisites

- Python 3.x
- NetworkX
- Matplotlib

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fsm-parser.git
   cd fsm-parser
   ```

2. Example usage in `main.py`:

   ```python
   from fsm_parser import generate_fsm_json
   from fsm_table import generate_fsm_table_json
   from fsm_graph import generate_fsm_graph, draw_fsm_graph

   input_text = "... YOUR FSM DESCRIPTION HERE ..."

   #Generate FSM JSON
   fsm = generate_fsm_json(input_text)

   # Generate FSM transition table as JSON
   table_json = generate_fsm_table_json(input_text)
   print(table_json)

   # Generate and draw FSM transition graph
   graph = generate_fsm_graph(fsm)
   draw_fsm_graph(graph)
   ```

3. Execute the script:

   ```bash
   python main.py
   ```

## FSM Description Format

The FSM description should follow a specific format:

- Each line represents a transition between two states.
- Use `_` prefix for initial states and `+` suffix for final states.
- Use `participant:Type` to represent new participants.
- Use `participant>` to represent existing participants.
- Use `>action` to represent the action called in the transition.

Example FSM description:

```
_S0 o:O>action(x) S1
S1 o>Test(x1) S2+
S2 b:B>f2() S3
S3 o>makeOffer(c:B) S1
```
```

For more details, please refer to the [FSM Parser and Visualization documentation](https://github.com/your-username/fsm-parser).
```
