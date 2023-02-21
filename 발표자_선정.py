import random

list = ["김영민", "백승필", "신지훈", "정희윤"]
random_list = random.sample(list, 2)

print("1번 질문 : " + random_list[0])
print("2번 질문 : " + random_list[1])