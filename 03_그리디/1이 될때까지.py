"""
n이 k로 나누어 떨어지면 k로 나누고 
아니면 1을 뺀다

"""

n, k = map(int, input().split())

count = 0

while n >= k:
    # k가 1인 경우
    if k == 1:
        count = n
        break
    
    if n % k == 0:
        n = n / k
        count += 1
    else:
        n -= n % k
        count += n % k
    
print(count)