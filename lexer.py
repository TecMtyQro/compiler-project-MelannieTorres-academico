import fileinput
import sys
#https://www.dabeaz.com/ply/PLYTalk.pdf

tokens = (
    #reserved words
    'PUBLIC', 'PRIVATE',
    'CONST','IF', 'ELSE','READ', 'RETURN',
    'VAR','WHILE','WRITE',
    #operatoris
    'IS_EQUAL','IS_NOT_EQUAL', 'GT', 'LT', 'GET', 'LET',
    'AND', 'OR', 'NOT', 'EQUALS',
    'ADD','MINUS', 'MULTIPLICATION', 'DIVISION',
    #data types
    'INT', 'FLOAT', 'BOOL', 'STRING',
    #literals
    'INT_LITERAL', 'FLOAT_LITERAL', 'BOOL_LITERAL', 'STRING_LITERAL',
    #punctuation
    'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', 'LEFT_CURLY_BRACKET',
    'RIGHT_CURLY_BRACKET', 'LEFT_SQUARE_BRACKET', 'RIGHT_SQUARE_BRACKET',
    'COMMA', 'SEMICOLON', 'DOT',
    'DOUBLE_QUOTE', 'QUOTE',
    #whitespace
    'SPACE', 'TAB', 'NEW_LINE',
    #comment
    'ONE_LINE_COMMENT', 'MULTIPLE_LINE_COMMENT',
    #id
    'ID'
)
#tokens

#reserved words
t_PUBLIC = r'public'
t_PRIVATE = r'private'
t_CONST = r'const'
t_IF = r'if'
t_ELSE = r'else'
t_READ = r'Console\.Read'
t_RETURN = r'return'
t_VAR = r'var'
t_WHILE = r'while'
t_WRITE = r'Console\.Write'

#operators
t_GT = r'>'
t_LT = r'<'
t_GET = r'>='
t_LET = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQUALS = r'=='
t_IS_NOT_EQUAL = r'!='
t_ADD = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_IS_EQUAL = r'\='

#data types
t_INT = r'int'
t_FLOAT = r'float'
t_BOOL = r'bool'
t_STRING = r'string'

#literals
t_INT_LITERAL = r'[-]?[0-9]+'
t_FLOAT_LITERAL = r'[-]?[\d]+\.[\d]+'
t_BOOL_LITERAL = r'true|false'
t_STRING_LITERAL = r'\"([^\\\n]|(\\(.|\n)))*?\"|\'([^\\\n]|(\\(.|\n)))*?\'' #r'^[\'|\"]\w+[\'|\"]$'

#punctuation
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_CURLY_BRACKET = r'{'
t_RIGHT_CURLY_BRACKET = r'}'
t_LEFT_SQUARE_BRACKET = r'\['
t_RIGHT_SQUARE_BRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'
t_DOUBLE_QUOTE = r'"'
t_QUOTE = r"'"

#whitespace
# t_SPACE = r'\\s'
# t_TAB = r'\\t'
# t_NEW_LINE = r'\\n'

#comment
t_ONE_LINE_COMMENT = r'^(?:[^"/\\]|\"(?:[^\"\\]|\\.)*\"|/(?:[^/"\\]|\\.)|/\"(?:[^\"\\]|\\.)*\"|\\.)*//(.*)$' # regex by python https://stackoverflow.com/questions/15423658/regular-expression-for-single-line-comments
t_MULTIPLE_LINE_COMMENT = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/' # r'(/\*(.|\n)*?\*/)'

#id
t_ID = r'[a-zA-Z]\w*'

# ignore
t_ignore=' \t\r\n\f\v'


def t_error(t):
    print("Lexer error: Illegal character '",t.value[0],"' at line",t.lineno)
    # t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

if(len(sys.argv) > 1):
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        lex.input(s)
        while True:
            tok = lex.token()
            if tok:
                print(tok)
            else:
                break

else:
    file_input = fileinput.input()
    for s in file_input:
        lex.input(s)
        while True:
            tok = lex.token()
            if tok:
                print(tok)
            else:
                break
