#include <stdio.h>
#include <stdint.h>
#include "guava.h"

static const long
	K   = 2862933555777941757L,
	M64 = 0xffffffffffffffffL;

static const double
	D   = 0x1.0p31;

unsigned guava(long state, unsigned int buckets) {
	unsigned candidate = 0;
	unsigned next;
	while (1) {
		state = K * state + 1;
		next = (int) ( (double) (candidate + 1) / ( (double)( (int)( (long unsigned) state >> 33 ) + 1 ) / D ) );
		if ( ( next >= 0 ) && ( next < buckets )) {
			candidate = next;
		} else {
			return candidate;
		}
	}
}

