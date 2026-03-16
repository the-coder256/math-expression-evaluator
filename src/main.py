import sys
import tokeniser
import parser
import evaluator

if len(sys.argv) < 2:
    print("No mathematical expression given!")
    print("Try 'py main.py " + '"<math_expression>"' + "'")
    exit(1)

math_expr = sys.argv[1]
tokens = tokeniser.Tokeniser().tokenise(math_expr)
tree = parser.Parser().parse(tokens)
result = evaluator.Evaluator().evaluate(tree)

print(result)