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
#define vi vector<int>
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
    	int n;
		cin>>n;
    	vi arr(n);
    	for(int i=0; i<n; i++)
    		cin>>arr[i];

	    if(arr[0] != 1){
	    	cout<<"No"<<nl;
	    }
	    else{
	        cout<<"Yes"<<nl;   
	    }
    }
}