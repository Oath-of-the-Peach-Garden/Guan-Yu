# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0
    n=len(jobs)
    jobs.sort(key=lambda x: x[0])
    time=jobs[0][0]
    queue=[]
    while True:
        while jobs and jobs[0][0]<=time:
            r_time, p_time=jobs.pop(0)
            heapq.heappush(queue, [p_time, r_time])
        if not queue:
            if jobs:
                r_time, p_time=jobs.pop(0)
                heapq.heappush(queue, [p_time, r_time])
                time=r_time
            else:
                break
        process_time, request_time=heapq.heappop(queue)
        answer+=(time-request_time)+process_time
        time+=process_time
    return answer//n

jobs=[[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))#15
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))#74
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))#72
print(solution([[2, 8]]))