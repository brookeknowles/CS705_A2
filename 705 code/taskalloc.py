from z3 import Solver, sat, Or, If, Real 


def reduce(sV, Ej):
    def max(x, y):
        return If(x > y, x, y)

    if len(Ej) == 0:
        return sV
    else:
        # Return the max from first and rest
        return max(Ej[0], reduce(sV, Ej[1:]))


def main(P, T, X):
    """P is the number of processors
    T is the number of tasks
    X is the execution time of each task on any processor
    """
    assert(X >= 0)

    # Initialise the solver
    s = Solver()

    # Making the 1/0 Reals 
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
    ret = s.check()
    if ret == sat:
        model = s.model()

        # The makespan
        print('Result makespan %s\n' % (model[makespan]))

        # The allocations
        print('Allocations: \n')
        for i in range(T):
            row = [str(model[Iijs[i][j]]) for j in range(P)]
            print('\t'.join(row))
    else:
        print('No satisfaction found. No model!')


if __name__ == '__main__':
    P = 4
    T = 5 
    X = 100
    main(P, T, X)
