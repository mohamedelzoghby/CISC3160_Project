#Simple Lexer to be used for the toy langague

import ply.lex as lex
 
 # List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LETTER',
    'EQUAL'
 )
 
 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_EQUAL   = r'='
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
 
 # A regular expression rule with some action code
def t_LETTER(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.value = str(t.value)    
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
 # Build the lexer
lexer = lex.lex()

 # Test it out

userInput = input("Enter a String \n")
type (userInput)

  # Give the lexer some input
lexer.input(userInput)
 
 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print (tok)
print (userInput)


