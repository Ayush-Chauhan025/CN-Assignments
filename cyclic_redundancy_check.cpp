#include <iostream>
#include <string>
using namespace std;

string divide(string data, string gen) {
    string rem = data;

    for (int i = 0; i <= (int)data.size() - (int)gen.size(); i++) {
        if (rem[i] == '1') {
            for (int j = 0; j < (int)gen.size(); j++)
                rem[i + j] = (rem[i + j] == gen[j]) ? '0' : '1';
        }
    }

    return rem.substr(data.size() - gen.size() + 1);
}

int main() {
    string data, gen;
    cout << "Enter data bits: ";
    cin >> data;
    cout << "Enter generator bits: ";
    cin >> gen;

    string code = data + string(gen.size() - 1, '0');
    string rem = divide(code, gen);
    string transmitted = data + rem;

    cout << "Transmitted code: " << transmitted << endl;

    string received;
    cout << "Enter received code: ";
    cin >> received;

    rem = divide(received, gen);

    bool error = false;
    for (char c : rem)
        if (c == '1') error = true;

    cout << (error ? "Error detected" : "No error detected");
    return 0;
}