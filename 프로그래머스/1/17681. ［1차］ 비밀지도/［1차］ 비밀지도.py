def solution(n, arr1, arr2):
    # 이진수 변환한 다음 하나씩 비교해서 합쳐야하나? 0이랑1이면 1이고 00이면 0 11이면 1
    # 이진수 변환한건 스트링으로 저장해서 비교하는게 나은가? 배열엔 1이면 # 아니면 " " 으로 저장하고?
    answer = []
    for number1,number2 in zip(arr1,arr2) :
        number1 = "{:0{}b}".format(number1, n)
        number2 = "{:0{}b}".format(number2, n)
        number1_str = str(number1)
        number2_str = str(number2)
        result = ""
        for i in range(n) :
            if number1_str[i] == "1" or number2_str[i] == "1" :
                result += "#"
            else :
                result += " "
        answer.append(result)
                
        
    
    return answer