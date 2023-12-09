#include <iostream>
using namespace std;
   
int MemorizeThis[10][20];

int main() 
{
        for (int x = 0; x < 10; x++) 
        {
            for (int y = 0; y < 20; y++ ) 
            { 
                MemorizeThis[x][y] = x * y;
            }       
        }
    cout << MemorizeThis[9][13] << endl;
    cout << sizeof(MemorizeThis) / sizeof(int) << endl;
    return 0;
}