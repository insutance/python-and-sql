import collections

def solution(s):
    s = s.upper()
    dic = collections.Counter(s)
    
    if dic['P'] == dic['Y'] or (not dic['P'] and not dic['Y']):
        return True
    else:
        return False

# upper(), lower()
# isupper(), islower() 반환형 => Bool
# collection.Counter() 반환형 => dictionary

"""
s.lower().count('p') == s.lower().count('y')

#1. count() 함수를 통해 문자열 내에서 원하는 문자를 찾을 수 있음
#2. count(self, x, __start, __end)
"""