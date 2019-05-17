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
    t[0] = t[1:]

def p_block(t):
    '''block :  LEFT_CURLY_BRACKET expressions RIGHT_CURLY_BRACKET'''
    t[0] = t[1:]

def p_expressions(t):
    '''expressions : expression
                   | expression expressions '''
    t[0] = t[1:]


def p_expression(t):
    '''expression : read_expression SEMICOLON
                  | write_expression SEMICOLON
                  | RETURN arithmetic_expression SEMICOLON
                  | RETURN bool_expression SEMICOLON
                  | assign_expression SEMICOLON
                  | if_expression
                  | while_expression'''
    t[0] = t[1:]


def p_while_expression(t):
    '''while_expression : WHILE LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block'''
    t[0] = t[1:]

def p_if_expression(t):
    '''if_expression : start_if
                     | start_if else_expression'''
    t[0] = t[1:]

def p_start_if(t):
    '''start_if : IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block'''
    t[0] = t[1:]

def p_else_expression(t):
    '''else_expression : ELSE IF LEFT_PARENTHESIS condition RIGHT_PARENTHESIS block else_expression
                       | ELSE block'''
    t[0] = t[1:]

def p_read_expression(t):
    '''read_expression : READ'''
    t[0] = t[1:]

def p_write_expression(t):
    '''write_expression : WRITE LEFT_PARENTHESIS string_literals RIGHT_PARENTHESIS'''
    t[0] = t[1:]

def p_arithmetic_datatypes(t):
    '''arithmetic_datatypes : INT
                            | FLOAT'''
    t[0] = t[1:]

def p_bool_datatypes(t):
    '''bool_datatypes : BOOL'''
    t[0] = t[1:]

def p_string_datatypes(t):
    '''string_datatypes : STRING'''
    t[0] = t[1:]

def p_assign_expression(t):
    '''assign_expression : CONST aux_assign_expression
                         | aux_assign_expression
                         | declaration_expression
                         | aux2_assign_expression'''
    t[0] = t[1:]
    if t[0][0] == 'const':
        mark_as_const_in_stack(t[0][1][1], t[0][1][0], t[0][1][3])


def p_aux_assign_expression(t):
    '''aux_assign_expression : arithmetic_datatypes ID EQUALS arithmetic_expression
              | bool_datatypes ID EQUALS bool_expression
              | string_datatypes ID EQUALS string_expression'''
    add_var_to_stack(t[2], t[4], t[1][0], False)
    t[0] = t[1:]

def p_aux2_assign_expression(t):
    '''aux2_assign_expression : ID EQUALS arithmetic_expression
              | ID EQUALS bool_expression
              | ID EQUALS string_expression'''
    t[0] = t[1:]
    var = update_variable_in_stack(t[1], t[3])


def p_declaration_expression(t):
    '''declaration_expression : arithmetic_datatypes ID
              | bool_datatypes ID
              | string_datatypes ID'''
    add_var_to_stack(t[2], None, t[1][0], False)
    t[0] = t[1:]


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


    if type(t[1]) is list:
        t[1]=t[1][0]

    if len(t)>2:
        if type(t[3]) is list:
            t[3]=t[3][0]

        if t[2] == '+':
            t[0] = num(t[1])+num(t[3])
        elif t[2] == '-':
            t[0] = num(t[1])-num(t[3])
        elif t[2] == '*':
            t[0] = num(t[1])*num(t[3])
        elif t[2] == '/':
            t[0] = num(t[1])/num(t[3])
    else:
        t[0] = t[1]

    t[0] = [t[0], 'float']




def p_arithmetic_literals(t):
    '''arithmetic_literals : INT_LITERAL
                           | FLOAT_LITERAL
                           | ID'''
    t[0] = t[1:]

def p_string_literals(t):
    '''string_literals : STRING_LITERAL
                       | ID'''
    t[0] = t[1:]

def p_bool_expression(t):
    '''bool_expression : BOOL_LITERAL AND bool_expression
                         | BOOL_LITERAL OR bool_expression
                         | BOOL_LITERAL'''
    t[0] = t[1:]
    t[0] = [t[0], 'bool']


def p_string_expression(t):
    '''string_expression : STRING_LITERAL'''


    t[0] = [t[0], 'string']


def p_condition(t):
    '''condition : arithmetic_expression GT arithmetic_expression
                   | arithmetic_expression LT arithmetic_expression
                   | arithmetic_expression GET arithmetic_expression
                   | arithmetic_expression LET arithmetic_expression
                   | arithmetic_expression IS_EQUAL arithmetic_expression
                   | arithmetic_expression IS_NOT_EQUAL arithmetic_expression
                   | BOOL_LITERAL IS_EQUAL BOOL_LITERAL
                   | BOOL_LITERAL IS_NOT_EQUAL BOOL_LITERAL'''
    if t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '==':
        t[0] = t[1] <= t[3]
    elif t[2] == '!=':
        t[0] = t[1] <= t[3]
    else:
        t[0] = t[1:]


# https://stackoverflow.com/questions/24627928/ply-lex-yacc-errors-handling
def p_error(t):
    global Errors
    Errors = Errors + 1
    if t is not None:
        print("Syntax error at %s line: %s"%(t.value, t.lineno ))
        parser.errok()
    else:
        print("Unexpected end of input")


def resulting_type(type_1, type_2):
    if type_1 == type_2:
        return type_1
    elif (type_1 == 'float' and type_2 == 'int') or (type_1 == 'int' and type_2 == 'float'):
        return 'float'
    elif (type_1 == 'bool' and type_2=='int' and (type_2 == 0 or type_2 ==1)):
        return 'bool'
    else:
        raise Exception('Mismatch type operations: %s and %s' % (type_1, type_2))

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def add_var_to_stack(var_name, var_value, var_type, is_const):
    if (find_in_variables_stack(var_name) is not None):
        raise Exception('Var: %s is being redeclared' % (var_name))
    if is_const:
        new_var=[var_type, var_name, var_value, 'const']
    elif(var_value):
        new_var=[var_type, var_name, var_value[0]]
    else:
        new_var=[var_type, var_name]
    variables.append(new_var)

def find_in_variables_stack(var_name):
    for var in variables:
        if var[1] == var_name:
            return var

def update_variable_in_stack(var_name, new_value):
    if (find_in_variables_stack(var_name)==None):
        raise Exception('Var: %s wasnt previously declared' % (var_name))
    for var in variables:
        if var[1] == var_name:
            if len(var)>4 and var[4] == 'const':
                raise Exception('Trying to modify a const: %s' % (var[1]))
            else:
                new_type = resulting_type(var[0], new_value[1]) #type checking
                var[0] = new_type
                var[2] = new_value[0]

def mark_as_const_in_stack(var_name, var_value, var_type):
    if (find_in_variables_stack(var_name)==None):
        # print('curernt',Current_block)
        add_var_to_stack(var_name, var_value, var_type, True)
    else:
        for var in variables:
            if var[1] == var_name:
                var.append('const')

# def code_generation():
#     with open("code.py", "w") as f:
#         f.write(New_tree)
#
# def scope(tree):
#     blockId = 0
#     flag = 0
#     print(tree)
#     for child in tree:
#         if flag == 1:
#             print(child)
#             flag = 0
#         if isinstance(child, str):
#             if child is 'int' or child is 'float'  or child is 'string' or child is 'bool':
#                 print('declaration1')
#                 flag = 1
#
#         else:
#             recursive_scope(child, blockId)
#
# def recursive_scope(tree, blockId, flag = 0):
#     # flag = 0
#     blockId = blockId + 1
#     if tree is not 'int' and tree is not 'float'  and tree is not 'string' and tree is not 'bool' and  not isinstance(tree, bool):
#         for i in range(len(tree)):
#             if flag == 1:
#                 print(tree[i])
#                 flag = 0
#             if (isinstance(tree[i], str) or isinstance(tree[i], int) or isinstance(tree[i], float)) and i == 0 :
#                 # print(i)
#                 if tree[i] is 'int' or tree[i] is 'float'  or tree[i] is 'string' or tree[i] is 'bool':
#                     print('declaration')
#                     flag = 1
#                     print(tree[i])
#                     print(tree[i+1])
#             else:
#                 recursive_scope(tree[i], blockId)
Errors = 0
import ply.lex as lex
import ply.yacc as yacc


parser = yacc.yacc(method="SLR")
lexer = lex.lex()
variables = []

def _process(s):
    lex.input(s)
    while True:
        tok = lex.token()
        if not tok:
            break
        par = parser.parse(s)
        print(variables)


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
