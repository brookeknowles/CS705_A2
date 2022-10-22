#define rand	pan_rand
#define pthread_equal(a,b)	((a)==(b))
#if defined(HAS_CODE) && defined(VERBOSE)
	#ifdef BFS_PAR
		bfs_printf("Pr: %d Tr: %d\n", II, t->forw);
	#else
		cpu_printf("Pr: %d Tr: %d\n", II, t->forw);
	#endif
#endif
	switch (t->forw) {
	default: Uerror("bad forward move");
	case 0:	/* if without executable clauses */
		continue;
	case 1: /* generic 'goto' or 'skip' */
		IfNotBlocked
		_m = 3; goto P999;
	case 2: /* generic 'else' */
		IfNotBlocked
		if (trpt->o_pm&1) continue;
		_m = 3; goto P999;

		 /* PROC P1 */
	case 3: // STATE 1 - Assignment_Q1.pml:7 - [assert(((_pid==0)||(_pid==1)))] (0:0:0 - 1)
		IfNotBlocked
		reached[0][1] = 1;
		spin_assert(((((int)((P0 *)_this)->_pid)==0)||(((int)((P0 *)_this)->_pid)==1)), "((_pid==0)||(_pid==1))", II, tt, t);
		_m = 3; goto P999; /* 0 */
	case 4: // STATE 2 - Assignment_Q1.pml:9 - [flag[_pid] = 1] (0:0:1 - 3)
		IfNotBlocked
		reached[0][2] = 1;
		(trpt+1)->bup.oval = ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]);
		now.flag[ Index(((P0 *)_this)->_pid, 2) ] = 1;
#ifdef VAR_RANGES
		logval("flag[_pid]", ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 5: // STATE 3 - Assignment_Q1.pml:10 - [turn = (1-_pid)] (0:0:1 - 1)
		IfNotBlocked
		reached[0][3] = 1;
		(trpt+1)->bup.oval = ((int)now.turn);
		now.turn = (1-((int)((P0 *)_this)->_pid));
#ifdef VAR_RANGES
		logval("turn", ((int)now.turn));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 6: // STATE 4 - Assignment_Q1.pml:11 - [(((flag[(1-_pid)]==0)||(turn==_pid)))] (0:0:0 - 1)
		IfNotBlocked
		reached[0][4] = 1;
		if (!(((((int)now.flag[ Index((1-((int)((P0 *)_this)->_pid)), 2) ])==0)||(((int)now.turn)==((int)((P0 *)_this)->_pid)))))
			continue;
		_m = 3; goto P999; /* 0 */
	case 7: // STATE 5 - Assignment_Q1.pml:13 - [numCriticalProcesses = (numCriticalProcesses+1)] (0:0:1 - 1)
		IfNotBlocked
		reached[0][5] = 1;
		(trpt+1)->bup.oval = ((int)now.numCriticalProcesses);
		now.numCriticalProcesses = (((int)now.numCriticalProcesses)+1);
#ifdef VAR_RANGES
		logval("numCriticalProcesses", ((int)now.numCriticalProcesses));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 8: // STATE 6 - Assignment_Q1.pml:14 - [assert((numCriticalProcesses==1))] (0:0:0 - 1)
		IfNotBlocked
		reached[0][6] = 1;
		spin_assert((((int)now.numCriticalProcesses)==1), "(numCriticalProcesses==1)", II, tt, t);
		_m = 3; goto P999; /* 0 */
	case 9: // STATE 7 - Assignment_Q1.pml:15 - [numCriticalProcesses = (numCriticalProcesses+1)] (0:0:1 - 1)
		IfNotBlocked
		reached[0][7] = 1;
		(trpt+1)->bup.oval = ((int)now.numCriticalProcesses);
		now.numCriticalProcesses = (((int)now.numCriticalProcesses)+1);
#ifdef VAR_RANGES
		logval("numCriticalProcesses", ((int)now.numCriticalProcesses));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 10: // STATE 8 - Assignment_Q1.pml:17 - [flag[_pid] = 0] (0:0:1 - 1)
		IfNotBlocked
		reached[0][8] = 1;
		(trpt+1)->bup.oval = ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]);
		now.flag[ Index(((P0 *)_this)->_pid, 2) ] = 0;
#ifdef VAR_RANGES
		logval("flag[_pid]", ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case  _T5:	/* np_ */
		if (!((!(trpt->o_pm&4) && !(trpt->tau&128))))
			continue;
		/* else fall through */
	case  _T2:	/* true */
		_m = 3; goto P999;
#undef rand
	}

