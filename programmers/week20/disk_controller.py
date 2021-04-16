# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[1])
    print(jobs)
    hap=0
    start=0
    for _,j in jobs:
        
    return answer

jobs=[[0, 3], [1, 9], [2, 6]]
print(solution(jobs))