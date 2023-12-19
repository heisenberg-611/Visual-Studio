/* A simple student grades database. */
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#define CLASSES  3
#define GRADES  30
int grade[CLASSES][GRADES];
void enter_grades(void);
int get_grade(int num);
void disp_grades(int g[][GRADES]);
int main(void)
{
    char ch, str[80];
    for(;;) 
    { do 
        {
            printf("(E)nter grades\n");
            printf("(R)eport grades\n");
            printf("(Q)uit\n");
            gets(str);
            ch = toupper(*str);
        } 
    while(ch!='E' && ch!='R' && ch!='Q');
    switch(ch) 
        {
      case 'E':
        enter_grades();
        break;
      case 'R':
        disp_grades(grade);
        break;
      case 'Q':
        exit(0); 
        }
    }
    return 0; 
}
/* Enter the student's grades. */
void enter_grades(void)
{
int t, i;
  for(t=0; t<CLASSES; t++) 
    {
        printf("Class # %d:\n", t+1);
        for(i=0; i<GRADES; ++i)
        grade[t][i] = get_grade(i);
    }
}
/* Read a grade. */
int get_grade(int num)
    {
    char s[80];
        printf("Enter grade for student # %d:\n", num+1);
        gets(s);
        return(atoi(s));
    }
/* Display grades. */
void disp_grades(int g[][GRADES])
{
int t, i;
    for(t=0; t<CLASSES; ++t) 
    {
        printf("Class # %d:\n", t+1);
         for(i=0; i<GRADES; ++i)
         printf("Student #%d is %d\n", i+1, g[t][i]);
    }
}