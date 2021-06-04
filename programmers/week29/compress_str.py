# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = int(1e9)
    n=len(s)
    if n==1:
        return 1
    for i in range(1,(n//2)+1):
        idx=i
        tmp=s[0:i]
        tmp_len=n
        tmp_cnt=0
        #print(f'{tmp} {s[idx:idx+i]} {tmp_cnt} {tmp_len}')
        while idx+i<=n:
            if tmp==s[idx:idx+i]:
                tmp_cnt+=1
                tmp_len-=i
            else:
                if tmp_cnt>0:
                    print(tmp_cnt)
                    tmp_len+=len(str(tmp_cnt+1))
                tmp_cnt=0
                tmp=s[idx:idx+i]
            idx+=i
            #print(f'{tmp} {s[idx:idx+i]} {tmp_cnt} {tmp_len}')
        if tmp_cnt>0:
            tmp_len+=len(str(tmp_cnt+1))
        #print(tmp_len)
        answer=min(answer, tmp_len)
    return answer

print(solution("aaaaaaaaaaaaaaaaaaaa"))