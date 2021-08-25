#include<iostream>

using namespace std;

int main(){
    int N;
    int sum;
    int part;

    cin>>N;

    for (int i=0;i<=N;i++){
        sum = i;
        part = i;

        while (part){
            sum += part%10; // 235%10 ==> 5
            part /= 10; // 235/10 ==> 23
        }

        if (N==sum){
            cout<<i<<endl;
            return 0;
        }

    }
    cout<<0<<endl;
}
