# 실패율

def solution(n, stages):
    player_cnt=[0]*(n+2)
    for s in stages:
        player_cnt[s-1]+=1
    
    player=len(stages)
    failure=[ [i,0] for i in range(1,n+1)]

    for i in range(n):
        failure[i][1]=player_cnt[i]/player
        player-=player_cnt[i]
        if player==0:
            break
    failure.sort(key=lambda x: (-x[1], x[0]))

    result=[]
    for idx,_ in failure:
        result.append(idx)
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))