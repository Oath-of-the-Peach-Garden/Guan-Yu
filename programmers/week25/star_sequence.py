# 스타수열
# https://programmers.co.kr/learn/courses/30/lessons/70130

import heapq

def solution(a):
    answer = 0
    n=len(a)
    if n<2:
        return 0
    cnt_list=[0]*n
    max_cnt=0
    i=0
    while i<n:
        cnt_list[a[i]]+=1
        if i<n-1 and a[i]==a[i+1]:
            i+=1
        max_cnt=max(max_cnt, cnt_list[a[i]])
        i+=1
    answer=max_cnt*2
    return answer

a=[5,2,3,3,5,3]
print(solution(a))