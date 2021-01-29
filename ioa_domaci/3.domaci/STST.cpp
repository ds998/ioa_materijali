#include <iostream>

using namespace std;

int prices[11][11];

int min_price = 0;
int real_p[8];
int t[18];
int min_t[18];

void calculate() {
	int sum = 0;
	int appearances[11];
	for (int i = 0; i < 11; i++) {
		appearances[i] = 0;
	}
	for (int i = 0; i < 18; i += 2) {
		int j = i + 1;
		sum += prices[t[i]][t[j]];
		appearances[t[i]]++;
		appearances[t[j]]++;
	}

	for (int i = 1; i <= 10; i++) {
		if (appearances[i] >= 4) {
			sum += 100 * (appearances[i] - 3);
		}
	}
	
	if (sum < min_price || min_price == 0) {
		min_price = sum;
		for (int i = 0; i < 18; i++) {
			min_t[i]=t[i];
		}
	}
}

void stst() {
	int v[10];
	int q = 0;
	for (int i = 0; i < 10; i++) {
		v[i] = 0;
	}
	for (int i = 0; i < 8; i++) {
		v[real_p[i] - 1] += 1;
	}
	for (int i = 0; i < 18; i++) {
		t[i] = 0;
	}

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 10; j++) {
			if (v[j] == 0) {
				v[j] = -1;
				t[q++] = j + 1;
				t[q++] = real_p[i];
				v[real_p[i] - 1]--;
				break;
			}
		}
	}

	int x = 0;

	for (int i = 0; i < 10; i++) {
		if (v[i] == 0 && x == 0) {
			t[q++] = i + 1;
			x++;
		}
		else if (v[i] == 0 && x == 1) {
			t[q++] = i + 1;
			break;
		}
	}

	calculate();


}

int main() {
	prices[2][1] = 374;
	prices[3][1] = 200;
	prices[3][2] = 255;
	prices[4][1] = 223;
	prices[4][2] = 166;
	prices[4][3] = 128;
	prices[5][1] = 108;
	prices[5][2] = 433;
	prices[5][3] = 277;
	prices[5][4] = 430;
	prices[6][1] = 178;
	prices[6][2] = 199;
	prices[6][3] = 821;
	prices[6][4] = 47;
	prices[6][5] = 453;
	prices[7][1] = 252;
	prices[7][2] = 135;
	prices[7][3] = 180;
	prices[7][4] = 52;
	prices[7][5] = 478;
	prices[7][6] = 91;
	prices[8][1] = 285;
	prices[8][2] = 95;
	prices[8][3] = 160;
	prices[8][4] = 84;
	prices[8][5] = 344;
	prices[8][6] = 110;
	prices[8][7] = 114;
	prices[9][1] = 240;
	prices[9][2] = 136;
	prices[9][3] = 131;
	prices[9][4] = 40;
	prices[9][5] = 389;
	prices[9][6] = 64;
	prices[9][7] = 83;
	prices[9][8] = 47;
	prices[10][1] = 356;
	prices[10][2] = 17;
	prices[10][3] = 247;
	prices[10][4] = 155;
	prices[10][5] = 423;
	prices[10][6] = 181;
	prices[10][7] = 117;
	prices[10][8] = 78;
	prices[10][9] = 118;


	for (int i = 1; i < 10; i++) {
		for (int j = i + 1; j <= 10; j++) {
			prices[i][j] = prices[j][i];
		}
	}

	

	int p[8];
	for (int i = 0; i < 8; i++) {
		p[i] = 0;
	}
	int q;

	do {

		for (int i = 0; i < 8; i++) {
			real_p[i] = p[i] + 1;
		}
		stst();
		q = 7;
		while (q >= 0) {
			p[q]++;
			if (p[q] == 10) {
				p[q] = 0;
				q--;
			}
			else break;
		}



	} while (q >= 0);

	cout << "Minimalna cena povezivanja: " << min_price << endl;
	cout << endl;
	cout << "Sekvenca minimalnog povezanog stabla:" << endl;
	for (int i = 0; i < 18; i += 2) {
		int j = i + 1;
		cout << (char)(min_t[i]+64) << " ";
		cout << (char)(min_t[j]+64) << "  ";
	}
	cout << endl;
	return 0;


}