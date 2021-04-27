# 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    graph=[[0]*(m+1) for _ in range(n+1)]
    for x,y in puddles:
        graph[y][x]=-1
    graph[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if graph[i][j]==-1:
                continue
            if graph[i-1][j]!=-1:
                graph[i][j]=(graph[i][j]+graph[i-1][j])%1000000007
            if graph[i][j-1]!=-1:
                graph[i][j]=(graph[i][j]+graph[i][j-1])%1000000007
    answer=graph[n][m]
    return answer

print(solution(4,3,[[2,2]]))