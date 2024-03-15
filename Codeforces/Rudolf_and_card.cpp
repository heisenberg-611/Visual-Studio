#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;

        vector<int> left_pocket(n);
        vector<int> right_pocket(m);

        for (int i = 0; i < n; ++i) {
            cin >> left_pocket[i];
        }

        for (int i = 0; i < m; ++i) {
            cin >> right_pocket[i];
        }

        // Sort the denominations in both pockets
        sort(left_pocket.begin(), left_pocket.end());
        sort(right_pocket.begin(), right_pocket.end());

        // Initialize a counter for valid pairs
        int valid_pairs = 0;

        // Iterate through the denominations in both pockets
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (left_pocket[i] + right_pocket[j] <= k) {
                    valid_pairs++;
                }
            }
        }

        cout << valid_pairs << endl;
    }

    return 0;
}
