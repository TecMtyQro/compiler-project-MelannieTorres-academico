
#librerías
#main
#que crezca a la derecha

def p_block(t):
    '''block :  LEFT_CURLY_BRACKET expression RIGHT_CURLY_BRACKET'''

def p_expression(t):
    '''expression : while_expression
                  | if_expression
                  | arithmetic_expression
                  | bool_expression
                  | assign_expression'''

def p_while_expression(t):
    '''while_expression : WHILE LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block'''

def p_if_expression(t):
    '''if_expression : IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block
                     | IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block ELSE block'''

def p_assign_expression(t):
    '''assign_expression : INT ID EQUALS arithmetic_expression
              | FLOAT ID EQUALS arithmetic_expression
              | BOOL ID EQUALS bool_expression
              | STRING ID EQUALS string_expression'''
#start arithmetic_expressions
def p_arithmetic_expression(t):
    '''arithmetic_expression : term ADD arithmetic_expression
                             | term MINUS arithmetic_expression
                             | term '''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]

def p_multiplication(t):
    '''term : number MULTIPLICATION term
            | number DIVISION term
            | number '''

def p_number(t):
    '''number : INT_LITERAL
              | FLOAT_LITERAL '''
#ends arithmetic_expressions

#start binary_expression

def p_bool_expression(t):
    '''bool_expression : bool_expression AND BOOL_LITERAL
                         | bool_expression OR BOOL_LITERAL
                         | BOOL_LITERAL '''

def p_string_expression(t):
    '''string_expression : QUOTE STRING_LITERAL QUOTE
                         | DOUBLE_QUOTE STRING_LITERAL DOUBLE_QUOTE '''

def p_condition(t):
    '''condition : condition GT term
                   | condition LT term
                   | condition GET term
                   | condition LET term
                   | condition IS_EQUAL term
                   | condition IS_NOT_EQUAL term
                   | BOOL_LITERAL
                   | term'''


# def p_accept(t):
#     '''expression : PUBLIC
#                 | PRIVATE
#                 | CONST
#                 | READ
#                 | RETURN
#                 | VAR
#                 | WRITE
#                 | NOT
#                 | COMMA
#                 | SEMICOLON
#                 '''
    print('', end = '')

def p_error(t):
    if (t):
            print('', end = '')
            #print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


while True:
    try:
        s = input('> ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
