/**
 * Includes the standard input/output header file. This provides declarations for standard I/O functions like printf and scanf.
 */
#include <stdio.h>
int main(void)
{
    int t, i, num[4][5];
    for(t=0; t<4; ++t)
    {
       for(i=0; i<5; ++i)
        {
            num[t][i] = (t*5)+i+1;
        }
    }
    /* now print them out */
    for(t=0; t<4; ++t) 
    {
        for(i=0; i<5; ++i)
        {
            printf("%3d ", num[t][i]);
        }
        printf("\n");
    }
    return 0; 
}