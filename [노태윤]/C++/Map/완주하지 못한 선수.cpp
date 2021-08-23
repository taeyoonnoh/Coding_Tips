#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

// dictionary 활용
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int>d; // unordered map 에서는 자동으로 0 이 default 로 저장이 됨
    for (auto& i :participant) d[i]++; // 1씩 더하기
    for (auto& i: completion) d[i]--; // 1씩 빼주기
    for (auto& i : d){
        if (i.second>0){ // value 값이 0 초과면
            answer=i.first; // 이 때의 key 값을 담는다
            break;
        }
    }
    return answer;
}

// sort 함수 활용
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(),participant.end()); // 오름차순 정렬
    sort(completion.begin(),completion.end()); // 오름차순 정렬
    for (int i=0;i<completion.size();i++){
        if (completion[i]!=participant[i]){ // 같지 않다면
            return participant[i];
        }
    }
    return participant[participant.size() - 1]; // participant 의 마지막 값 담기
}
