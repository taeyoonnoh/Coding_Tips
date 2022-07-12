#include <iostream>
using namespace std;

int cnt[26];
string str;

int main() {

    cin >> str;

    for (char a : str) {
        cnt[a-'a']++;
    }

    for (int i=0; i<26; i++) { 
        cout << cnt[i] << " ";
    }

    return 0;

}

// cnt[a-'a'] 를 하게 되면 배열 크기를 줄일 수 있다!
