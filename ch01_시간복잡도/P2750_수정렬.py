import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 증가

# 병렬 정렬(merge sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 두 리스트를 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소들 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 입력 처리
input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 병합 정렬 수행
sorted_numbers = merge_sort(numbers)

# 결과 출력
for num in sorted_numbers:
    print(num)
