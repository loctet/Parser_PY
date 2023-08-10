from Parser.Parser import Parser
import json
import hashlib
from DataTypes.RolesParticipants import RolesParticipants


def only_has_declaration(parser, pKey):
    return not parser.has_assignation[pKey] and not parser.has_assertion[pKey] and not parser.has_existential[pKey]


input_path = "./global_out.json"

with open(input_path, 'r') as file:
    input_text = file.readlines()


fsm = json.loads(''.join(input_text))
transitions = fsm['transitions']

role_set = RolesParticipants()
role_set.add_multiple_elements(fsm['rPAssociation'])

parser = Parser(role_set)
preC = ''
postC = ''

for transition in transitions:
    preC = transition['preCondition']
    preCKey = hashlib.md5(('preC'.join(transition)).encode()).hexdigest()
    postC = transition['postCondition']
    postCKey = hashlib.md5(('postC'.join(transition)).encode()).hexdigest()
    
    if (len(preC) != 0):
        parser.check_assertion_syntax(preC, preCKey)
        if(transition['actionLabel'] == 'starts'): 
            print(f" ' No precondition in the start")
            
        if(transition['actionLabel'] != 'starts' and (parser.has_assignation[preCKey] or parser.has_declaration[preCKey])): 
            print(f" Only deploy action can have assignation or declaration")
            
        if not parser.has_error[preCKey] and transition['actionLabel'] != 'starts':
            print(f" '{preC}' is correctly written.")
        else :
            print(f" '{preC}' is incorrectly written.")

    if (len(postC) != 0):    
        parser.check_assertion_syntax(postC, postCKey)
        if(transition['actionLabel'] != 'starts' and (parser.has_assignation[postCKey] or parser.has_declaration[postCKey])): 
            print(f" '{postC}' is incorrectly written. Only deploy action can have assignation or declaration")
            
        if not parser.has_error[postCKey]:
            print(f" '{postC}' is correctly written.")
        else:
            print(f" '{postC}' is incorrectly written.")
    
    if (len(transition['input']) > 0):
        params = transition['input']
        paramKey = hashlib.md5(('paramKey'.join(transition)).encode()).hexdigest()

        parser.check_assertion_syntax(params, paramKey)
        has_allInPost = True
        for toexist in parser.tobe_in_existential[paramKey]:
            if(toexist not in parser.has_existentials[postCKey]):
                print(f"Existance of {toexist} Should be added in post condition")
                has_allInPost = False

        if not parser.has_error[paramKey] and only_has_declaration(parser, paramKey) and has_allInPost:
            print(f" '{params}' is correctly written.")
        else:
            print(f" '{params}' is incorrectly written.")

# Test cases
# check_assertion_syntax("b1 && b2 && e == c")
# check_assertion_syntax("£x.b")
# check_assertion_syntax("b1 == b2")
# check_assertion_syntax("b1 >= 50")
# check_assertion_syntax("b1 && b2 || e == c")
# check_assertion_syntax("b1 && b2 || e == c")
# check_assertion_syntax("b1 && b2 ||  ∀x.b")
# check_assertion_syntax("∀x.b || £x.b")
# check_assertion_syntax("£x.b")
# check_assertion_syntax("∀x.b")
# check_assertion_syntax("∃b.p")
# check_assertion_syntax("p")
# check_assertion_syntax("True")
# check_assertion_syntax("False")
# check_assertion_syntax("True && True")
# check_assertion_syntax("m4")
# check_assertion_syntax("b1 && b2 || !c")
# check_assertion_syntax("a := 50") 
# check_assertion_syntax("int a := 0; b := 10; a >= b; B := 0")  
# 
# check_assertion_syntax('int a := 0')  
# check_assertion_syntax('string b := "test"') 