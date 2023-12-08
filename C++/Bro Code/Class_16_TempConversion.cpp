#include<iostream>
using namespace std;

int main(){
    double Temperature;
    char Unit;

    cout<<"********* Temperature Conversion *********"<<endl;
    cout<<"F = Farenheit"<<endl;
    cout<<"C = Celcius"<<endl;
    cout<<"What do you want to convert?"<<endl;
    cin>>Unit;

    if(Unit == 'F' || 'f'){
        cout<<"Enter the temperature in Celcius: ";
        cin>>Temperature;

        Temperature = (1.8 * Temperature)+32.0;
        cout<<"Temperature is =>> "<<Temperature<<" F"<<endl;
    }
    else if(Unit == 'C' || 'c'){
        cout<<"Enter the temperature in Farenheit: ";
        cin>>Temperature;

        Temperature = (Temperature - 32)/1.8;
        cout<<"Temperature is =>> "<<Temperature<<" C"<<endl;
   }
   return 0;
}