#1931 회의실배정(실패(시간초과)) 이게 왜 greedy 유형인지 모르겠다 
import sys
input = sys.stdin.readline
#가장 여러개(max) 연결(중간에 시간 뜰 수도 있음) 될 수 있는 회의들의 경우를 찾는다. 
N = int(input())
meetings = list()
for i in range(N): 
    S, T = map(int, input().split(' '))
    meetings.append((T,S))#끝나는 시간 기준으로 오름차순 정렬
meetings.sort() 

max=0
while len(meetings): #시간초과가 뜨면 while문을 돌리면서 규칙이 있어서 반복을 (빨리끝내거나) 줄일수있는지 본다
    possibleMeetings =list()#(겹치지 않아서) 이 회의실에서 가능한 회의 구성
    possibleMeetings.append(meetings.pop(0))
    for nextMeeting in meetings:
        if possibleMeetings[-1][0]<=nextMeeting[1] : # 가능한 회의 리스트의 가장 늦은 회의의 끝시간보다, 다음 회의의 시작시간이 더 늦다면
            possibleMeetings.append(nextMeeting) #다음 회의는 이 회의실에서 할 수 있다
    if len(possibleMeetings)>max:
        max=len(possibleMeetings)

print(max)
