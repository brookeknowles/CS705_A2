bool turn, flag[2];
byte numCriticalProcesses; // counter for the number of proccesses currently in critical section

ltl {[](numCriticalProcesses != 2)} // property 1 (safety)

active[2] proctype P1(){ // active creates instances of processes, [2] means 2 proccesses 
    assert (_pid == 0 || _pid == 1); // make sure that there are only 2 proccesses, and that their identifiers are 0 and 1
again:
    flag[_pid] = 1;
    turn = 1 - _pid;
    (flag[1 - _pid] == 0 || turn == _pid);

    numCriticalProcesses++;
    // Critical section
    // Checks for property 1 - multiple proccesses cannot enter the critical section together (i.e. max number of critical proccesses at any one time != 2)
    numCriticalProcesses--;

    flag[_pid] = 0;
    goto again;
}
