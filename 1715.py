import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    card = card1 + card2
    result += card
    heapq.heappush(cards, card)
    
print(result)