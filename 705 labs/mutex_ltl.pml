bit flag; 
byte mutex; 
ltl {[](mutex != 2)}
proctype P(bit i) {
  flag != 1;
  flag = 1;
  mutex++;
  printf("MSC: P(%d) has entered section.\n", i);
  mutex--;
  flag = 0;
}

init {
  atomic { run P(0); run P(1);}
}