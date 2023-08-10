import ply.lex as lex

class Lexer(object):
    reserved_words = ['int', 'string', 'array', 'set', 'adress']
    # Define tokens
    tokens = [
        'TRUE', 'FALSE', 'ATOM', 'REL_OP',
        'NOT', 'AND', 'OR', 'EXISTS', 'FORALL','VTYPE', 'INTEGER', 'STRING','ACCEPTEDCHAR',
        'FREEZE', 'ID', 'PARTICIPANT', 'DOT', 'IN', 'ASSIGNATION', 'SEMICOLON', 'COLON'
    ]

    # Token definitions
    # Token definitions
    t_TRUE = r'True'
    t_FALSE = r'False'
    t_REL_OP = r'[<>]=?|==|!='
    t_NOT = r'!'
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_EXISTS = r'\∃'
    t_FORALL = r'\∀'
    t_FREEZE = r'\£'
    t_DOT = r'\.'
    t_COLON = r':'
    t_IN = r'in'
    t_ASSIGNATION = r':='
    t_SEMICOLON = r';'
    t_VTYPE = r'' + '|'.join(reserved_words)
    t_ACCEPTEDCHAR = r'\.|\(|\)'

    
    # Ignored characters
    t_ignore = ' \t'

    # Error handling
    def t_error(self, t):
        #print(f"Invalid character: {t.value[0]}")
        t.lexer.skip(1)

    def t_ATOM(self, t):
        r'(?!(?:int|string|array|set|True|False|adress)\b)[a-zA-Z_][a-zA-Z_0-9]*'
        return t
    
    def t_STRING(self, t): 
        r'"[^"\n]*"|\'[^\n\']*\''  # Match anything between single or double quotes
        return t

    def t_INTEGER(self, t):
        r'(-){0,1}\d+'
        t.value = int(t.value)   
        return t

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self)

