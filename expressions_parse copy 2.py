import ply.lex as lex
import ply.yacc as yacc

class ParserResult:
    has_error = False
    has_declaration = False
    has_assignation = False
    has_assertion = False

reserved_words = ['int', 'string', 'array', 'set']
# Regular expression
regex = r'(?!(?:' + '|'.join(reserved_words) + r')\b)[a-zA-Z_][a-zA-Z_0-9]*|\d+|"[^"]*"'


results = ParserResult()


# Define tokens
tokens = [
    'TRUE', 'FALSE', 'ATOM', 'REL_OP',
    'NOT', 'AND', 'OR', 'EXISTS', 'FORALL','VTYPE', 'INTEGER', 'STRING','ACCEPTEDCHAR',
    'FREEZE', 'ID', 'PARTICIPANT', 'DOT', 'IN', 'ASSIGNATION', 'SEMICOLON'
]

# Token definitions
# Token definitions
t_TRUE = r'True'
t_FALSE = r'False'
t_ATOM = r'(?!int\b|string\b|array\b|set\b)[a-zA-Z_][a-zA-Z_0-9]*'
t_REL_OP = r'[<>]=?|==|!='
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_EXISTS = r'\∃[a-zA-Z_][a-zA-Z_0-9]*'
t_FORALL = r'\∀[a-zA-Z_][a-zA-Z_0-9]*'
t_FREEZE = r'\£[a-zA-Z_][a-zA-Z_0-9]*'
t_DOT = r'\.'
t_IN = r'in'
t_ASSIGNATION = r':='
t_SEMICOLON = r';'
t_VTYPE = r'' + '|'.join(reserved_words)
t_ACCEPTEDCHAR = r'\.|\(|\)'

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

def t_STRING(t): 
    r'/^\"[a-zA-Z_0-9]*\"$/'
    print('STring :'+t.value)
    return t

def t_INTEGER(t):
    r'(-){0,1}[0-9]+'
    t.value = int(t.value)   
    return t

# Lexer
lexer = lex.lex()

# Custom function to handle assertion rule
def handle_assertion(p):
    global results
    results.has_assertion = True
    return p

# Custom function to handle declaration rule
def handle_declaration(p):
    global results
    results.has_declaration = True
    # Return the extracted data
    return p[1], p[2], p[4]

# Custom function to handle assignation rule
def handle_assignation(p):
    global results
    results.has_assignation = True

    # Return the extracted data
    return p[1], p[3]

# Parser rules
def p_statements(p):
    '''statements : statement
                  | statements statement'''

def p_statement(p):
    '''statement : assertion
                 | declaration
                 | SEMICOLON statement'''

def p_assertion(p):
    '''assertion : ATOM
                 | TRUE
                 | FALSE
                 | expression REL_OP expression
                 | FREEZE DOT assertion
                 | NOT assertion
                 | assertion AND assertion
                 | assertion OR assertion
                 | EXISTS DOT assertion
                 | EXISTS PARTICIPANT DOT assertion
                 | FORALL DOT assertion
                 | FORALL PARTICIPANT DOT assertion
                 | assignation
                 '''
    handle_assertion(p)

def p_expression(p):
    '''expression : fixedvalues
                    | expression REL_OP expression
                    | PARTICIPANT DOT ATOM
                    '''
    return p

def p_fixedvalues(p):
    '''fixedvalues : ATOM
                    | TRUE
                    | FALSE
                    | INTEGER
                    | STRING
                    '''
    return p

def p_declaration(p):
    '''declaration : VTYPE ATOM ASSIGNATION ATOM
                   | VTYPE ATOM ASSIGNATION TRUE
                   | VTYPE ATOM ASSIGNATION FALSE
                   | VTYPE ATOM ASSIGNATION INTEGER
                   | VTYPE ATOM ASSIGNATION STRING
    '''
    variable_type, identifier, expression = handle_declaration(p)
    return p

def p_assignation(p):
    '''assignation : ATOM ASSIGNATION ATOM
                   | ATOM ASSIGNATION TRUE
                   | ATOM ASSIGNATION FALSE
                   | ATOM ASSIGNATION INTEGER
                   | ATOM ASSIGNATION STRING
    '''
    identifier, expression = handle_assignation(p)
    return p



# Error handling for syntax errors
def p_error(p):
    global results
    results.has_error = True

# Build parser
parser = yacc.yacc()

# Function to check if the assertion is correctly written
def check_assertion_syntax(input_str):
    try:
        global results
        results.has_error = False
        results.input_str = input_str
        result = parser.parse(input_str)
        return results
    except Exception as e:
        print(f"Assertion '{input_str}' is not correctly written. Error: {e}")
