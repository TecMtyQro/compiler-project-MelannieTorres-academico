import fileinput
import sys
#https://www.dabeaz.com/ply/PLYTalk.pdf
#https://github.com/dabeaz/ply/blob/master/example/yply/ylex.py

reserved = {
    'static' : 'STATIC',
    'const' : 'CONST',
    'if' : 'IF',
    'else' : 'ELSE',
    'return' : 'RETURN',
    'while': 'WHILE',
    'Main':'MAIN',
    #datatypes
    'int':'INT',
    'float' : 'FLOAT',
    'bool': 'BOOL',
    'string':'STRING',
    'void': 'VOID'
}

tokens = [
    # I / O
    'READ','WRITE',
    # operators
    'EQUALS','IS_NOT_EQUAL', 'GT', 'LT', 'GET', 'LET',
    'AND', 'OR',
    'IS_EQUAL',
    'ADD','MINUS', 'MULTIPLICATION', 'DIVISION',
    #literals
    'INT_LITERAL', 'FLOAT_LITERAL', 'BOOL_LITERAL', 'STRING_LITERAL',
    #punctuation
    'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS',
    'LEFT_CURLY_BRACKET','RIGHT_CURLY_BRACKET',
    'SEMICOLON',
    #id
    'ID'
]+ list(reserved.values())
# tokens

# comments
# old one line comment regex  r'^(?:[^"/\\]|\"(?:[^\"\\]|\\.)*\"|/(?:[^/"\\]|\\.)|/\"(?:[^\"\\]|\\.)*\"|\\.)*//(.*)$' # regex by python https://stackoverflow.com/questions/15423658/regular-expression-for-single-line-comments
t_ignore_MULTIPLE_LINE_COMMENT = r'(/\*(.|\n)*?\*/)' #r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
t_ignore_ONE_LINE_COMMENT = r'//.*'

#read write
def t_READ(t): r'Console\.Read\(\)'; return t
def t_WRITE(t): r'Console\.Write'; return t

#operators
t_GT = r'>'
t_LT = r'<'
t_GET = r'>='
t_LET = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_IS_EQUAL = r'=='
t_IS_NOT_EQUAL = r'!='
t_ADD = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_EQUALS = r'\='

#literals
t_INT_LITERAL = r'[-]?[0-9]+'
t_FLOAT_LITERAL = r'[-]?[\d]+\.[\d]+'
def t_BOOL_LITERAL(t): r'true|false'; return t
t_STRING_LITERAL = r'\"([^\\\n]|(\\(.|\n)))*?\"|\'([^\\\n]|(\\(.|\n)))*?\'' #r'^[\'|\"]\w+[\'|\"]$'

#punctuation
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_CURLY_BRACKET = r'{'
t_RIGHT_CURLY_BRACKET = r'}'
t_SEMICOLON = r';'

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t

# ignore
t_ignore=' \t\r\f\v'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Lexer error: Illegal character '",t.value[0],"' at line",t.lineno)
    t.lexer.skip(1)


def p_program(t):
    '''program : STATIC VOID MAIN block'''
    if Errors == 0:
        print('Correct :)')

def p_block(t):
    '''block :  LEFT_CURLY_BRACKET expressions RIGHT_CURLY_BRACKET'''

def p_expressions(t):
    '''expressions : expression
                   | expression expressions '''

def p_expression(t):
    '''expression : read_expression SEMICOLON
                  | write_expression SEMICOLON
                  | RETURN arithmetic_expression SEMICOLON
                  | RETURN bool_expression SEMICOLON
                  | assign_expression SEMICOLON
                  | if_expression
                  | while_expression'''

def p_while_expression(t):
    '''while_expression : WHILE LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block'''

def p_if_expression(t):
    '''if_expression : start_if
                     | start_if else_expression'''

def p_start_if(t):
    '''start_if : IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block'''

def p_else_expression(t):
    '''else_expression : ELSE IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block else_expression
                       | ELSE block'''

def p_read_expression(t):
    '''read_expression : READ'''

def p_write_expression(t):
    '''write_expression : WRITE LEFT_PARENTHESIS string_literals RIGHT_PARENTHESIS'''

def p_arithmetic_datatypes(t):
    '''arithmetic_datatypes : INT
                            | FLOAT'''

def p_bool_datatypes(t):
    '''bool_datatypes : BOOL'''

def p_string_datatypes(t):
    '''string_datatypes : STRING'''

def p_assign_expression(t):
    '''assign_expression : CONST aux_assign_expression
                         | aux_assign_expression
                         | declaration_expression
                         | aux2_assign_expression'''

def p_aux_assign_expression(t):
    '''aux_assign_expression : arithmetic_datatypes ID EQUALS arithmetic_expression
              | bool_datatypes ID EQUALS bool_expression
              | string_datatypes ID EQUALS string_expression'''

def p_aux2_assign_expression(t):
    '''aux2_assign_expression : ID EQUALS arithmetic_expression
              | ID EQUALS bool_expression
              | ID EQUALS string_expression'''

def p_declaration_expression(t):
    '''declaration_expression : arithmetic_datatypes ID
              | bool_datatypes ID
              | string_datatypes ID'''

precedence = (
     ('left', 'ADD', 'MINUS'),
     ('left', 'MULTIPLICATION', 'DIVISION'),
 )

def p_arithmetic_expression(t):
    '''arithmetic_expression : arithmetic_literals ADD arithmetic_expression
                             | arithmetic_literals MINUS arithmetic_expression
                             | arithmetic_literals MULTIPLICATION arithmetic_expression
                             | arithmetic_literals DIVISION arithmetic_expression
                             | arithmetic_literals '''

def p_arithmetic_literals(t):
    '''arithmetic_literals : INT_LITERAL
                           | FLOAT_LITERAL
                           | ID'''

def p_string_literals(t):
    '''string_literals : STRING_LITERAL
                       | ID'''
def p_bool_expression(t):
    '''bool_expression : BOOL_LITERAL AND bool_expression
                         | BOOL_LITERAL OR bool_expression
                         | BOOL_LITERAL'''

def p_string_expression(t):
    '''string_expression : STRING_LITERAL'''

def p_condition(t):
    '''condition : arithmetic_expression GT arithmetic_expression
                   | arithmetic_expression LT arithmetic_expression
                   | arithmetic_expression GET arithmetic_expression
                   | arithmetic_expression LET arithmetic_expression
                   | arithmetic_expression IS_EQUAL arithmetic_expression
                   | arithmetic_expression IS_NOT_EQUAL arithmetic_expression
                   | BOOL_LITERAL IS_EQUAL BOOL_LITERAL
                   | BOOL_LITERAL IS_NOT_EQUAL BOOL_LITERAL'''

# https://stackoverflow.com/questions/24627928/ply-lex-yacc-errors-handling
def p_error(t):
    global Errors
    Errors = Errors + 1
    if t is not None:
        print("Syntax error at %s line: %s"%(t.value, t.lineno ))
        parser.errok()
    else:
        print("Unexpected end of input")


Errors = 0
import ply.lex as lex
import ply.yacc as yacc
parser = yacc.yacc(method="SLR")
lexer = lex.lex()

def _process(s):
    lex.input(s)
    while True:
        tok = lex.token()
        if not tok:
            break
        par = parser.parse(s)

if(len(sys.argv) < 2):
    aux_s = ''
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        if "/*" in s or aux_s:
            aux_s = aux_s +s
            if "*/" in s:
                _process(aux_s)
                aux_s=''
        else:
            _process(s)


else:
    Errors = 0
    file = open(sys.argv[1], "r")
    _process(file.read())
