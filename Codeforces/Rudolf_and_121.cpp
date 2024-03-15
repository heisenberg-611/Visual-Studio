#include <iostream>
#include <vector>

using namespace std;

string makeZero(vector<int>& A, int n) {
    int xorSum = 0;
    bool isZero = true;

    for (int i = 0; i < n; ++i) {
        if (A[i] > 0) {
            isZero = false;
        }
        xorSum ^= A[i];
    }

    if (isZero || xorSum == 0) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> A(n);
        for (int i = 0; i < n; ++i) {
            cin >> A[i];
        }

        cout << makeZero(A, n) << "\n";
    }

    return 0;
}
