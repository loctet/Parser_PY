import ply.lex as lex
import ply.yacc as yacc

# Lexer rules
tokens = [
    "INT",
    "STRING",
    "ARRAY",
    "DECLARE",
    "EQUALS",
    "ID",
]

t_INT = r"\d+"
t_STRING = r"'[^']*'"
t_ARRAY = r"array"
t_DECLARE = r"declare"
t_EQUALS = r"="
t_ID = r"[a-zA-Z_][a-zA-Z0-9_]*"

t_ignore = ' \t'


def t_error(t):
    """Print an error message for invalid tokens"""
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

# Parser rules
def p_program(p):
    """program : declaration_list"""
    p[0] = p[1]

def p_declaration_list(p):
    """declaration_list : declaration declaration_list
                       | declaration"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + p[2]

def p_declaration(p):
    """declaration : DECLARE ID EQUALS type"""
    p[0] = ("declaration", p[2], p[4])

def p_type(p):
    """type : INT
            | STRING
            | ARRAY INT"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ("array", p[2])

parser = yacc.yacc()

def main():
    """Main function"""
    code = input("Enter a program: ")
    parser.parse(code)


main()
