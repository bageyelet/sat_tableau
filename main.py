from parser import *
from ast import *
from sat_tableau import *

if __name__=="__main__":
    p = Parser()
    while 1:
        s = raw_input("> ")
        p.setString(s)
        try:
            exp = p.parse()
        except:
            print "> !syntax error"
            continue
        if sat([exp]):
            print "> SAT"
        else:
            print "> UNSAT"