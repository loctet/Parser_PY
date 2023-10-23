import ply.yacc as yacc
from .Lexer import Lexer

from .parser_state import ParserState
from Handlers.RelOpHandler import RelOpHandler
from Handlers.AssertionHandler import AssertionHandler
from Handlers.DeclarationHandler import DeclarationHandler
from Handlers.AssignationHandler import AssignationHandler
from Handlers.ExistentialHandler import ExistentialHandler
from Handlers.ForAllHandler import ForAllHandler
from Handlers.FreezeHandler import FreezeHandler
from Handlers.VariableNameHandler import VariableNameHandler
from Handlers.CheckInHandler import CheckInHandler

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Parser(object):  
    tokens = Lexer.tokens
    stack = Stack()

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
                    | rel_op_assertion
                    | NOT assertion
                    | and_op_assertion
                    | or_op_assertion
                    | checkin
                    | existential
                    | forall
                    | freeze
                    | LPAR assertion RPAR
                    '''
        self.handlers['assertion'].handle(p)
        self.stack.push(p[:])
        return p

    def p_rel_op_assertion(self, p):
        '''rel_op_assertion : expression REL_OP expression'''

        self.handlers['relop'].handle(p)
        self.stack.push(p[:])
        return p
    
    def p_and_op_assertion(self, p):
        '''and_op_assertion : assertion AND assertion'''
        self.handlers['relop'].handle(p)
        self.stack.push(p[:])
        return p
    
    def p_or_op_assertion(self, p):
        '''or_op_assertion : assertion OR assertion'''
        self.handlers['relop'].handle(p)
        self.stack.push(p[:])
        return p
    
    def p_expression(self, p):
        '''expression : fixedvalues
                        | variablename
                        | expression REL_OP expression
                        | expression OPERATOR expression
                        | PARTICIPANT DOT ATOM
                        '''
        self.stack.push(p[:])
        return p

    def p_variablename(self, p):
        '''variablename : ATOM'''
        self.handlers['variablename'].handle(p)
        #print(self.parser.token())
        self.stack.push(p[:])
        return p
    
    def p_fixedvalues(self, p):
        '''fixedvalues : TRUE
                        | FALSE
                        | INTEGER
                        | STRING
                        '''
        self.stack.push(p[:])
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
        self.handlers['declaration'].handle(p)
        self.stack.push(p[:])
        return p

    def p_assignation(self, p):
        '''assignation : ATOM ASSIGNATION ATOM
                    | ATOM ASSIGNATION TRUE
                    | ATOM ASSIGNATION FALSE
                    | ATOM ASSIGNATION INTEGER
                    | ATOM ASSIGNATION STRING
        '''
        self.handlers['assignation'].handle(p)
        self.stack.push(p[:])
        return p

    def p_checkin(self, p):
        '''checkin : ATOM IN ATOM'''
        self.handlers['checkin'].handle(p)
        self.stack.push(p[:])
        return p
    
    def p_existential(self, p):
        '''existential : EXISTS ATOM ATOM
                       | EXISTS ATOM ATOM DOT LPAR assertion RPAR'''

        self.handlers['existential'].handle(p)
        self.stack.push(p[:])
        return p

    def p_forall(self, p):
        '''forall : FORALL ATOM ATOM
                  | FORALL ATOM ATOM DOT LPAR assertion RPAR'''
        self.handlers['forall'].handle(p)
        self.stack.push(p[:])
        return p


    def p_freeze(self, p):
        '''freeze : FREEZE ATOM ATOM'''
        self.handlers['freeze'].handle(p)
        self.stack.push(p[:])

        return p

    # Parser rules and other methods

    # Error handling for syntax errors
    def p_error(self, p):
        self.state.set_error(self.key)

    
    # Function to check if the assertion is correctly written
    def check_assertion_syntax(self, input_str, key):
        if (len(input_str) == 0) : 
            return
        self.stack.items = []
        self.input_str = input_str
        self.key = key
        self.state.reset(key)
        try:
            self.state.set_error(self.key, False)
            self.parser.parse(input_str)
        except Exception as e:
            print(f"Assertion '{input_str}' is not correctly written. Error: {e}")

        # print(self.stack.items)
        return self
        
       
   
    def __init__(self, participants):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)
        self.state = ParserState(participants)
        self.handlers = {
            'relop': RelOpHandler(self),
            'declaration': DeclarationHandler(self),
            'assertion': AssertionHandler(self),
            'assignation': AssignationHandler(self),
            'existential': ExistentialHandler(self),
            'checkin': CheckInHandler(self),
            'forall': ForAllHandler(self),
            'freeze': FreezeHandler(self),
            'variablename': VariableNameHandler(self)
        }
     
