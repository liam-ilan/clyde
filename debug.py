import lex
import parse

code = open("main.clyde", "r").read()

print("\nCODE:")
print(code)

print("\nTOKENS:")
tokens = lex.lex(code)
for i in tokens:
  print(i)

print("\nTREE:")
tree = parse.parse(tokens)
print(tree) 

print("\nRUNTIME:")
r = tree.runtime()
r.run()