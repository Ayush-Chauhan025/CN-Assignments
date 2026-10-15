#include <iostream>
#include <vector>
using namespace std;

int checksum(vector<int> data) {
    unsigned int sum = 0;

    for (int x : data) {
        sum += x;
        sum = (sum & 65535) + (sum >> 16);
    }

    return (~sum) & 65535;
}

int main() {
    int n;
    cout << "Enter number of 16-bit words: ";
    cin >> n;

    vector<int> data(n);
    cout << "Enter 16-bit words in decimal (0-65535):\n";

    for (int i = 0; i < n; i++)
        cin >> data[i];

    int cs = checksum(data);
    cout << "Checksum: " << cs << endl;

    data.push_back(cs);

    cout << "Enter received words including checksum:\n";
    vector<int> received(n + 1);

    for (int i = 0; i <= n; i++)
        cin >> received[i];

    unsigned int sum = 0;

    for (int x : received) {
        sum += x;
        sum = (sum & 65535) + (sum >> 16);
    }

    cout << ((sum & 65535) == 65535
                 ? "No error detected"
                 : "Error detected");

    return 0;
}