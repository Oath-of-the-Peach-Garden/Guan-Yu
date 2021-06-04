# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for idx,abs in enumerate(absolutes):
        answer+=abs if signs[idx] else -abs
    return answer

absolutes=[4,7,12]
signs=[True,False,True]
print(solution(absolutes,signs))