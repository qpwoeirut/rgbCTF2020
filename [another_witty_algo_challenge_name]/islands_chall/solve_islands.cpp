#include <fstream>
#include <iostream>

using namespace std;

const int N = 5000;
const int C = 400;

bool grid[N][N];
bool V[N][N];
void dfs(int r, int c) {
	if (r < 0 || r >= N || c < 0 || c >= N || V[r][c] || grid[r][c] == false) {
		return;
	}

	V[r][c] = true;
	dfs(r+1, c);
	dfs(r-1, c);
	dfs(r, c+1);
	dfs(r, c-1);
}

int main() {
    ifstream fin("grid.txt");
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            char c;
            fin >> c;
            grid[i][j] = c == '1';
        }
    }

	int ans = 0;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (!V[i][j] && grid[i][j] == true) {
				++ans;
				dfs(i, j);
			}
		}
	}

	cout << ans << endl;

	return 0;
}


