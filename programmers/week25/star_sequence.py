# 스타수열
# https://programmers.co.kr/learn/courses/30/lessons/70130

import heapq
from collections import Counter

def solution(a):
    answer = 0
    n=len(a)
    cnt_list=Counter(a).most_common()
    for k,v in cnt_list:
        if v<=answer:
            break
        max_cnt=0
        i=0
        while i<n-1:
            if (a[i]!=k and a[i+1]!=k) or a[i]==a[i+1]:
                i+=1
                continue
            i+=2
            max_cnt+=1
        answer=max(max_cnt, answer)
    answer=answer*2
    return answer

a=[5,2,3,3,5,3]
a=[0,0]
print(solution(a))