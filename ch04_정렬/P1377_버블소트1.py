import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))  # A = [(10,0),(1,1),(5,2),(2,3),(3,4)]
Max = 0
sorted_A = sorted(A)             # sorted_A = [(1,1),(2,3),(3,4),(5,2),(10,0)]
for i in range(N):
    if Max < sorted_A[i][1] - i:    # ch04_정렬 전 index - ch04_정렬 후 index 계산의 최댓값 저장하기
        Max = sorted_A[i][1] - i
print(Max + 1)