#include <iostream>
#include <algorithm>

using namespace std;

int shorts[9];

int main() { 

    // 배열에 넣기
    for (int i=0; i<9; i++) {
        cin >> shorts[i];
    }

    sort(shorts, shorts+9);

    do {
        int sum = 0;
        for (int i=0;i<7;i++) sum += shorts[i];
        for (int i=0;i<7;i++) cout << shorts[i] << " ";
        cout << endl << "The Sum is : " << sum << "\n";
        cout << "=======================" << endl;
        if (sum == 100) break;
    }
    while (next_permutation(shorts, shorts+9));
    for (int i=0; i<7; i++) { 
        cout << shorts[i] << endl;
    }

}

// 9개 중에 7개 순서없이 뽑기
