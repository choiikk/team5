#10844 쉬운 계단수(성공)
import sys 
input = sys.stdin.readline

N = int(input()) #N자리수
num = [[0 for col in range(10)] for row in range(N+1)] #2차원리스트 num[몇자리수인지][그 자리수의 숫자]=경우의 수를 저장
for j in range(1,10):
    num[1][j]=1; #한자리수는 경우의 수 1개

for i in range(2,N+1): #두자리수 부터 N자리수
    for j in range(10): #0~9
        if j==0: #ㅁㅁㅁㅁ0 
            num[i][0]=num[i-1][1]
        elif j==9: #ㅁㅁㅁㅁ9 
            num[i][9]=num[i-1][8]
        else: #그 외 일반적인 경우
            num[i][j] = num[i-1][j-1] + num[i-1][j+1]
    
#N자리수일때, 경우의 수 총 합 구하기
sum=0
for j in range(10):
    sum += num[N][j]

print(sum%1000000000)







