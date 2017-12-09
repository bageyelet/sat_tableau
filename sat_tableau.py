from ast import *

def all_atomic(formulae):
    ris = True
    for f in formulae:
        ris = ris and f.isAtomic()
    return ris

def consistent(formulae):
    neg_f = set()
    pos_f = set()
    for f in formulae:
        if isinstance(f, FFalse):
            return False
        if isinstance(f, NotClass):
            if isinstance(f._e, TTrue):
                return False
            neg_f.add(f._e)
        else:
            pos_f.add(f)
    return not bool(pos_f.intersection(neg_f))

def sat(formulae):
    stack = []
    stack.append(formulae)
    while stack:
        node = stack.pop(0)
        if all_atomic(node):
            if consistent(node):
                return True
        else:
            first_formula = node.pop(0)
            if first_formula.isAtomic():
                node.append(first_formula) # put the atom at the end
                stack.append(node)
            elif isinstance(first_formula, AndClass):
                node.append( first_formula._left)
                node.append( first_formula._right)
                stack.append(node)
            elif isinstance(first_formula, OrClass):
                new_node = node[:]
                new_node.append( first_formula._left)
                node.append(     first_formula._right)
                stack.append(node)
                stack.append(new_node)
            elif isinstance(first_formula, ImplyClass):
                new_node = node[:]
                new_node.append(Not(first_formula._left))
                node.append(first_formula._right)
                stack.append(node)
                stack.append(new_node)
            elif isinstance(first_formula, DImplyClass):
                new_node = node[:]
                new_node.append( Not(first_formula._left ))
                new_node.append( Not(first_formula._right))
                node.append(first_formula._left )
                node.append(first_formula._right)
                stack.append(node)
                stack.append(new_node)
            elif isinstance(first_formula, NotClass):
                first_formula = first_formula._e
                if   isinstance(first_formula, AndClass):
                    new_node = node[:]
                    new_node.append( Not(first_formula._left ))
                    node.append(     Not(first_formula._right))
                    stack.append(node)
                    stack.append(new_node)
                elif isinstance(first_formula, OrClass):
                    node.append( Not(first_formula._left ))
                    node.append( Not(first_formula._right))
                    stack.append(node)
                elif isinstance(first_formula, ImplyClass):
                    node.append(     first_formula._left  )
                    node.append( Not(first_formula._right))
                    stack.append(node)
                elif isinstance(first_formula, DImplyClass):
                    new_node = node[:]
                    new_node.append( Not(first_formula._left ))
                    new_node.append(     first_formula._right )
                    node.append(         first_formula._left )
                    node.append(     Not(first_formula._right))
                    stack.append(node)
                    stack.append(new_node)
                elif isinstance(first_formula, NotClass):
                    node.append(first_formula._e)
                    stack.append(node)
                else:
                    raise Exception("malformed formula")
            else:
                raise Exception("malformed formula")
    return False