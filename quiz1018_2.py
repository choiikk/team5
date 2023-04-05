#1018 체스판 다시 칠하기(성공)
import sys
input=sys.stdin.readline

#M,N입력
M, N = map(int,input().split(' '))

#보드 B W 입력
board =list() 
for i in range(M):
    board.append(list(input().strip()))

min=8*8
#print(board)
for i in range(M-7):
    for j in range(N-7):
        tempBoard=[row[j:j+8] for row in board[i:i+8]]#전체 2차원 리스트로부터 8x8 2차원 리스트를 잘라서 저장
        count1=0 #다시 칠해야 하는 정사각형 개수
        count2=0
        tempMin=0
        #w로 시작하는 체스판이랑 비교. count1
        for k in range(8):
            for l in range(8):
                if((k+l)%2==0):
                    if(tempBoard[k][l]!='W'):
                        count1+=1
                if((k+l)%2==1):
                    if(tempBoard[k][l]!='B'):
                        count1+=1
        #B로 시작하는 체스판이랑 비교. count2
        for k in range(8):
            for l in range(8):
                if((k+l)%2==1):
                    if(tempBoard[k][l]!='W'):
                        count2+=1
                if((k+l)%2==0):
                    if(tempBoard[k][l]!='B'):
                        count2+=1
        if(count1<count2):
            tempMin=count1
        else:
            tempMin=count2
        if(tempMin<min):
            min = tempMin
        
print(min)