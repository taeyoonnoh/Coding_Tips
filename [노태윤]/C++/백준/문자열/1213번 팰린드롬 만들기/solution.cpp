#include <iostream>

using namespace std;

int alpha[26], flag, mid_pos;
string str, ans;
char mid;

int main() {

    cin >> str;
    for (char a : str) alpha[a - 'A'] +=1;

    for (int i = 25; i>= 0; i--) { 
        if (!alpha[i]) continue;

        if (alpha[i] & 1) { 
            mid = char(i + 'A');
            flag +=1;
            alpha[i] -=1;
        }

        if (flag >=2) {
            cout << "I'm Sorry Hansoo\n";
            return 0;
        }
        for (int j=0; j<alpha[i]; j+=2) { 
            ans = char(i+'A') + ans;
            ans += char(i+'A');
        }
    }
    // mid_pos = ans.size() /2;
    if (mid) ans.insert(ans.begin() + ans.size()/2, mid);
    cout << ans << "\n";

    return 0;

}
