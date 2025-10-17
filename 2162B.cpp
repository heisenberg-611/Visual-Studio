#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(const string &x) {
    int l = 0, r = x.size() - 1;
    while (l < r) {
        if (x[l] != x[r]) return false;
        l++, r--;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        string s;
        cin >> n >> s;
        bool found = false;

        for (int mask = 0; mask < (1 << n); mask++) {
            string p, x;
            vector<int> indices;

            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    p.push_back(s[i]);
                    indices.push_back(i + 1);
                } else {
                    x.push_back(s[i]);
                }
            }

            // Check if p is non-decreasing
            bool nonDec = true;
            for (int i = 0; i + 1 < (int)p.size(); i++) {
                if (p[i] > p[i + 1]) {
                    nonDec = false;
                    break;
                }
            }
            if (!nonDec) continue;

            // Check if x is palindrome
            if (isPalindrome(x)) {
                cout << indices.size() << "\n";
                if (!indices.empty()) {
                    for (int i = 0; i < (int)indices.size(); i++) {
                        cout << indices[i] << (i + 1 == indices.size() ? '\n' : ' ');
                    }
                }
                found = true;
                break;
            }
        }

        if (!found) cout << "-1\n";
    }

    return 0;
}
