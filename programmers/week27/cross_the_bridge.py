# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

def check(mid, stones, k):
    ck=0
    for s in stones:
        if s-mid<=0:
            ck+=1
        else:
            ck=0
        if ck>=k:
            return True
    return False

def solution(stones, k):
    min_num, max_num=1, 200000000
    while min_num < max_num-1:
        mid=(min_num+max_num)//2
        if check(mid, stones, k):
            max_num=mid
        else:
            min_num=mid
    return max_num

stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k=3
print(solution(stones, k))