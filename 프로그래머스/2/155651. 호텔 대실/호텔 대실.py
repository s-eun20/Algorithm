import heapq
def solution(book_time):
    new_book = []
    
    for start,end in book_time :
        sh,sm = map(int,start.split(":"))
        eh,em = map(int,end.split(":"))
        
        start_time = sh * 60 + sm
        end_time = eh * 60 + em + 10
        
        new_book.append((start_time,end_time))
        
    new_book.sort()
    
    rooms = []
    
    for start_time, end_time in new_book :
        # 가장 빨리 비는 방을 현재 손님ㅁ이 사용할 수 있는 경우
        if rooms and rooms[0] <= start_time :
            heapq.heappop(rooms)
        
        #현재 예약의 퇴실 시간 + 청소 시간(+10)을 저장
        heapq.heappush(rooms,end_time)
        
    return len(rooms)