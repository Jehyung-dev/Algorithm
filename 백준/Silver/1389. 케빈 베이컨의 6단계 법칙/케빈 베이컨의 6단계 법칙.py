# 케빈 베이컨의 6단계 법칙

from collections import deque  # 큐를 사용하기 위함


def BFS(n):  # BFS함수
    Q = deque([n])
    visited = [0] * (N + 1)  # 방문 확인을 위함
    visited[n] = 1

    while Q:  # 큐가 빌 때까지 반복
        num = Q.popleft()
        for j in graph[num]:  # 해당 수의 친구들을 넣어 반복
            if not visited[j]:  # 방문 확인
                visited[j] = visited[num] + 1  # 이전 방문 횟수 +1번
                if visited.count(0) == 1:  # 인덱스 0을 제외하고 다 방문했다면 리턴
                    return sum(visited)  # 일반 방문횟수보다 +1 되어있지만, 전체적인 합으로 비교 가능
                Q.append(j)  # 방문하지 않은 곳이 있다면 다시 큐에 추가


N, M = map(int, input().split())  # N : 유저의 수 / M : 관계의 수
graph = [[] for _ in range(N + 1)]  # graph : 교우 관계
ans = 0
min_val = int(1e9)


for _ in range(M):  # M만큼 반복
    A, B = map(int, input().split())  # A와 B는 서로 친구 관계
    graph[A].append(B)
    graph[B].append(A)

for i in range(N, 0, -1):  # 역순으로 BFS에 대입
    tmp = BFS(i)
    if tmp <= min_val:  # 케빈 베이컨이 적은 경우 갱신
        min_val = tmp
        ans = i

print(ans)
