#include<iostream>
#include<string>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    for(int i = 0; i < a.length(); i++){
        a[i] = tolower(a[i]);
        b[i] = tolower(b[i]);
    }
    if(a==b){
        cout<<"0"<<endl;
    }
    else{
        for(int i = 0; i < a.length(); i++){
            if(a[i] < b[i]){
                cout<<"-1"<<endl;
                break;
            }
            else if(a[i] > b[i]){
                cout<<"1"<<endl;
                break;
            }
            else{
                continue;
            }
        }
    }
}