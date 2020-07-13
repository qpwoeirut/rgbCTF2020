#include <fstream>
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int N = 5000;
const int C = 400;

bool grid[N][N];

void dfs(int r, int c) {
	if (r < 0 || r >= N || c < 0 || c >= N || grid[r][c]) {
		return;
	}

	grid[r][c] = true;
	if (rand() % 1000 < C) {
		dfs(r+1, c);
	}
	if (rand() % 1000 < C) {
		dfs(r-1, c);
	}
	if (rand() % 1000 < C) {
		dfs(r, c+1);
	}
	if (rand() % 1000 < C) {
		dfs(r, c-1);
	}
}


int main() {
	srand(time(NULL));

	for (int i=0; i<N*50; i++) {
		int r = rand() % N;
		int c = rand() % N;

		dfs(r, c);
	}

	ofstream fout("grid.txt");
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			fout << grid[i][j];
		}
		fout << endl;
	}

	return 0;
}
