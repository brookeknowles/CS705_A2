#!/usr/bin/env python3
from z3 import Solver, sat, And, Consts


def general():
    from z3 import Function, ForAll, DeclareSort

    # Declaring the new type T
    T = DeclareSort('T')        # A new Type "T"

    s = Solver()

    # Declaring the variables we need for type T
    i, o1, o2, outl, outr = Consts('i o1 o2 outl outr', T)

    # Declaring the new function "f" of type signature: (T, T) -> T
    f = Function('f', T, T, T)

    # Adding the commutativity constraint
    x, y = Consts('x y', T)
    s.add(ForAll([x, y], f(x, y) == f(y, x)))

    # Make outl, replacing the operator with f everywhere
    s.add(And(o1 == i, o2 == f(o1, i), outl == f(o2, i)))

    # Make outr, replacing the operators with f everywhere
    s.add(outr == f(i, f(i, i)))

    s.add(outl != outr)

    # Print what is in the solver
    print('Solver state: %s' % s)
    print('\n')

    if s.check() == sat:
        # Print the model if something is wrong
        print('Codes not equivalent, example trace:')
        print(s.model())
    else:
        # Else everything is A OK!
        print('Codes are equivalent')


def main():
    general()


if __name__ == '__main__':
    main()
