from collections import deque

num = int(input())

card = deque(range(1, num + 1))

while len(card) > 1:
    card.popleft()  # 왼쪽 끝 요소를 삭제
    card.append(card.popleft())  # 왼쪽 끝 요소를 오른쪽 끝으로 이동

print(card[0])
