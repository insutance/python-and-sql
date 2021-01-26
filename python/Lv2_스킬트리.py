def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = ""                                  # 하나의 스킬트리를 뽑을 때마다 s, index 초기화
        index = 0                   
        for ch in skill_tree:
            if ch in skill:                     # 스킬트리에 skill이 있다면 s에 추가
                s += ch
                if s[index] != skill[index]:    # 인덱스 값이 다르다면 s를 -1 변경 후 break
                    s = "-1"
                    break
                index += 1                      # s[index]==skill[index] 면 index값 +1
        if s != "-1":                           # s가 -1이 아니라면(=제대로 된 스킬트리라면) count += 1
            count += 1
    
    return count

def solution2(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = ""                      # 하나의 스킬트리를 뽑을 때마다 s 초기화
        for ch in skill_tree:       
            if ch in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
                s += ch
        
        if skill[:len(s)] == s:     # 만든 s를 기준으로 skill과 같다면 count += 1
            count += 1
    
    return count
        

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2
print(solution("ABC", ["DEF"]))     # 1
print(solution("CBD", ["CAD"]))     # 0
print(solution("CBD", ["AEF", "ZJW"]))  # 2
print(solution("REA", ["REA", "POA"]))  # 1
print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]))  # 4
print(solution("BDC", ["AAAABACA"]))    # 0
print(solution("CBD", ["C", "D", "CB", "BDA"])) # 2