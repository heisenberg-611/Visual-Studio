#include <iostream>
using namespace std;

int main(){
    double a,b,c;
    cin>>a>>b>>c;
    cout.precision(3);
    cout.setf(ios::fixed);
    cout<<"TRIANGULO: "<<(a*c)/2<<endl;
    cout<<"CIRCULO: "<<3.14159*c*c<<endl;
    cout<<"TRAPEZIO: "<<((a+b)*c)/2<<endl;
    cout<<"QUADRADO: "<<b*b<<endl;
    cout<<"RETANGULO: "<<a*b<<endl;
    return 0;
}