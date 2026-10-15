#include <iostream>
#include <string>
using namespace std;

int main() {
    string data;
    int parity = 0;
    cout << "Enter data bits: ";
    cin >> data;

    for (char c : data)
        parity ^= (c - '0');

    cout << "Even parity bit: " << parity << endl;

    string received;
    cout << "Enter received data with parity bit: ";
    cin >> received;

    int check = 0;
    for (char c : received)
        check ^= (c - '0');

    if (check == 0)
        cout << "No error detected";
    else
        cout << "Error detected";

    return 0;
}