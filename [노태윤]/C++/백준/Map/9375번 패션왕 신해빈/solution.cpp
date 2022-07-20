#include <iostream>
#include <map>

using namespace std;

int T, N;
string a, b;

int main() {
    cin >> T;

    for (int i=0; i<T; i++) {
        map<string, int> map1;
        cin >> N;
        long long ans=1;
        
        for (int j=0; j<N;j++) { 
            cin >> a >> b;
            map1[b]+=1;
        }   

        for (auto c : map1) { 
            ans *= c.second + 1;
        }

        cout << ans - 1 << "\n";

    }

    return 0;

}

// map을 계속 최신화 해줘야 된다는 점이 관건!!
