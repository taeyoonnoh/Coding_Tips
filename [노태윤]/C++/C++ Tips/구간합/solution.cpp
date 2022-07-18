#include <iostream>

using namespace std;

int N, K, num, psum[100001], max_val = -1 * (100000 * 100) - 4;

int main() {

    cin >> N >> K;

    for (int i=1;i<=N;i++) {
        cin >> num;
        psum[i] = psum[i-1] + num;
    }

    for (int i=K;i<=N;i++) { 
        max_val = max(max_val, psum[i] - psum[i-K]);
        // cout << i << " " << max_val << "\n";
    }

    cout << max_val;

    //확인
    // for (int i=0;i<10;i++) { 
    //     cout << psum[i] << "\n";
    // }

    return 0;

}

// 먼저 전 것을 계속 더해주기 (Cumulative Sum)
// 그 후 K 만큼 빼줘서 그 떄의 Max 값 갱신!
