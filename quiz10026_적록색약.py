#실패: DFS 함수가 안끝남 ㅜㅜ 
import sys
input=sys.stdin.readline

def DFS(x,y):
    visited[x][y]==1
    for i in range(4):
        xNext=x+xMove[i]
        yNext=y+yMove[i]
        if(0<=xNext<N and 0<=yNext<N and visited[xNext][yNext]==0 and graph[xNext][yNext]==graph[x][y]):
            # 동서남북 이동이 가능하고(그래프의 끝이 아니고 아직 방문 안함), 이동 할 곳이 지금과 같은 색깔 구역이면
            DFS(xNext,yNext) #이동해서 주변 색 조사해서 같은 색이면 visited로 만들기

N = int(input())
graph=list()
for i in range(N):
    graph.append(list(input().strip()))
visited = [[0]*N for i in range(N)] 

#동서남북 이동
xMove=[-1,1,0,0]
yMove=[0,0,-1,1]

normal=0#정상인이 본 구역의 수
for x in range(N):
    for y in range(N):
        if(visited[x][y]==0):
            DFS(x,y)
            normal+=1
print(normal)

visited = [[0]*N for i in range(N)] 
for x in range(N):
    for y in range(N):
        if graph[x][y]=='R':
            graph[x][y]=='G' #색약이보기에는 G==R

blind=0#색약이 본 구역의 수
for x in range(N):
    for y in range(N):
        if(visited[x][y]==0):
            DFS(x,y)
            blind+=1
print(blind)