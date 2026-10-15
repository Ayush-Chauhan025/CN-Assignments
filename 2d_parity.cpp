#include <iostream>
using namespace std;

int main() {
    int r, c, a[20][20] = {};
    cout << "Enter rows and columns: ";
    cin >> r >> c;

    cout << "Enter data bits:\n";
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            cin >> a[i][j];

    for (int i = 0; i < r; i++) {
        int p = 0;
        for (int j = 0; j < c; j++)
            p ^= a[i][j];
        a[i][c] = p;
    }

    for (int j = 0; j <= c; j++) {
        int p = 0;
        for (int i = 0; i < r; i++)
            p ^= a[i][j];
        a[r][j] = p;
    }

    cout << "Transmitted data:\n";
    for (int i = 0; i <= r; i++) {
        for (int j = 0; j <= c; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }

    int b[20][20];
    cout << "Enter received data including parity bits:\n";
    for (int i = 0; i <= r; i++)
        for (int j = 0; j <= c; j++)
            cin >> b[i][j];

    bool error = false;

    for (int i = 0; i <= r; i++) {
        int p = 0;
        for (int j = 0; j <= c; j++)
            p ^= b[i][j];
        if (p) error = true;
    }

    for (int j = 0; j <= c; j++) {
        int p = 0;
        for (int i = 0; i <= r; i++)
            p ^= b[i][j];
        if (p) error = true;
    }

    cout << (error ? "Error detected" : "No error detected");
    return 0;
}