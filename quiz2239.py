#2239 스도쿠 (전혀 모르겠어요 ㅠㅠ)
import sys
input = sys.stdin.readline

sudoku = list()
for i in range(9):
    sudoku.append(list(map(int, input().strip())))

for i in range(9):
    for j in range(9):
        if(sudoku[i][j]==0):#0인 칸 채우기-> 리스트에 저장
            

