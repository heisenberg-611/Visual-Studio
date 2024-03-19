#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        int num_of_tent = a + (b / 3) + (((b % 3) + c) / 3) + 1;
        if (((b % 3) + c) % 3 == 0) {
            num_of_tent = a + (b / 3) + (((b % 3) + c) / 3);
        } else if (b % 3 != 0 && (b % 3) + c < 3) {
            num_of_tent = -1;
        } else if (a == 0 && b == 0 && c == 0) {
            num_of_tent = 0;
        } else if (b == 0 && c == 0) {
            num_of_tent = a;
        } else if (a == 0 && c == 0) {
            num_of_tent = b / 3;
        }
        cout << num_of_tent << endl;
    }
    return 0;
}