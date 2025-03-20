T = int(input())

for _ in range(T) :
    K = int(input())
    N = int(input())
    
    apt = [[0]*(N+1) for _ in range(K+1)]
    
    for i in range(1,N+1):
        apt[0][i] = i
        
    for i in range(1,K+1):
        for j in range(1,N+1):
            apt[i][j] = apt[i][j-1]+apt[i-1][j]
    
    
    print(apt[K][N])