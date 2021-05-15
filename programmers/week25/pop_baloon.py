# 풍선 터트리기
# https://programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    n=len(a)
    if n<=2:
        return n
    answer=2
    left=a[0]
    right=a[-1]
    for i in range(1,n-1):
        if left>a[i]:
            answer+=1
            left=a[i]
        elif right>a[-1-i]:
            answer+=1
            right=a[-1-i]
    return answer if left!=right else answer-1

a=[-16,27,65,-2,58,-92,-71,-68,-61,-33]
#a=[9,-1,-5]
print(solution(a))