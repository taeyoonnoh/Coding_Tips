#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    vector<int> v = {1,5,3,2,9,0};
    sort(v.begin(),v.end(),greater<>()); // 내림차순 정렬
    for (auto& i:v)
        cout<<i<<" ";
}

int main(){
    vector<int> v = {1,5,3,2,9,0};
    sort(v.begin(),v.end()); // 오름차순 정렬
    for (auto& i:v)
        cout<<i<<" ";
}
