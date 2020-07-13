/*
 * gen_islands.cpp
 *
 *  Created on: Jul 12, 2020
 *      Author: Stanley
 */


#include <fstream>
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int N = 5000;
const int C = 400;

bool grid[N][N];

void dfs(int r, int c) {
//	cout <<r << ' ' << c << endl;
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


bool V[N][N];
void dfs2(int r, int c) {
	if (r < 0 || r >= N || c < 0 || c >= N || V[r][c] || grid[r][c] == false) {
		return;
	}

	V[r][c] = true;
	dfs2(r+1, c);
	dfs2(r-1, c);
	dfs2(r, c+1);
	dfs2(r, c-1);
}

int solve() {
	int ans = 0;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (!V[i][j] && grid[i][j] == true) {
				++ans;
				dfs2(i, j);
			}
		}
	}

	return ans;
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

	cout << solve() << endl;

	return 0;
}
