#include<iostream>
#include<iomanip>
using namespace std;

void showBalance(double balance);
double deposite();
double withdraw(double balance);

int main()
{
    double balance = 0;
    int choice = 0;
    do{ 
    cout << "******************"<<endl;
    cout << "Enter your choice:"<<endl;
    cout << "******************"<<endl;
    cout << "1. Show Balance"<<endl;
    cout << "2. Deposite Balance"<<endl;
    cout << "3. Withdraw Money"<<endl;
    cout << "4. Exit"<<endl;
    cin >> choice;

    switch(choice){
        case 1: showBalance(balance);
                break;
        case 2: balance = balance += deposite();
                showBalance(balance);
                break;
        case 3: balance = balance -= withdraw(balance);
                showBalance(balance);
                break;
        case 4: cout << "Thanks for visiting" << endl;
                break;
        default: cout << "Invalid choice";
    }

    }while (choice != 4);
    
    return 0;
}
void showBalance(double balance){
        cout << "Your balance is: $" << setprecision(2) << std::fixed << balance << endl;
}
double deposite(){

    double amount = 0;

    cout << "Enter amount to be deposited: ";
    cin >> amount;

    if(amount > 0){
        return amount;
    }
    else{
        cout << "That's not a valid amount: "<<endl;
    }
    return amount;
}
double withdraw(double balance){
    double amount = 0;

    cout << "Enter amount to be withdrawn: ";
    cin>>amount;
    if(amount > balance){
        cout << "Insufficient funds";
        return 0;
    }
    else if(amount < 0){
        cout << "That's not a valid amount: ";
        return 0;
    }
    else{
        return amount;
    }
}

//hello dear