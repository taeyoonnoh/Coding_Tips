#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> temp;
    
    for (int i=0;i<commands.size();i++){
        temp = array; // array 복사
        sort(temp.begin()+commands[i][0]-1,temp.begin()+commands[i][1]); // 현재 index 부터 끝 index 까지 (파이썬 slicing 이랑 다름!)
        answer.push_back(temp[commands[i][0]-1+commands[i][2]-1]); // answer 에 append 하는 
    }
    return answer;
}
