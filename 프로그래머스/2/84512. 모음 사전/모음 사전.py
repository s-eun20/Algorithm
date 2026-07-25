def solution(word):
    vowels = ["A","E","I","O","U"]
    words = []
    
    def dfs(now) :
        if now :
            words.append(now)
        if len(now) == 5 :
            return
        
        for v in vowels :
            dfs(now+v)
    dfs("")
    
    return words.index(word) + 1