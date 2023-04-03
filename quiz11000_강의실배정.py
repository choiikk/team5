#11000 강의실배정(실패) 왜 틀렸는지 모르겠다 ㅜㅜ 
from queue import PriorityQueue
import sys
input = sys.stdin.readline 
N = int(input())
lectures=list()

for i in range(N):
    S, T = map(int, input().split(' '))
    lectures.append((S,T))
lectures.sort()# (강의) 시작 시간 기준으로 오름차순 정렬

rooms = PriorityQueue() # 강의실
rooms.put(lectures[0][1]) # 강의실에는 종료시간만 저장해 놨다가, 다음 배정할 강의의 시작시간과 비교하는데 쓴다


for i in range(1,N):
    nextLecStart = lectures[i][0]
    nextLecEnd = lectures[i][1]



    # if rooms[0] <= nextLecStart:#이어서 수업 가능 (새로운 강의실 필요 없음)
    #     rooms.get() #이어서 수업할거니까 현재 종료 시간을 삭제 
    # rooms.put(nextLecEnd) #이어서 수업한다면 종료시간을 업데이트 한 것이고, 이어서 수업할 수 없다면 강의실을 추가한 것이다
        #우선순위큐는 인덱스 쓸 수 없다.......
    
    
    if rooms.get() <= nextLecStart:#이어서 수업 가능 (새로운 강의실 필요 없음)
        rooms.put(nextLecEnd) #이어서 수업한다면 종료시간을 업데이트
    else:
        rooms.put(lectures[0][1])
        rooms.put(nextLecEnd) #이어서 수업할 수 없다면 강의실 추가 
    
print(rooms.qsize())
        

