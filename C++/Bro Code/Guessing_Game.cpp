#include<iostream>
using namespace std;

int main(){
    int num = 0;
    int guess = 0;
    int tries = 0;

    srand(time(NULL));
    num = (rand() % 100 )+ 1;

    cout<<"*************NUMBER GUESSING GAME**************"<<endl;

    do{
        cout<<"Enter a guess between (1-100)"<<endl;
        cin>>guess;
        tries++;

        if(guess>num){
            cout<<"Number too high"<<endl;
        }
        else if(guess<num){
            cout<<"Number too low"<<endl;
        }
        else{
            cout<<"CORRECT! # of tries : "<< tries <<endl;
        }

    }while(guess != num);
    
    cout<<"****************************************";
    
    return 0;
}
//hello