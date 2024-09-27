#include <iostream>
#include <vector>
#include <set>
#include <utility> // Include this for std::pair

using namespace std;

bool isChordal(int N, const vector<vector<int> >& adj) {
    vector<int> visited(N + 1, 0);
    vector<int> order(N + 1, 0);
    vector<int> degree(N + 1, 0);

    set<pair<int, int> > vertices;

    for (int i = 1; i <= N; ++i) {
        vertices.insert(make_pair(0, i)); // Use make_pair instead of brace initialization
    }

    int index = N;

    while (!vertices.empty()) {
        int v = vertices.begin()->second;
        vertices.erase(vertices.begin());

        order[v] = index--;
        visited[v] = 1;

        for (int u : adj[v]) {
            if (!visited[u]) {
                vertices.erase(make_pair(degree[u], u)); // Use make_pair instead of brace initialization
                degree[u]++;
                vertices.insert(make_pair(degree[u], u)); // Use make_pair instead of brace initialization
            }
        }
    }

    vector<int> largestClique(N + 1, 0);

    for (int v = 1; v <= N; ++v) {
        int maxCliqueSize = 1;

        for (int u : adj[v]) {
            if (order[u] > order[v]) {
                maxCliqueSize = max(maxCliqueSize, largestClique[u] + 1);
            }
        }

        largestClique[v] = maxCliqueSize;

        if (maxCliqueSize > N / 2) {
            return true;
        }
    }

    return false;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<vector<int> > adj(N + 1);

        for (int i = 0; i < M; ++i) {
            int A, B;
            cin >> A >> B;
            adj[A].push_back(B);
            adj[B].push_back(A);
        }

        if (isChordal(N, adj)) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
