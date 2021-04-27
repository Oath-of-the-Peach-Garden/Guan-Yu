# 풍선 터트리기
# https://programmers.co.kr/learn/courses/30/lessons/68646

import heapq

def solution(a):
    n=len(a)
    if n==1:
        return 1
    answer = 2
    left=[]
    heapq.heappush(left, a[0])
    right=[]
    for j in range(1,n):
        heapq.heappush(right,a[j])
    
    i=1
    while i<n-1:
        add=0
        if left[0]>a[i]: # 왼쪽에 나보다 작은 숫자가 없는 경우
            heapq.heappush(left, a[i])
            add+=1
        
        if right[0]==a[i]:
            heapq.heappop(right)
            add+=1
        if add>1:
            add-=1
        answer+=add
        i+=1
    return answer

a=[-16,27,65,-2,58,-92,-71,-68,-61,-33]
#a=[9,-1,-5]
print(solution(a))