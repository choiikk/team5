#성공
import sys
input = sys.stdin.readline
from collections import deque
N=int(input()) #컴퓨터 수
C = int(input()) #연결 개수
graph = [[0]*N for i in range(N)]
for i in range(C):
    x,y = map(int, input().split(' '))
    x-=1
    y-=1 #graph 인덱스랑 맞추기 위해
    graph[x].append(y)
    graph[y].append(x)

visited=list(0 for i in range(N)) #방문한 컴퓨터는 1, 방문 안한거면 0

#0번째 컴퓨터(1번컴퓨터) 부터 탐색
visited[0]=1
queue=deque([0]) 

def BFS(x,y):
    while queue:
        #print("test")
        now=queue.popleft()
        for nextC in graph[now]:
            if visited[nextC]==0:
                queue.append(nextC)
                visited[nextC]=1

BFS(0,0)

print(sum(visited)-1) #1번 컴퓨터 빼고 바이러스 걸린 컴퓨터



