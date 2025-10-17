#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        long long a, b;
        cin >> a >> b;

        vector<long long> ops;
        bool ok = false;

        for (int step = 0; step < 100; ++step) {
            if (a == b) {
                ok = true;
                break;
            }

            long long x = (a ^ b);
            if (x <= a) {
                ops.push_back(x);
                a ^= x;
                ok = true;
                break;
            } else {
                // make a smaller but change bits
                if (a == 0) break; // can't move anymore
                ops.push_back(a - 1);
                a ^= (a - 1);
            }
        }

        if (!ok) {
            cout << -1 << "\n";
        } else {
            cout << ops.size() << "\n";
            if (!ops.empty()) {
                for (int i = 0; i < (int)ops.size(); i++) {
                    cout << ops[i] << (i + 1 == (int)ops.size() ? '\n' : ' ');
                }
            }
        }
    }
    return 0;
}
