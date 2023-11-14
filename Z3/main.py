import sys
from Chercker import get_json_from_file, check_well_formness, check_independant_sat, check_path_sat

# setting path
sys.path.append('../')

from Parser_PY.fsm_graph import *

argv = sys.argv
if len(argv) == 1 :
    print("""
    To run this file you need to provide at least one argument 
    1- json file name withou extension 
    2- Type of check you will like to perform
        1 for well formnes
        2 for individual funtion check 
        3 path check
        (none) for all  
    ie: python .\Z3\main.py simplemarket_place 3 // will perform only path check    
""")
    exit()


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
    
