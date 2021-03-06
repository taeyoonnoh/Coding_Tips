# 서로소 집합

## 기본 개념

* {1,2} 와 {3,4} 은 서로소
* {1,2} 와 {2,3} 은 서로소가 아니다

## 서로소 집합 자료구조

* union : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
* find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

## 과정
1. 합집합 연산을 확인하여, 서로 연결된 노드 A, B 를 확인
2. A 와 B 의 루트 노드 를 각각 찾기
3. 루트 노드의 부모 노드를 설정
4. 모든 합집한 연산을 처리할 때까지 1~3 과정을 반복

## 시간 복잡도
* 모든 노드를 거처야 하기 때문에 O(V)
* 만약 서로 연결되어 있다면 최종 부모 노드를 찾을 때까지 연산을 수행해야되기 때문에 최악의 경우 O(V)
  * 경로 압축 기법 활용!

==================================================================================================

# 사이클 판별
* 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있음

## 사이클 판별 알고리즘
1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
 * 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산을 수행
 * 루트 노드가 서로 같다면 사이클이 발생

2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복
