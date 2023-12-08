#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter number: ";
    cin>>n;
    
    if(n%2==0)
    {
        cout<<"Y= "<<(-1)*(n*(n+1)/2)<<endl;
    }
    else
    {
        cout<<"Y= "<<pow(-1,(n+1))*(n*(n+1))/2<<endl;
    }
    return 0;
    
}