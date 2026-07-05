from datetime import datetime
def solution(today, terms, privacies):
    months = {}
    result = []
    
    for term in terms :
        word, month = term.split()
        months[word] = int(month)
        
        
        
    year2,month2,day2 = map(int, today.split("."))
    today_date = year2 * 12 * 28 + month2 * 28 + day2
    
    for i,privacy in enumerate(privacies) :
        pre, word = privacy.split()
        year, month, day = map(int, pre.split("."))
        pre_date = year * 12 * 28 + month * 28 + day
        if today_date- pre_date >= months[word] * 28 :
            result.append(i+1)
        
    return result
    
    