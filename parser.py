from ast import *

class Parser:
    def __init__(self):
        self.string = ""
        self.operators = ["and", "or", "not", "(", ")", "->", "<->"]
        self.constants = ["true", "false"]

    def setString(self, string):
        self.string = ""
        for c in string:
            if c == "(" or c == ")":
                self.string = self.string + " " + c + " "
            else:
                self.string += c

    def parse(self):
        operand_stack  = []
        operator_stack = []

        e = self.string.split()
        e.insert(0, "(")
        e.append(")")

        for el in e:
            if el in self.operators:
                if el != ")":
                    operator_stack.append(el)
                else:
                    op = operator_stack.pop()
                    while op != "(":
                        if op == "not":
                            v = operand_stack.pop()
                            exp = Not(v)
                            operand_stack.append(exp)
                        elif op == "and":
                            v2 = operand_stack.pop()
                            v1 = operand_stack.pop()
                            exp = And(v1, v2)
                            operand_stack.append(exp)
                        elif op == "or":
                            v2 = operand_stack.pop()
                            v1 = operand_stack.pop()
                            exp = Or(v1, v2)
                            operand_stack.append(exp)
                        elif op == "->":
                            v2 = operand_stack.pop()
                            v1 = operand_stack.pop()
                            exp = Imply(v1, v2)
                            operand_stack.append(exp)
                        elif op == "<->":
                            v2 = operand_stack.pop()
                            v1 = operand_stack.pop()
                            exp = DImply(v1, v2)
                            operand_stack.append(exp)
                        else:
                            raise Exception("Wrong operand")
                        op = operator_stack.pop()
            elif el in self.constants:
                if el == "true":
                    operand_stack.append(TTrue())
                else:
                    operand_stack.append(FFalse())
            else:
                operand_stack.append(Var(el))
        return operand_stack.pop()

if __name__=="__main__":
    p = Parser()
    p.setString("not((a or b) -> (a and b))")
    print p.parse()
    p.setString("(not a) or b")
    print p.parse()
    p.setString("((p -> (q and r)) and ((not q) or (not r)) and (not (not p))")
    print p.parse()
    p.setString("true -> false")
    print p.parse()
    p.setString("((not true) and a) or b")
    print p.parse()
