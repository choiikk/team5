#1932 정수삼각형(성공)
import sys
input=sys.stdin.readline

n = int(input()) #삼각형의크기(n단 삼각형)
tri = list()
for i in range(n):
    tri.append(list(map(int,input().split(' '))))

for i in range(n-1):
    for j in range(0,n-1-i):
        #[n-2-i]: 아래줄부터 누적합 구해서 올라가기
        tri[n-2-i][j] += max(tri[n-1-i][j],tri[n-1-i][j+1])

print(tri[0][0])