#14889 스타트와 링크(전혀 모르겠어요 ㅠㅠ)
import sys
input = sys.stdin.readline

N= int(input().strip())
table = list()

for row in range(N):
    table.append(list(input().strip().split(' ')))

#combination, 차: 절댓값 

