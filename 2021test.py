#!/usr/bin/env python3

from z3 import Ints, Solver, sat, Or

# 1. Prove that the swap1 and swap2 functions below return the same swapped values for all
# the same inputs a and b of type int. Encode the equivalence (validation) problem as SMT
# constraints in Z3 Python API. Show the Python code along with the output of running the
# Z3 solver. (15 marks)


# From the question
def swap11(a, b):
    tmp = b
    b = a
    a = tmp
    return a, b

# From the question
def swap22(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# The swap1 function (uncoding)
def swap1(a, b, s):         # input s being the solver defined in q1()
    tmp, ar, br = Ints('tmp ar br')
    s.add(tmp == b)         # tmp can remain same on both sides
    s.add(br == a)          # on LHS of the converted to SSA form, the variable cant be (cont.) 
    s.add(ar == tmp)        # same as left, so change to a1/b1 or ar/br etc.
    return ar, br           # always return the last assignment from LHS (ar, then br)


# The second swap function (uncoding)
def swap2(a, b, s):         # input s being the solver defined in q1()
    tmp2, ar2, br2 = Ints('tmp2 ar2 br2')
    s.add(tmp2 == a + b)
    s.add(br2 == tmp2 - b)
    s.add(ar2 == tmp2 - br2)
    return ar2, br2         # always return the last assignment from LHS (ar2, then br2)


def q1():
    a, b = Ints('a b')
    s = Solver()
    ar1, br1 = swap1(a, b, s)
    ar2, br2 = swap2(a, b, s)
    s.add(Or(ar1 != ar2, br1 != br2)) # counter example
    # print(s)
    ret = s.check()
    if ret == sat:
        print('Codes not equivalent')
        print(s.model())
    else:
        print('Codes equivalent')


# Let x, y,z of some generic type T represent the sides an equilateral triangle. Let an uninterpreted function L with type signature L : T → Int give the length of any side of the equilateral
# triangle. The goal is to prove the conjecture: the sum of the lengths of any two sides of the
# equilateral triangle is greater than the (other) third side. Encode the above goal as SMT
# constraints in Z3 via Python API. Show the Python code along with the output of running
# the Z3 solver. Is the aforementioned conjecture true? (15 marks)

def q2():
    """For an equilateral triangle show that the sum of two sides is always
    greater than any one side.

    """
    from z3 import Function, ForAll, IntSort, Or, DeclareSort, Consts

    # The non numeric type for the sides of the triangle
    T = DeclareSort('T')

    # Declared the variables of type T
    x, y, z, a = Consts('x y z a', T)

    # The solver
    s = Solver()

    # The length function on Int
    L = Function('Length', T, IntSort())
    s.add(ForAll([a], L(a) > 0))

    # Equilateral triangle property -- all side lengths are equal
    s.add(L(x) == L(y), L(y) == L(z), L(z) == L(x))

    # Finally the triangle inequality
    s.add(Or(L(x) + L(y) < L(z), L(y) + L(z) < L(x), L(x) + L(z) < L(y)))
    # print(s)
    ret = s.check()
    if ret == sat:
        print('Triangle inequality violated!')
        print(s.model())
    else:
        print('Triangle inequality is true for equilateral triangles')


if __name__ == '__main__':
    q1()
    q2()

    # DEBUG swap11 and swap22
    # print(swap11(6, 38), swap22(6, 38))
