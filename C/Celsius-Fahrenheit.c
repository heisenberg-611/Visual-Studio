#include <stdio.h>
/* print Fahrenheit-Celsius table */
/*for fahr = 0, 20, ..., 300 */
int main()
{
    float fahr, celsius;
    float lower, upper, step;
    lower = 0; /* lower limit of temperature scale */
    upper = 300; /* upper limit*/
    step = 5; /* step size*/ 
    fahr = lower;
    printf("%3s\t%3s\n","Fhar","Celsius");
    while (fahr <= upper) 
    {
        celsius = 5 * (fahr-32) / 9;
        printf("%3.0f\t%3.4f\n", fahr, celsius);
        fahr = fahr + step;
    }
}



#include <stdio.h>
/* print Fahrenheit-Celsius table */
int main()
{
    int fahr;
    for (fahr = 0; fahr <= 300; fahr = fahr + 20)
    printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
    return 0;
}