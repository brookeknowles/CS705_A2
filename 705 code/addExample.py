#!/usr/bin/env python3
from z3 import Solver, sat, And, Consts


def add():
    # Importing the Real type, to simulate floats
    from z3 import RealSort
    s = Solver()

    # Declaring variables as Reals
    i, o1, o2, outl, outr = Consts('i o1 o2 outl outr', RealSort())
    # Make add3_func_ssa format
    s.add(And(o1 == i, o2 == (o1 + i), outl == (o2 + i)))

    # Make outr
    s.add(outr == (i + (i + i)))


    # Add the equivalence statement
    s.add(outl != outr)
    if s.check() == sat:
        print('Codes not equivalent, example:')
        print(s.model())
    else:
        print('Codes are equivalent')


if __name__ == '__main__':
    add()
