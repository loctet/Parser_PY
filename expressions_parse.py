import ply.lex as lex
import ply.yacc as yacc

has_error = False
# Define tokens
tokens = [
    'TRUE', 'FALSE', 'ATOM', 'REL_OP',
    'NOT', 'AND', 'OR', 'EXISTS', 'FORALL',
    'FREEZE', 'ID', 'PARTICIPANT', 'DOT', 'IN'
]

# Token definitions
t_TRUE = r'True'
t_FALSE = r'False'
t_ATOM = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_REL_OP = r'[<>]=?|==|!='
t_NOT = r'not'
t_AND = r'\^'
t_OR = r'or'
t_EXISTS = r'\∃[a-zA-Z_][a-zA-Z_0-9]*'
t_FORALL = r'\∀[a-zA-Z_][a-zA-Z_0-9]*'
t_FREEZE = r'\£[a-zA-Z_][a-zA-Z_0-9]*'
t_DOT = r'\.'
t_IN = r'in'

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Grammar rules
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
                 '''

def p_expression(p):
    '''expression : ATOM
                  | TRUE
                  | FALSE
                  | expression REL_OP expression
                  | PARTICIPANT DOT ATOM'''

# Error handling for syntax errors
def p_error(p):
    global has_error
    has_error = True

# Build parser
parser = yacc.yacc()

# Function to check if the assertion is correctly written
def check_assertion_syntax(input_str):
    try:
        global has_error
        has_error = False
        result = parser.parse(input_str)
        if not has_error:
            print(f"Assertion '{input_str}' is correctly written.")
        else:
            print(f"Assertion '{input_str}' is incorrectly written.")
        print()
    except Exception as e:
        print(f"Assertion '{input_str}' is not correctly written. Error: {e}")

# Test cases
check_assertion_syntax("b1 ^ b2 ^ e == c")
check_assertion_syntax("£x.b")
check_assertion_syntax("b1 == b2")
check_assertion_syntax("b1 ^ b2 ^ e == c")
check_assertion_syntax("b1 ^ b2 ^ e == c")
check_assertion_syntax("b1 ^ b2 ^  ∀x.b")
check_assertion_syntax("∀x.b ^ £x.b")
check_assertion_syntax("£x.b")
check_assertion_syntax("∀x.b")
check_assertion_syntax("∃b.p")
check_assertion_syntax("p")
check_assertion_syntax("b1 ^ b2 or not c")
