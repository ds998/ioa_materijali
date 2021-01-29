#include <iostream>

using namespace std;


double dots[21][2];

void perms(int n) {
    double min_dist = 100000000.0;
    int min_perm[21];

    int perm[21];
    for (int i = 1; i <= n; i++) {
        perm[i] = i;
    }

    while (true) {
        double dist = 0.0;
        for (int i = 1; i < n; i++) {
            int first_dot = perm[i];
            int second_dot = perm[i + 1];
            dist += sqrt((dots[second_dot][1] - dots[first_dot][1]) * (dots[second_dot][1] - dots[first_dot][1]) + (dots[second_dot][0] - dots[first_dot][0]) * (dots[second_dot][0] - dots[first_dot][0]));
        }
        if (dist < min_dist) {
            min_dist = dist;
            for (int i = 1; i <= n; i++) {
                min_perm[i] = perm[i];
            }
        }
        int temp = 0;
        int first = 1;
        int last = n;
        int k = n - 1;
        int l = last;
        while (k > first) {
            if (perm[k] < perm[k + 1]) break;
            k--;
        }

        if (perm[k] > perm[k + 1]) {
            cout << "Minimalna distanca za n=" << n << " : " << min_dist << endl;
            cout << "Minimalna permutacija za n=" << n << " : ";
            for (int i = 1; i <= n; i++) {
                cout << min_perm[i] << " ";
            }
            cout << endl;
            cout << endl;
            return;
        }

        while (l > k) {
            if (perm[l] > perm[k]) break;
            l--;
        }

        temp = perm[k];
        perm[k] = perm[l];
        perm[l] = temp;

        first = k + 1;
        while (first < last) {
            temp = perm[first];
            perm[first] = perm[last];
            perm[last] = temp;
            first++;
            last--;
        }



    }

}

int main() {


    dots[1][0] = 62.0; dots[1][1] = 58.4;
    dots[2][0] = 57.5; dots[2][1] = 56.0;
    dots[3][0] = 51.7; dots[3][1] = 56.0;
    dots[4][0] = 67.9; dots[4][1] = 19.6;
    dots[5][0] = 57.7; dots[5][1] = 42.1;
    dots[6][0] = 54.2; dots[6][1] = 29.1;
    dots[7][0] = 46.0; dots[7][1] = 45.1;
    dots[8][0] = 34.7; dots[8][1] = 45.1;
    dots[9][0] = 45.7; dots[9][1] = 25.1;
    dots[10][0] = 34.7; dots[10][1] = 26.4;
    dots[11][0] = 28.4; dots[11][1] = 31.7;
    dots[12][0] = 33.4; dots[12][1] = 60.5;
    dots[13][0] = 22.9; dots[13][1] = 32.7;
    dots[14][0] = 21.5; dots[14][1] = 45.8;
    dots[15][0] = 15.3; dots[15][1] = 37.8;
    dots[16][0] = 15.1; dots[16][1] = 49.6;
    dots[17][0] = 9.1; dots[17][1] = 52.8;
    dots[18][0] = 9.1; dots[18][1] = 40.3;
    dots[19][0] = 2.7; dots[19][1] = 56.8;
    dots[20][0] = 2.7; dots[20][1] = 33.1;

    perms(8);
    perms(12);





    return 0;
}