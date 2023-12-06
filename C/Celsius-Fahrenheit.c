#include <stdio.h>
/* print Fahrenheit-Celsius table
for fahr = 0, 20, ..., 300 */
int main()
{
    float fahr, celsius;
    float lower, upper, step;
    lower = 0; /* lower limit of temperature scale */
    upper = 300; /* upper limit */
    step = 5; /* step size */
    fahr = lower;
    printf("%3s\t%3s\n","Fhar","Celsius");
    while (fahr <= upper) 
    {
        celsius = 5 * (fahr-32) / 9;
        printf("%3.0f\t%3.2f\n", fahr, celsius);
        fahr = fahr + step;
    }
}