#!/usr/bin/env python3

from z3 import And, Not, Xor, BoolSort, Or, sat
from z3 import Solver, Consts


def functional(sumf, carryf, a, b, c, s):
    s.add(sumf == Or(And(Not(a), Not(b), c),
                     And(Not(a), b, Not(c)),
                     And(a, Not(b), Not(c)),
                     And(a, b, c)))

    s.add(carryf == Or(And(b, c), And(a, c), And(a, b)))


def implementation(Si, Ci, A, B, C, s):
    u, v, w = Consts('u, v, w', BoolSort())
    s.add(u == Xor(A, B))
    s.add(v == And(u, C))
    s.add(w == And(A, B))
    s.add(Si == Xor(u, C))
    s.add(Ci == Or(w, v))


def main():
    A, B, Cin = Consts('A, B, Cin', BoolSort())
    Sf, Cf = Consts('Sf, Cf', BoolSort())
    s = Solver()
    functional(Sf, Cf, A, B, Cin, s)
    Si, Ci = Consts('Si, Ci', BoolSort())
    implementation(Si, Ci, A, B, Cin, s)

    # Now the "mitre" circuit
    s.add(Or(Xor(Sf, Si), Xor(Cf, Ci)))

    # Check if the circuits are equivalent
    if s.check() == sat:
        print('Circuits not equivalent')
        print(s.model())        # print the values of A, B, C, etc.
    else:
        print('Circuits are equivalent')


if __name__ == '__main__':
    main()
