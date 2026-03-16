class Node_Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Parser:
    def __init__(self):
        self.index = 0
        self.tokens = []
        self.tree = ""
    
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

    def parseTerm(self):
        left = self.advance()
        operator = self.advance()
        right = self.consume()

        if operator == "+":
            self.check(left, right)
            return Node_Add(left, right)


    def atEnd(self):
        return self.peek() == "END"

    def parse(self, tokensToParse):
        self.tokens = tokensToParse

        while not self.atEnd():
            node = self.parseTerm()

            if self.tree == "":
                self.tree = node
            else:
                if self.peek(-1) == "+":
                    self.tree = Node_Add(self.tree, self.consume())

        return self.tree