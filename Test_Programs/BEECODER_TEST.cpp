#include<iostream>
#include<iomanip>
using namespace std;

int main(){

    int n;
    string word;
    cin>>n;

    while(n--){
        cin>>word;

        if(word.size()>10){
            cout<<word[0]<<  word.size()-2 << word[word.size()-1] <<endl;
        }
        else{
            cout<<word<<endl;
        }
    }

    return 0;
}