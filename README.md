# CS705_A2

This was an assignment I did for a university class on formal methods for safety critical software. 

### Q1: Model-checking LTL properties on concurrent processes.

#### Part-A
Model Petersons mutual exclusion algorithm in Promela.

#### Part-B
Represent the following properties in LTL and verify them against at least 2 processes from above.
- Property-1 (Safety property): Multiple processes cannot enter the ciritical section together.
- Property-2 (Liveness property): If a process is waiting, eventually it will enter the critical section.
- Property-3 (Liveness property): Any process not in the critical section will eventually enter the critical section.

### Q2: Using SMT solvers for hardware verification.
Majority voter is a protocol used in fault tolerant systems. Consider 3-processors A, B, and C, carrying
out the same computation simultaneously. Any of these processors might suffer from transient faults
during processing. In the majority voter protocol, an output Y is set depending upon the majority
result produced from the processors. The truth table below describes the majority voter protocol:

| A | B | C | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

The boolean equation:
`Y = (¬A /\ B /\ C) \/ (A /\ ¬B /\ C) \/ (A /\ B /\ ¬C) \/ (A /\ B /\ C)` gives the functional description of the truth-table above. 

A hardware engineer states that he/she will implement the above circuit using the equation below: 

`Y' = (A /\ B) \/ (B /\ C) \/ (A /\ C)`

Prove using the SMT solver that Equations (1) and (2) are equivalent. If they are not, show why not?
