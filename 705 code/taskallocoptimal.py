from z3 import Solver, sat, Or, If, Real 


def reduce(sV, Ej):
    def max(x, y):
        return If(x > y, x, y)

    if len(Ej) == 0:
        return sV
    else:
        return max(Ej[0], reduce(sV, Ej[1:]))


Iijs = None
def main(P, T, X):
    """P is the number of processors
    T is the number of tasks
    X is the execution time of each task on any processor
    """
    assert(X >= 0)

    # Initialise the solver
    s = Solver()

    # Making the 1/0 Reals 
    global Iijs
    Iijs = [[Real('I_%s_%s' % (i, j)) 
             for j in range(P)] for i in range(T)]

    # Adding the constraint that they can only be 1 or 0
    [s.add(Or(Iijs[i][j] == 1, Iijs[i][j] == 0))
     for i in range(T) for j in range(P)]

    # Now, making sure that the allocation of task is only on one
    # processor.
    [s.add(1 == sum(Iijs[i])) for i in range(T)]

    # Next compute the total execution time for each processor
    Ej = [Real('E_%s' % j) for j in range(P)]

    # Adding the constraint for the total execution time
    for j in range(P):
        V = 0
        for i in range(T):
            V += Iijs[i][j]
        s.add(Ej[j] == V*X)

    # Now the total makespan
    makespan = Real('makespan')
    s.add(makespan == reduce(0, Ej))

    return s, makespan


def binary_search(lb, ub, s, makespan, epsilon=1e-6):
    if (ub - lb <= epsilon):
        global Iijs
        s.check()
        return s.model()[makespan], Iijs, s.model()
    else:
        half = lb + ((ub - lb)/2.0)
        s.push()
        s.add(makespan >= lb, makespan <= half)
        ret = s.check()
        s.pop()
        if ret == sat:
            return binary_search(lb, half, s, makespan, epsilon)
        else:
            return binary_search(half, ub, s, makespan, epsilon)


if __name__ == '__main__':
    P = 4
    T = 5
    X = 100
    s, makespan = main(P, T, X)

    # Now do a binary search for the optimal makespan between lower and
    # upper bounds

    UB = (X*T)
    LB = (UB/P)

    optimal_makespan, Iijs, model = binary_search(LB, UB, s, makespan)
    print('Optimal makespan %s \n' % optimal_makespan)

    # The allocations
    print('Allocations: \n')
    for i in range(T):
        row = [str(model[Iijs[i][j]]) for j in range(P)]
        print('\t'.join(row))
