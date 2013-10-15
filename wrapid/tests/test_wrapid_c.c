
// wrapid - Simpler wrapper of C libraries based on Ctypes 
// Stefano Pedemonte
// Aalto University, School of Science, Helsinki
// Oct 2013, Helsinki 


#include <stdio.h>
#include <stdlib.h>


/*
out = in
*/
extern int echo(int *in, int *out)
{
    *out = *in; 
    return 0;
}



