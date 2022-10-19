#!/usr/bin/env python3

# Using the z3 SMT solver with python3 bindings
from z3 import IntSort, Solver, sat, And, Consts
# Importing the datatype Int, the Solver class, and the 'sat' variable.
# Finally, the And (logical And class)

def main():
        # Declaring and defining the two variables.
        x, y = Consts('x y', IntSort())  # IntSort just stands for Int (type)

        s = Solver()                # Initialising the solver

        # Adding the equations into the solver
        s.add(And(x + y >= 10, x - y >= 20))

        # Show the state of the solver
        print('Solver state: %s' % s)                    # Just for debugging

        # Solving for all free variables: x and y
        ret = s.check()

        # Check if there is some assignment for x and y
        # that satisfy the equations
        if ret == sat:
                print('Result:')
                print('x: %s' % s.model()[x])
                print('y: %s' % s.model()[y])


# Calling the main function in python
if __name__ == '__main__':
        main()
