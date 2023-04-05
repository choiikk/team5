#1946 신입사원(실패 (답은 나오는거 같은데 시간초과, 어떻게 greedy 알고리즘으로 푸는지 모르겠다))
import sys
input = sys.stdin.readline

T = int(input())
testCases=list() #테스트 케이스들의 리스트
for i in range(T): 
    N = int(input())
    tempCase=list()#각 테스트 케이스
    for j in range(N):
        score1, score2 = map(int, input().split(' '))#서류점수, 면접점수
        tempCase.append((score1,score2))#튜플로 저장
    testCases.append(tempCase) #각 테스트 케이스를 테스트 케이스들의 리스트에 저장

#불합격 조건: 본인(i)이 속한 테스트 케이스에서, 서류와 면접 모두 순위가 높은(숫자가 작은) 사람(비교상대:j)이 있으면 나는 불합격
for tempCase in testCases:
    count=0 #각 테스트케이스 당 합격자 수
    for i in tempCase:
        ok = True #default는 합격
        for j in tempCase:
            if i[0]> j[0] and i[1]>j[1]: #불합격조건
                ok = False
        if ok:
            count+=1
    print(count)#결과 출력