#성공
import sys
input = sys.stdin.readline


def DFS(x,y):
    visited[x][y]=1
    global apts #이 단지에 아파트 몇채인지 저장
    if graph[x][y]==1: 
        apts+=1 #아파트 수 추가
    for i in range(4): #동서남북 이웃 조사
        xNext=x+xMove[i]
        yNext=y+yMove[i]
        if(0<=xNext<N and 0<=yNext<N and visited[xNext][yNext]==0 and graph[xNext][yNext]==1):
            # 동서남북 이동이 가능하고(그래프의 끝이 아니고), 이동 할 곳이 아직 방문 안한 집(1)이면 
            DFS(xNext,yNext) #이동해서 또 다음 이웃들 조사하기
            


N = int(input())
graph=list()
for i in range(N):
    graph.append(list(map(int, input().rstrip())))
visited = [[0]*N for i in range(N)] #0이면 방문 안한거, 1이면 방문 한거

#동서남북 이동
xMove=[-1,1,0,0]
yMove=[0,0,-1,1]


aptsList=list()#아파트 단지 당 아파트 몇채인지
apts=0 #아파트 몇채인지
for x in range(N):
    for y in range(N):
        if(graph[x][y]==1 and visited[x][y]==0):
            DFS(x,y)
            aptsList.append(apts)
            apts=0 #다음 단지의 아파트수 세기 위해 0으로 초기화



print(len(aptsList))
for apts in sorted(aptsList):
    print(apts)
    
