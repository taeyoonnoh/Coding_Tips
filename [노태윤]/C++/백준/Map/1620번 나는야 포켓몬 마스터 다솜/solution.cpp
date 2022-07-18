#include <iostream>
#include <map>

using namespace std;

int N, M;
map<string, int> map1;
map<int, string> map2;
string str, check_str;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;

    for (int i=0; i<N; i++) {
        cin >> str;
        map1[str] = i+1;
        map2[i+1] = str;
    }

    for (int i=0;i<M;i++) { 
        cin >> check_str;
        if (atoi(check_str.c_str()) == 0) cout << map1[check_str] << "\n";
        else cout << map2[atoi(check_str.c_str())] << "\n";
    }
}

// map stl 써야함
// I/O 추가 안해주면 시간 초과 나더라..
// aoit(check_str.c_str()) == 0 --> 숫자가 아니라는 
