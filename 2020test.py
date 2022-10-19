#!/usr/bin/env python3
from z3 import Function, Solver, Consts, And, Ints
from z3 import Exists, DeclareSort, ForAll


def q2():
    # Consider the following puzzle.
    # Spend exactly 100 dollars and buy exactly 100 animals.
    # Dogs cost 15 dollars, cats cost 1 dollar, and mice cost 25 cents each.
    # You have to buy at least one of each. How many of each should you buy?

    s = Solver()
    # Create 3 integer variables
    dog, cat, mouse = Ints('dog cat mouse')
    s.check(dog >= 1,    # at least one dog
            cat >= 1,    # at least one cat
            mouse >= 1,  # at least one mouse
            # we want to buy 100 animals
            dog + cat + mouse == 100,
            # We have 100 dollars (10000 cents):
            #   dogs cost 15 dollars (1500 cents),
            #   cats cost 1 dollar (100 cents), and
            #   mice cost 25 cents
            1500 * dog + 100 * cat + 25 * mouse == 10000)
    print(s.model())


def q1():
    """Write this in latex without the model and python Given f an
    uninterpreted function with signature int f(int x), and
    variables x and y of type int.

    Which of the answers below, for the definition of function f,
    satisfy the constraint f(f(x)) == x ∧ f(x) == y ∧ x != y

    A.) int f(int x) {return (x == 1) ? 0 : 1;}
    B.) int f(int x) {return (x == 0) ? 1 : 0;}
    C.) int f(int x) {return 0;}
    D.) int f(int x) {return 1;}

    """
    T = DeclareSort('T')
    x, y = Consts('x y', T)
    f = Function('f', T, T)

    s = Solver()
    s.add(Exists([x, y], And(f(f(x)) == x, f(x) == y, x != y)))
    s.check()
    print(s.model()[f])


if __name__ == '__main__':
    q1()
    q2()
