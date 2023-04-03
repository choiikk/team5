#1759 암호만들기(모르겠음)
import sys
input = sys.stdin.readline

L, C = map(int,input().split(' '))

chars=list(input().split(' '))
chars.sort()#오름차순 정렬
tempCode=list()#L자리 암호

#L자리 암호를 어떻게 채우는지 모르겠다. (자리수가 정해져 있으면 그만큼 중첩 for문 만들면 되는데... )
#자음모음 조건은 알겠다
        # tempCode가 L자리의 암호일 때,
        # aeiou=0 #모음
        # others=0 #자음
        # for alphabet in codeTry:
        #     if alphabet=='a'or alphabet=='e'or alphabet=='i'or alphabet=='o'or alphabet=='u':
        #         aeiou+=1
        #     else:
        #         others+=1
        # if aeiou>=1 and others>=2 :
        #     print(''.join(tempCode))#결과 출력
       # list, len