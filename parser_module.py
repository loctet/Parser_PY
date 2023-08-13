from Parser.Parser import Parser
import hashlib

def only_has_declaration(parser, pKey):
    return not parser.has_assignation[pKey] and not parser.has_assertion[pKey] and not parser.has_existential[pKey]

def process_transitions(transitions, parser):
    for transition in transitions:
        preC = transition['preCondition']
        preCKey = hashlib.md5(('preC'.join(transition)).encode()).hexdigest()
        postC = transition['postCondition']
        postCKey = hashlib.md5(('postC'.join(transition)).encode()).hexdigest()
        params = transition['input']
        paramKey = hashlib.md5(('paramKey'.join(transition)).encode()).hexdigest()
        parser.check_assertion_syntax(params, paramKey)

        if (len(preC) != 0):
            parser.check_assertion_syntax(preC, preCKey)
            if(transition['actionLabel'] == 'starts'):
                print(f" ' No precondition in the start")

            if(transition['actionLabel'] != 'starts' and (parser.has_assignation[preCKey] or parser.has_declaration[preCKey])):
                print(f" Only deploy action can have assignation or declaration")
                parser.has_error[preCKey] = True


            if not parser.has_error[preCKey] and transition['actionLabel'] != 'starts':
                print(f" '{preC}' is correctly written.")
            else:
                print(f" '{preC}' is incorrectly written.")

        if (len(postC) != 0):
            parser.check_assertion_syntax(postC, postCKey)
            if(transition['actionLabel'] != 'starts' and (parser.has_assignation[postCKey] or parser.has_declaration[postCKey])):
                print(f" '{postC}' is incorrectly written. Only deploy action can have assignation or declaration")
                parser.has_error[postCKey] = True

            if not parser.has_error[postCKey]:
                print(f" '{postC}' is correctly written.")
            else:
                print(f" '{postC}' is incorrectly written.")

        if (len(transition['input']) > 0):
            has_allInPost = True
            for toexist in parser.tobe_in_existential[paramKey]:
                if(toexist not in parser.has_existentials[postCKey]):
                    print(f"Existance of {toexist} Should be added in post condition")
                    has_allInPost = False

            if not parser.has_error[paramKey] and only_has_declaration(parser, paramKey) and has_allInPost:
                print(f" '{params}' is correctly written.")
            else:
                print(f" '{params}' is incorrectly written.")
