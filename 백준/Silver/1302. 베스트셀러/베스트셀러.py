from collections import Counter

# 입력
N = int(input())
books = [input() for _ in range(N)]

# 각 책의 판매 횟수를 카운트
book_counts = Counter(books)

# 가장 많이 팔린 책의 제목을 찾음
max_sold_title = sorted(book_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]

# 출력
print(max_sold_title)
