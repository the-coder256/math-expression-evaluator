class Tokeniser:
    def __init__(self):
        self.currentToken = ""
        self.expr = ""
        self.tokens = []

    def tokenise(self, math_expr):
        self.expr = math_expr
        
        for char in math_expr:
            if char == " ":
                continue
            elif char == "+":
                self.tokens.append(self.currentToken)
                self.tokens.append(char)
                self.currentToken = ""
            elif char == "-":
                self.tokens.append(self.currentToken)
                self.tokens.append(char)
                self.currentToken = ""
            else:
                self.currentToken += char
        
        if self.currentToken != "":
            self.tokens.append(self.currentToken)
        
        self.tokens.append("END")

        return self.tokens