#
# def p_statement_expr(t):
#     'statement : expression'
#     print('', end = '')
#
#
# def p_expression_binop(t):
#     '''expression : INT_LITERAL ADD INT_LITERAL
#                   | expression MINUS expression
#                   | expression MULTIPLICATION expression
#                   | expression DIVISION expression'''
#
# def p_accept(t):
#     '''expression : PUBLIC
#                 | PRIVATE
#                 | CONST
#                 | IF
#                 | ELSE
#                 | READ
#                 | RETURN
#                 | VAR
#                 | WHILE
#                 | WRITE
#                 | GT
#                 | LT
#                 | GET
#                 | LET
#                 | AND
#                 | OR
#                 | NOT
#                 | EQUALS
#                 | IS_NOT_EQUAL
#                 | ADD
#                 | MINUS
#                 | MULTIPLICATION
#                 | DIVISION
#                 | IS_EQUAL
#                 | INT
#                 | FLOAT
#                 | BOOL
#                 | STRING
#                 | FLOAT_LITERAL
#                 | BOOL_LITERAL
#                 | STRING_LITERAL
#                 | LEFT_PARENTHESIS
#                 | RIGHT_PARENTHESIS
#                 | LEFT_CURLY_BRACKET
#                 | RIGHT_CURLY_BRACKET
#                 | COMMA
#                 | SEMICOLON
#                 | SPACE
#                 | TAB
#                 | NEW_LINE
#                 | ONE_LINE_COMMENT
#                 | MULTIPLE_LINE_COMMENT
#                 | DOUBLE_QUOTE
#                 | QUOTE
#                 | ID
#                 '''
#     print('', end = '')
#
# def p_error(t):
#     if (t):
#             print('', end = '')
#             #print("Syntax error at '%s'" % t.value)
#
#
#
# import ply.yacc as yacc
# parser = yacc.yacc()
#
#
# while True:
#     try:
#         s = input('> ')   # Use raw_input on Python 2
#     except EOFError:
#         break
#     parser.parse(s)
