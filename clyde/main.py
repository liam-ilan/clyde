import lex
import parse
import sys

code = open(sys.argv[1] if len(sys.argv) > 1 else "main.clyde", "r").read()
tokens = lex.lex(code)
tree = parse.parse(tokens)
runtime = tree.runtime()

runtime.run()