def solution(s):
    stack = []
    for ch in s:
        if not stack and ch == ')':     # stack이 비었는데 ')'가 들어온다면
            return False                # False
        
        if ch=='(':                     # '(' 는 stack에 계속해서 추가
            stack.append(ch)    
        elif ch==')':                   # ')' 이라면 stack에서 마지막 문자를 pop
            stack.pop()
    
    if stack:                           # push, pop 상황이 다 끝났는데도 stack에 괄호가 남아있다면
        return False                    # False
        
    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("())))))"))