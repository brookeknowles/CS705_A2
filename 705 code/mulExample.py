#!/usr/bin/env python3
# The standard imports
from z3 import Solver, sat, And, Consts


def mul():
    # Importing the type Int
    from z3 import IntSort      # IntSort is typedef for Int type 
    s = Solver()                # Importing the solver
    # Declaring the variables we need
    i, o1, o2, outl, outr = Consts('i o1 o2 outl outr', IntSort())
    # Encode outl
    s.add(And(o1 == i, o2 == (o1 * i), outl == (o2 * i)))

    # Encode outr
    s.add(outr == (i * (i * i)))

    # Encode the condition that there exists no i, such that outl !=
    # outr
    s.add(outl != outr)

    if s.check() == sat:
        print('Codes not equivalent, example:')
        print(s.model())
    else:
        print('Codes are equivalent')


if __name__ == '__main__':
    mul()
