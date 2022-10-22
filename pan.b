	switch (t->back) {
	default: Uerror("bad return move");
	case  0: goto R999; /* nothing to undo */

		 /* PROC P1 */
;
		;
		
	case 4: // STATE 2
		;
		now.flag[ Index(((P0 *)_this)->_pid, 2) ] = trpt->bup.oval;
		;
		goto R999;

	case 5: // STATE 3
		;
		now.turn = trpt->bup.oval;
		;
		goto R999;
;
		;
		
	case 7: // STATE 5
		;
		now.numCriticalProcesses = trpt->bup.oval;
		;
		goto R999;
;
		;
		
	case 9: // STATE 7
		;
		now.numCriticalProcesses = trpt->bup.oval;
		;
		goto R999;

	case 10: // STATE 8
		;
		now.flag[ Index(((P0 *)_this)->_pid, 2) ] = trpt->bup.oval;
		;
		goto R999;
	}

