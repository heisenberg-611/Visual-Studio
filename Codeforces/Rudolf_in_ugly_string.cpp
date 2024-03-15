#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t; // Number of test cases

    while (t--) {
        int n;
        cin >> n; // Length of the string

        string s;
        cin >> s; // Input string

        // Initialize counters for "pie" and "map" occurrences
        int pieCount = 0, mapCount = 0;

        // Iterate through the string to find occurrences
        for (int i = 0; i < n; ++i) {
            if (i + 2 < n) {
                // Check for "pie"
                if (s[i] == 'p' && s[i + 1] == 'i' && s[i + 2] == 'e') {
                    pieCount++;
                    i += 2; // Skip the next two characters
                }
            }
            if (i + 2 < n) {
                // Check for "map"
                if (s[i] == 'm' && s[i + 1] == 'a' && s[i + 2] == 'p') {
                    mapCount++;
                    i += 2; // Skip the next two characters
                }
            }
        }

        // Calculate total deletions needed
        int totalDeletions = pieCount + mapCount;

        cout << totalDeletions << endl;
    }

    return 0;
}
