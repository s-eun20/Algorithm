def solution(numbers, hand):
    answer = ''
    keypad = {
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        5 : (1,1),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2),
        "*" : (3,0),
        0 : (3,1),
        "#" : (3,2)
    }
    left = "*"
    right = "#"
    for number in numbers :
        
        if number == 1 or number == 4 or number == 7 :
            answer += "L"
            left = number
        elif number == 3 or number == 6 or number == 9 :
            answer += "R"
            right = number
        else :
            lr,lc = keypad[left]
            rr,rc = keypad[right]
            nr,nc = keypad[number]
            distance_l = abs(lr - nr) + abs(lc - nc)
            distance_r = abs(rr - nr) + abs(rc - nc)
            if distance_l > distance_r :
                answer += "R"
                right = number
            elif distance_l < distance_r :
                answer += "L"
                left = number
            else :
                if hand == "right" :
                    answer += "R"
                    right = number
                else :
                    answer += "L"
                    left = number
                    
    return answer