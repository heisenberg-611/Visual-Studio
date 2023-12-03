//158A
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    
    int n, k, s, next = 0;

    cin>>n>>k;

    vector<int> scores;

    for(int i = 0; i < n; i++)
    {
        cin >> s;
        scores.push_back(s);
    }
    for(int i = 0; i<n; i++)
    {
        if( scores[i]>=scores[k-1] && scores[i]>0)
        {
            next++;
        }
    }
    cout<<next<<endl;
    return 0;
}