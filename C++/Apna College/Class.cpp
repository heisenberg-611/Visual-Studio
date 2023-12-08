//multiple language robot
#include<iostream>
using namespace std;

int main()
{
    char button;
    cout<<"Input a charachter: ";
    cin>>button;

    if(button =='a')
    {
        cout<<"Hello"<<endl;
    }
    else if(button=='b')
    {
        cout<<"Hola"<<endl;
    }
    else if(button=='c')
    {
        cout<<"Namaste"<<endl;
    }
    else
    {
        cout<<"I am still learning"<<endl;
    }
    return 0;
}   