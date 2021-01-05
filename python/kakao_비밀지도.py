def addZero(n, num):
    if len(num) < n:
        for i in range(n-len(num)):         # n(자리수)보다 적다면 앞에 0을 추가해줘야하므로 이런식으로 코드를 짰다.
            num = '0' + num                 # for문을 돌리지 말고 num = '0' * (n-len(num)) + num  이렇게 했어도 될 것 같다.
    return num

def solution(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1,arr2):
        x, y = bin(x)[2:], bin(y)[2:]       # bin(숫자) => 2진수로 만들어줌 0b2진수 이렇게 나오기 때문에 [2:] 해줌
        x, y = addZero(n,x), addZero(n,y)
        
        s = ''
        for c,d in zip(x,y):
            if c == d == '0':               # c와 d가 같고 그게 0과 같다면 공백을 추가
                s += ' '
            else:                           # 아니면 #을 추가
                s += '#'
        
        answer.append(s)

    return answer



def solution2(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1, arr2):
        a12 = str(bin(x | y)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    
    return answer

print(solution2(5, [9,20,28,18,11], [30,1,21,17,28]))
