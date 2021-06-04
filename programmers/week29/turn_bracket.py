# 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    n=len(s)
    if n<2:
        return 0
    for i in range(n):
        stack=[]
        #stack.append(s[i])
        #print(s[i], end='')
        for j in range(n):
            idx=(i+j)%n
            #print(f'{idx} {s[idx]}')
            #print(s[idx], end='')
            if s[idx] in ('(','[','{'):
                stack.append(s[idx])
                continue
            elif stack and ((s[idx]==')' and stack[-1]=='(') or (s[idx]==']' and stack[-1]=='[') or (s[idx]=='}' and stack[-1]=='{')):
                stack.pop()
            else:
                #print('break')
                break
        else:
            if not stack:
                #print('answer')
                answer+=1

    return answer


s="[](){}"#3
#s="}]()[{"#2
#="[)(]"#0
#s="}}}"#0
#s='()'

print(solution(s))