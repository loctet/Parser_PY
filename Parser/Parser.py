import ply.yacc as yacc
from .Lexer import Lexer

class Parser(object):
    tokens = Lexer.tokens

    has_error = {}
    has_declaration = {}
    has_assignation = {}
    has_assertion = {}
    has_existential = {}
    has_existentials = {}
    tobe_in_existential = {}
    registered_variables = {}
    participants = None
        
    # Custom function to handle assertion rule
    def handle_assertion(self, p):
        self.has_assertion[self.key] = True
        if (p[1] not in [None, 'True', 'False']) :
            self.set_errornotdefinedvar(p[1])
        return p

    # Custom function to handle declaration rule
    def handle_declaration(self, p):
        self.has_declaration[self.key] = True
        # Return the extracted data
        if len(p) <= 3 or (len(p) > 3 and p[3] != ':'):
            self.register_var(p[2], p[1])
            return p
        
        if (p[1] == 'address') :
            self.tobe_in_existential[self.key].append(p[2] + ' '+ p[4])
            if not self.participants.is_part_of_subset(p[2], p[4]):
                self.participants.add_element(p[2], p[4])
            else:
                self.has_error[self.key] = True
                print(f"Participant '{p[2]}' is already in list '{p[4]}' ")
        else:
            self.has_error[self.key] = True

        return p

    # Custom function to handle assignation rule
    def handle_assignation(self, p):
        self.has_assignation[self.key] = True

        # Check if the variable has been registered
        self.set_errornotdefinedvar(p[1])
        return p[1], p[3]

    # Parser rules
    def p_statements(self, p):
        '''statements : statement
                    | statements statement'''

    def p_statement(self, p):
        '''statement : declaration
                    | assertion
                    | assignation
                    | SEMICOLON statement'''

    def p_assertion(self, p):
        '''assertion : ATOM
                    | TRUE
                    | FALSE
                    | expression REL_OP expression
                    | NOT assertion
                    | assertion AND assertion
                    | assertion OR assertion
                    | existential
                    | forall
                    | freeze
                    '''
        self.handle_assertion(p)

    def p_expression(self, p):
        '''expression : fixedvalues
                        | variablename
                        | expression REL_OP expression
                        | PARTICIPANT DOT ATOM
                        '''
        return p

    def p_variablename(self, p):
        '''variablename : ATOM'''
        self.set_errornotdefinedvar(p[1])
        return p
    
    def p_fixedvalues(self, p):
        '''fixedvalues : TRUE
                        | FALSE
                        | INTEGER
                        | STRING
                        '''
        return(p)
    
    def p_declaration(self, p):
        '''declaration :  VTYPE ATOM
                    | VTYPE ATOM ASSIGNATION ATOM
                    | VTYPE ATOM ASSIGNATION TRUE
                    | VTYPE ATOM ASSIGNATION FALSE
                    | VTYPE ATOM ASSIGNATION INTEGER
                    | VTYPE ATOM ASSIGNATION STRING
                    | VTYPE ATOM COLON ATOM
        '''
        self.handle_declaration(p)
        return p

    def p_assignation(self, p):
        '''assignation : ATOM ASSIGNATION ATOM
                    | ATOM ASSIGNATION TRUE
                    | ATOM ASSIGNATION FALSE
                    | ATOM ASSIGNATION INTEGER
                    | ATOM ASSIGNATION STRING
        '''
        identifier, expression = self.handle_assignation(p)
        return p


    def p_existential(self, p):
        '''existential : EXISTS ATOM ATOM
                       | EXISTS ATOM ATOM DOT ATOM'''
        self.has_existential[self.key] = True
        self.has_existentials[self.key][p[2] + ' ' + p[3]] = True
        if not self.participants.is_part_of_subset(p[2], p[3]):
            self.has_error[self.key] = True
            print(f"Variable '{p[2]}' Not in list '{p[3]}' ")

        return p

    def p_forall(self, p):
        '''forall : FORALL ATOM ATOM'''
        return p


    def p_freeze(self, p):
        '''freeze : FREEZE ATOM ATOM'''
        
        if not self.participants.is_part_of_subset(p[2], p[3]):
            self.has_error[self.key] = True
            print(f"Variable '{p[2]}' Not in list '{p[3]}' ")

        return p

    def set_errornotdefinedvar(self, p):
        if p not in self.registered_variables:
            print(f"Variable '{p}' has not been registered yet.")
            self.has_error[self.key] = True

    def register_var(self, v, t):
        if v in self.registered_variables:
            print(f"Variable '{v}' has already been registered.")
            self.has_error[self.key] = True
            return
        if (t == 'set') : 
            self.registered_variables[v] = {}
        else:
            self.registered_variables[v] = t
        
    # Error handling for syntax errors
    def p_error(self, p):
        self.has_error[self.key] = True

    def set_participants(self, participants):
        self.participants = participants
    
    def __init__(self, participants):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)
        self.participants = participants

    def reset(self):
        self.has_error[self.key] = None
        self.has_declaration[self.key] = None
        self.has_assignation[self.key] = None
        self.has_assertion[self.key] = None
        self.has_existential[self.key] = None
        self.has_existentials[self.key] = {}
        self.tobe_in_existential[self.key] = []

    # Function to check if the assertion is correctly written
    def check_assertion_syntax(self, input_str, key):
        if (len(input_str) == 0) : 
            return
        self.input_str = input_str
        self.key = key
        self.reset()
        try:
            self.has_error[self.key] = False
            result = self.parser.parse(input_str)
            return self
        except Exception as e:
            print(f"Assertion '{input_str}' is not correctly written. Error: {e}")
