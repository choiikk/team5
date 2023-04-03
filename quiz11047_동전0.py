#11047 동전 0 (실패. 아무리봐도 맞는거같은데 틀림 ㅜㅜ)
from queue import PriorityQueue
import sys
input = sys.stdin.readline

#입력
N, K = map(int, input().split(" "))
print(N, K)
coins = PriorityQueue()
for i in range(N):
    coins.put((-1)*(int(input())))#내림차순 정렬을 위해 음수로 바꿔서 큐에 저장한다

#큰 액수의 동전으로 먼저 나눈 값. -> 남는 돈을 점점 더 작은 액수의 동전으로 나눈 값->최소 액수의 동전까지 반복

count=0 #동전의 수
while K>0: #K를 모두 동전으로 구성해서 남는 금액이 0이 되면 반복 종료
    coin=coins.get()*(-1) #내림차순 정렬을 위해 음수로 바꿨으니까, 양수로 돌려놓기
    count+= (K//coin) #동전개수 = 몫
    K%=coin #지금 액수의 동전으로 구성하고 남는 금액으로 K값을 업데이트한다 


print(count)