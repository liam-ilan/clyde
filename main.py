import lex
import parse
import sys
from keep_alive import keep_alive

code = open(sys.argv[1] if len(sys.argv) > 1 else "main.clyde", "r").read()
tokens = lex.lex(code)
tree = parse.parse(tokens)
runtime = tree.runtime()

keep_alive()
runtime.run()