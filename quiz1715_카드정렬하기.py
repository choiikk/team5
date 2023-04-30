#1715 카드정렬하기(성공)
import sys
input = sys.stdin.readline
from queue import PriorityQueue

#입력
N = int(input()) 
cards=PriorityQueue()#누적합을 구하는 문제이므로, 작은수부터 누적해서 더하는 것이 결과가 최소값이 된다. (오름차순)
for i in range(N):
    cards.put(int(input()))

sum=0#결과

while cards.qsize()>1:
    tempSum=cards.get()+cards.get() #첫번째로 작은 묶음, 두번째로 작은 묶음
    sum+= (tempSum)#결과에 더함
    cards.put(tempSum)# 이것도 다른 카드들과 비교할 새로운 묶음이니까 다시 우선순위큐에 넣어줌

#출력
print(sum)