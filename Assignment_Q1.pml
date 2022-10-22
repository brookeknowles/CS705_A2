// Just the two process peterson algorithm

bool turn, flag[2];
byte numCriticalProcesses;

active[2] proctype P1(){
    assert (_pid == 0 || _pid == 1);
again:
    flag[_pid] = 1;
    turn = 1 - _pid;
    (flag[1 - _pid] == 0 || turn == _pid);

    numCriticalProcesses++;
    assert(numCriticalProcesses == 1)   // Critical section
    numCriticalProcesses++;

    flag[_pid] = 0;
    goto again; 
}

