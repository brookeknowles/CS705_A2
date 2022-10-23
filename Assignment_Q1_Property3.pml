bool turn, flag[2];
bool waitingProccess;    // will only be true in critical section

ltl {[]<> waitingProccess} // property 3 (liveness)

active[2] proctype P1(){ // active creates instances of processes, [2] means 2 proccesses 
    assert (_pid == 0 || _pid == 1); // make sure that there are only 2 proccesses, and that their identifiers are 0 and 1
again:
    flag[_pid] = 1;
    turn = 1 - _pid;
    (flag[1 - _pid] == 0 || turn == _pid);

    waitingProccess = true;
    // Critical section
    // Checks for property 3 - any process not in the critical section will eventually enter the critical
    waitingProccess = false;    

    flag[_pid] = 0;
    goto again;
}
