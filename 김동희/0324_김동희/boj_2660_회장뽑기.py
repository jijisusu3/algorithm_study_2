import sys; sys.stdin=open('boj_2660_회장뽑기.txt')

'''
문제 : 회장은 회원들 중에서 점수가 가장 작은 사람이 된다
입력 : 첫째 : 회원의 수(N) / 둘째 : 한 줄에 두 개의 회원번호, 두 회원이 서로 친구 / 마지막은 -1이 두 개
출력 : 첫째 : 회장 후보의 점수와 후보의 수 / 둘째 : 회장 후보를 오름차순으로 모두 출력 
풀이 : BFS, graph, visit 한사람당 자신 제외 수 점수가 나옴. 점수의 합을 저장
'''
N = int(input())
graph = [[] for _ in range(N+1)]
visit = [[0] for _ in range(N+1)]
while True:
    a, b = map(int,input().split())
    if a == -1 and b == -1: break;
    graph[a].append(b)
    graph[b].append(a)

def BFS(c):
    q = [c]
    visit = [-1]*(N+1)
    visit[c] = 0
    while q:
        n = q.pop(0)
        for g in graph[n]:
            if visit[g]==-1:
                q.append(g)
                visit[g] = visit[n] + 1

    return max(visit)

ans = []
for i in range(1,N+1):
    ans.append(BFS(i))
min_v = min(ans)
print(min_v, ans.count(min_v))


for i in range(N):
    if min_v == ans[i]:
        print(i+1,end=' ')









