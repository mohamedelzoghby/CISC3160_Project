import sys
try:
  f = open(sys.argv[1])
  p = yacc.parse(f.read())
  print p
  
except EOFError:
  print "Could not open file %s." % sys.argv[1]
