#include<iostream>
#include<climits>
#include<algorithm>
#include<vector>
using namespace std;
#define len(x) int((x).size())
#define ll long long
#define ld long double
#define pi pair<int,int>
#define nl '\n';
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin>>n;
        
        string s;
        cin>>s;
        
        int e = 0;
        bool f = true;
        for(int i=0;i<n;i++){
            if (s[i]=='.')
            {
                e++;
            }
            if(i>0 && i<n-1){
                if(s[i-1] == '.' && s[i] == '.' && s[i+1] == '.'){
                    cout<<2<<endl;
                    f = false;
                }
            }
            if(f)
                cout<<e<<endl;
        }
    }
}