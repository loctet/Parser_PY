data = 'int a := 0 ; int b := 10; set B := 0; set M ; a >= b + 10 int := htr'
import ply.lex as lex

var_list_reserved_words = ['int', 'string', 'array', 'set', 'address']
# Define tokens
tokens = [
    'TRUE', 'FALSE', 'ATOM', 'REL_OP', 'OPERATOR',
    'NOT', 'AND', 'OR', 'EXISTS', 'FORALL','VTYPE', 'INTEGER', 'STRING','ACCEPTEDCHAR',
    'FREEZE', 'ID', 'PARTICIPANT', 'DOT', 'IN', 'ASSIGNATION', 'SEMICOLON', 'COLON', 'LPAR', 'RPAR'
]

# Token definitions
# Token definitions
t_TRUE = r'True'
t_FALSE = r'False'
t_REL_OP = r'[<>]=?|==|!='
t_OPERATOR = r'-|\+|\*|\\'
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
t_VTYPE = r'' + '|'.join(var_list_reserved_words)
t_LPAR = r'\('
t_RPAR = r'\)'


# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

def t_ATOM(t):
    r'(?!(?:int|string|array|set|True|False|address|in)\b)[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_STRING(t): 
    r'"[^"\n]*"|\'[^\n\']*\''  # Match anything between single or double quotes
    return t

def t_INTEGER(t):
    r'(-){0,1}\d+'
    t.value = int(t.value)  
    return t

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)