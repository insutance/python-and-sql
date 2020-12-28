def solution(s):
    answer = list()
    for word in s.split(' '):
        word = list(word)
        for i in range(len(word)):
            if i % 2 ==0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
            
        answer.append("".join(word))
        print(answer)
    
    return " ".join(answer)

print(solution("hello world"))

#1. 문자열 s를 split(' ')을 사용해 나눈다.
### 내가 이상한 건지, split()은 기본적으로 공백을 기준으로 나눈다고 생각하는데
### s.split() 을 사용하면 테스트에서 오류발생하고, s.split(' ')이면 오류가 발생하지 않는다..

#2. 해당 word를 리스트로 만들어준다
### 그 후 upper(), lower()를 통해 대소문자로 변환해주고

#3. join()을 통해 다시 word를 묶어서 answer 배열에 넣어준다
#4. 마지막으로 " ".join(answer) 는 단어를 조인할 때 띄어쓰기를 넣어달라는 뜻이다.