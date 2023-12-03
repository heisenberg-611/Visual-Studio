#include<iostream>
using namespace std;

int main()
{
    int n, i;
    cout<<"Enter your number: ";
    cin>>n;
    for(i=2;i<n;i++){
        if(n%i==0){
            cout<<"Non prime"<<endl;
            break;
        }
    }
    i==n;
    cout<<"Prime"<<endl;
    return 0;
}