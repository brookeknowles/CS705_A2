#!/usr/bin/env python3
from z3 import Solver, Consts, And, Not, Or, sat, BoolSort

# Must determine if the following boolean equations are equivilent 
# 1). Y = (¬A /\ B /\ C) \/ (A /\ ¬B /\ C) \/ (A /\ B /\ ¬C) \/ (A /\ B /\ C)
# 2). Y' = (A /\ B) \/ (B /\ C) \/ (A /\ C) – (2)

def encode(Y1, Y2, A, B, C, s):
    """ Encode the boolean logic into the Z3 solver """
    # Equation (1) is Y1
    s.add(Y1 == Or(And(Not(A), B, C), 
                    And(A, Not(B), C),
                    And(A, B, Not(C)),
                    And(A, B, C)
                    )) 

    # Equation (2) is Y2
    s.add(Y2 == Or(And(A, B), 
                    And(B, C), 
                    And(A, C)
                    )) 

def main():
    s = Solver()            # Initialising the solver
    
    A, B, C = Consts('A, B, C', BoolSort())

    ret = s.check()

    # check if returned values satisfy the constraints
    if ret == sat:
        print("Equations 1 and 2 are equivilent!")
    else:
        print("Equations 1 and 2 are not equivilent!")
        print(s.model())


if __name__ == '__main__':
    main()
