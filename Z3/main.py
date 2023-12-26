import sys
from Chercker import get_json_from_file, check_well_formness, check_independant_sat, check_path_sat
# setting path
sys.path.append('../')
from Parser_PY.fsm_graph import *

def print_help():
    help_text = """
    Usage: main.py [JSON_FILE_NAME] [CHECK_TYPE]

    Arguments:
    - JSON_FILE_NAME (without extension): The name of the JSON file for processing.
    - CHECK_TYPE (optional): The type of check to perform on the JSON file. 
      Options:
        1 - Well-Formedness Check: Validates the JSON file's structure.
        2 - Individual Function Check: Tests individual functions within the JSON file.
        3 - Path Check: Verifies the correctness of paths in the JSON file.
      If no check type is specified, all checks are performed.

    Example:
    python main.py simplemarket_place 3
    This command performs a Path Check on the 'simplemarket_place' JSON file.
    """
    print(help_text)



argv = sys.argv
if len(argv) == 1 :
    print_help()
    sys.exit(1)


file_name = argv[1]
option = int(argv[2] if len(argv) >2 else 0 )

fsm, input_text = get_json_from_file(file_name)

if option == 1:
    check_well_formness(fsm, file_name)
elif option == 2:
    check_independant_sat(fsm, file_name)
elif option == 3:
    check_path_sat(fsm, file_name)
elif option == 4:
    draw_fsm_graph(generate_fsm_graph(''.join(input_text)))
else:
    check_well_formness(fsm, file_name)
    check_independant_sat(fsm, file_name)
    check_path_sat(fsm, file_name)
    
