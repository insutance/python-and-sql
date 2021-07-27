def solution(numbers, hand):
    answer = ""
    keypad = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    }

    lHand = "*"
    rHand = "#"

    for number in numbers:
        if number in [1,4,7]:
            answer += "L"
            lHand = number
        elif number in [3,6,9]:
            answer += "R"
            rHand = number
        else:
            loc_Number = keypad[number]
            loc_lHand = keypad[lHand]
            loc_rHand = keypad[rHand]

            dis_L = abs(loc_Number[0]-loc_lHand[0]) + abs(loc_Number[1]-loc_lHand[1])
            dis_R = abs(loc_Number[0]-loc_rHand[0]) + abs(loc_Number[1]-loc_rHand[1])

            if dis_L > dis_R :
                answer += "R"
                rHand = number
            elif dis_L < dis_R :
                answer += "L"
                lHand = number
            else:
                if hand == "left":
                    answer += "L"
                    lHand = number
                else:
                    answer += "R"
                    rHand = number
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
#print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))

"""
def solution2(numbers, hand):
    answer = ""
    loc_left = [3,0]
    loc_right = [3,2]
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

    for number in numbers:
        for i in range(len(keypad)):
            if number in keypad[i]:
                if keypad[i].index(number) == 0:
                    answer += "L"
                    loc_left = [i, keypad[i].index(number)]

                elif keypad[i].index(number) == 2:
                    answer += "R"
                    loc_right = [i, keypad[i].index(number)]

                else:
                    if abs(i - loc_left[0]) + abs(keypad[i].index(number) - loc_left[1]) > abs(i - loc_right[0]) + abs(keypad[i].index(number) - loc_right[1]):
                        answer += "R"
                        loc_right = [i, keypad[i].index(number)]
                    elif abs(i - loc_left[0]) + abs(keypad[i].index(number) - loc_left[1]) < abs(i - loc_right[0]) + abs(keypad[i].index(number) - loc_right[1]):
                        answer += "L"
                        loc_left = [i, keypad[i].index(number)]
                    else:
                        if hand == "left":
                            answer += "L"
                            loc_left = [i, keypad[i].index(number)]
                        else:
                            answer += "R"
                            loc_right = [i, keypad[i].index(number)]

    return answer
"""