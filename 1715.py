import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) != 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    card = card1 + card2
    result += card
    heapq.heappush(cards, card)
    
print(result)

# 10 20 40 50 60 70
# 0  1  2  3  4  5
# 5  5  4  3  2  1
# 총 6개의 카드를 섞음
# 총 횟수는 5번

# 10 20 / 10 20 40 / 10 20 40 50 / 10 20 40 50 60 / 10 20 40 50 60 70 / ~~ 