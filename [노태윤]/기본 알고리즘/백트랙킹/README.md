![1](https://user-images.githubusercontent.com/74780115/160077462-c6356df7-8661-4b8e-a600-e4a5bd683197.PNG)
# Backtracking

## 백트랭킹
* 임의의 집합 (set) 에서 주어진 기준 (criterion) 대로 
  * 원소의 순서(sequence)를 선택하는 문제를 푸는 데 적합
  
* 트리 자료구조의 변형된 깊이우선탐색 (DFS : depth-first-search)

* 모든 문제 사례에 대해서 효율적이지 않지만
  * 많은 문제 사례에 대해서 효율적
  * n-Queens, 부분집합의 합, 0-1 배낭문제, etc
  
## 백트랙킹과 n-Queens 문제
* ![1](https://user-images.githubusercontent.com/74780115/160077509-64a0d872-8786-45b8-ad0a-898a8094c8ea.PNG)
* 스택으로 많이 풀었을 것

* 미로찾기 문제를 트리 탐색 문제로 해석
 * DFS 를 통한 문제 해결 : 트리 구조의 preorder 방문
 * 백츠랙킹은 항상 트리 형태

## 상태공간트리 (State Space Tree)
* 상태 공간 : 해답을 탐색하기 위한 탐색 공간
* 상태 공간 트리 : 탐색 공간을 트리 형태의 구조로 암묵적으로 해석
* 최단 경로는 다 봐야되긴 함... (모든 경우의 수)

## 백트래킹 기법
* 상태공간트리를 깊이우선탐색으로 탐색
 * 전체 : 단순무식법 (Brute-Force)

* 방문 중인 노드에서 더 하위 노드로 가면 해답이 없을 경우
 * 해당 노드의 하위 트리를 방문하지 않고 부모 노드로 되돌아 감(backtrack)

* 유망함 (promising)
 * 방문 중인 노드에서 하위 노드가 해답을 발견할 가능성이 있으면 유망 (promising)

## 백트래킹과 가지치기 (pruning)
* 유망하지 않으면 부모 노드로 되돌아감
* 유망하지 않으면 하위 트리를 가지치기함

## 일반적인 백트래킹 알고리즘
* ![2](https://user-images.githubusercontent.com/74780115/160079922-0a2b8a0d-dc60-46b0-b2ad-d9954d38b769.PNG)

## 백트래킹 알고리즘의 구현
* 상태공간트리를 실제로 구현할 필요는 없음
* 현재 조사중인 가지의 값에 대해 추적만 하면 됨
* 상태공간트리는 암묵적으로 존재한다고 이해하면 됨

## 유망의 조건 1 : 같은 열 체크
* col[i] : i 번째 행(row) 에서 퀸이 놓여있는 열(column)의 위치
* col[k] : k 번째 행(row) 에서 퀸이 놓여있는 열(column)의 위치
* col[i] == col[k] : 같은 열에 놓이게 되므로, 유망하지 않다

## 유망의 조건 2 : 대각선 체크
* ![3](https://user-images.githubusercontent.com/74780115/160090841-c0dea139-c7c0-4404-9f26-3613ff8c7764.PNG)
* col[i] - col[k] == i - k

