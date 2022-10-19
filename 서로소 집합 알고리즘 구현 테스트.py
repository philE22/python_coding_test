#팀 합치기 함수
def union_team(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a > b : 
    parent[a] = b
  else:
    parent[b] = a
  
#팀 확인 함수 -> 해당 원소의 부모 원소찾는 함수
def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

#입력 처리
e, v = map(int, input().split())

parent = [0] * (e + 1)

#부모 테이블 초기화
for i in range(1, e + 1):
  parent[i] = i

#마지막 프린트를 위한 리스트
list = []
  
#0, 1에 따라 union, find 수행
for i in range(v):
  check, a, b = map(int, input().split())
  #union
  if check == 0:
    union_team(parent, a, b)

  #find
  else:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
      list.append('YES')
    else:
      list.append('NO')
#결과 프린트 zz
for i in list:
  print(i)