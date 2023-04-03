#1931 회의실배정
from queue import PriorityQueue
import sys
input = sys.stdin.readline
#가장 여러개(max) 연결(중간에 시간 뜰 수도 있음) 될 수 있는 회의들의 경우를 찾는다. 
N = int(input())
meetings = PriorityQueue()
for i in range(N):
    S, T = map(int, input().split(' '))
    meetings.put((T,S))#끝나는 시간 기준으로 오름차순 정렬

max=0
while meetings.qsize()>=1:
    possibleMeetings =list(meetings.get())#(겹치지 않아서) 이 회의실에서 가능한 회의 구성
    for nextMeeting in meetings:#우선순위큐는 not iterable???!!!그러면 리스트로 한 다음에 sort함수로 정렬을 할까? 
        if possibleMeetings[-1][1]<=nextMeeting[0] : #가능한 회의 리스트의 가장 늦은 회의의 끝시간보다, 다음 회의의 시작시간이 더 늦다면
            possibleMeetings.append(nextMeeting) #다음 회의는 이 회의실에서 할 수 있다
    if len(possibleMeetings)>max:
        max=len(possibleMeetings)

print(max)
