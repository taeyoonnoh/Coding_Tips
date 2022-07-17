#include <iostream>
using namespace std;

string pre, suf, pattern, str;
int asterisk_pos, N;

int main() { 
    cin >> N;
    cin >> pattern;
    asterisk_pos = pattern.find('*');
    pre = pattern.substr(0, asterisk_pos);
    suf = pattern.substr(asterisk_pos+1);

    for (int i=0; i<N;i++) { 
        cin >> str;
        if (suf.size() + pre.size() > str.size()) cout << "NE" << "\n";
        else {
            if (str.substr(0, pre.size()) == pre && str.substr(str.size()-suf.size()) == suf) cout << "DA" << "\n";
            else cout << "NE" << "\n";
        }
    }

    return 0;

}

// find 함수는 해당 문자열의 위치값 int 로 반환
// substr(start index, 길이) -- 길이 paramter 는 굳이 없어도 됨, 없다면 맨 마지막 까지 반환
