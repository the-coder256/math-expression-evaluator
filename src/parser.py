import evaluator

operations = ["Add", "Sub", "Mul", "Div"]

class Node_Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Node_Sub:
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Node_Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Node_Div:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Parser:
    def __init__(self):
        self.index = 0
        self.tokens = []
        self.tree = ""
    
    def getType(self, ast):
        return evaluator.Evaluator().getType(ast)

    def peek(self, amount = 1):
        if self.index + amount >= len(self.tokens):
            return ""
        else:
            return self.tokens[self.index + amount]
    
    def consume(self):
        return self.tokens[self.index]
    
    def advance(self):
        self.index += 1
        return self.tokens[self.index - 1]

    def check(self, left, right):
        try:
            x = float(left)
        except:
            print("Invalid expression", flush = True)
            exit(1)
        
        try:
            x = float(right)
        except:
            print("Invalid expression", flush = True)
            exit(1)

    def parseMulDiv(self):
        left = self.advance()
        operation = self.advance()
        right = self.consume()

        if operation == "*":
            self.check(left, right)
            return Node_Mul(left, right)
        elif operation == "/":
            self.check(left, right)
            return Node_Div(left, right)

    def parseTerm(self):
        left = self.advance()
        operator = self.advance()
        right = self.consume()

        if operator == "+":
            self.check(left, right)

            if self.peek() == "*" or self.peek() == "/":
                return Node_Add(left, self.parseMulDiv())
            else:
                return Node_Add(left, right)
        elif operator == "-":
            self.check(left, right)

            if self.peek() == "*" or self.peek() == "/":
                return Node_Sub(left, self.parseMulDiv())
            else:
                return Node_Sub(left, right)
        if operator == "*":
            self.check(left, right)
            return Node_Mul(left, right)
        elif operator == "/":
            self.check(left, right)
            return Node_Div(left, right)

    def atEnd(self):
        return self.peek() == "END"

    def parse(self, tokensToParse):
        self.tokens = tokensToParse

        while not self.atEnd():
            node = self.parseTerm()

            if self.tree == "":
                self.tree = node
            else:
                if self.getType(node) == "Add":
                    if self.getType(node.right) in operations:
                        self.tree = Node_Add(self.tree, node.right)
                    else:
                        self.tree = Node_Add(self.tree, self.consume())
                elif self.getType(node) == "Sub":
                    if self.getType(node.right) in operations:
                        self.tree = Node_Sub(self.tree, node.right)
                    else:
                        self.tree = Node_Sub(self.tree, self.consume())
                elif self.getType(node) == "Mul":
                    self.tree = Node_Mul(self.tree, self.consume())
                elif self.getType(node) == "Div":
                    self.tree = Node_Div(self.tree, self.consume())

        return self.tree