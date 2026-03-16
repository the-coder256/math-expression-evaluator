operations = ["Add"]

class Evaluator:
    def __init__(self):
        self.tree = ""
    
    def getType(self):
        retVal = str(type(self.tree.left))

        if retVal == "<class 'parser.Node_Add'>":
            retVal = "Add"
        
        return retVal

    def num(self, value):
        try:
            x = float(value)

            if x == int(x):
                x = int(x)
            
            return x
        except:
            print("The value given is not good idk")
            return 0

    def evaluateTree(self, ast):   # This is very different to evaluate() trust me bro
        left_t = self.getType()
        right_t = self.getType()
        tree_t = self.getType()

        if left_t in operations:
            final_left = self.evaluateTree(ast.left)
        else:
            final_left = self.num(ast.left)
        
        if right_t in operations:
            final_right = self.evaluateTree(ast.right)
        else:
            final_right = self.num(ast.right)
        
        return final_left + final_right

    def evaluate(self, ast):   # This doesn't evaluate anything but sets up self.tree for other methods to use
        self.tree = ast

        result = self.evaluateTree(self.tree)

        return result