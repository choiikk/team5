#11053 "가장 긴" 증가하는 부분수열(성공!!!!!)
import sys
input=sys.stdin.readline

A = int(input()) #수열의 크기
arr=list(map(int,input().split(' ')))

sizes=list(1 for i in range(A)) #i번째 element로 끝나는 부분 수열의 크기. 일단 자기 자신 하나
for i in range(A):
    for j in range(i): #자기보다 이전에서 끝나는 부분수열들 순회
        if arr[j]<arr[i] and sizes[j]+1>sizes[i]: 
            #조건1. 자기(i번째)가 j번째보다 더 큼
            #조건2. 이 j번째 뒤에 붙는게 현재보다 더 길어지는 경우임
            sizes[i]=sizes[j]+1

print(max(sizes))

