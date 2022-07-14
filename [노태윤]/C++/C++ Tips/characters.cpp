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

#include <iostream>

using namespace std;

int N, cnt[26];
string s, ans;

int main() {

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> s;
        cnt[s[0] - 'a']+=1;
    }

    for (int i=0; i<26; i++) if (cnt[i]>=5) ans += (i+'a');
    if (ans.size()) cout << ans;
    else cout << "PREDAJA";

    return 0;
}

// i + 'a' 하면 자동으로 type casting 되어서 character 형태로 나온다
