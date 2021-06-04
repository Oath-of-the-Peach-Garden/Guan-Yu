# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = [6,1]
    min_cnt=0
    max_cnt=0
    for l in lottos:
        if l in win_nums:
            min_cnt+=1
        if l==0:
            max_cnt+=1
    max_cnt+=min_cnt

    rank={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer=[rank[max_cnt],rank[min_cnt]]
    return answer

lottos=[44, 1, 0, 0, 31, 25]
win_nums=[31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))