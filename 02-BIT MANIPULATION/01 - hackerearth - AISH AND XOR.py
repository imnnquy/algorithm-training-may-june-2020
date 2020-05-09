# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/aish-and-xor-2/


def solution():
    N = int(input())
    array = list(map(int, input().strip().split()))
    count_1 = []
    for i in range(N):
        count_1.append((count_1[i - 1] if i > 0 else 0) + array[i])
    Q = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        total_1 = count_1[R - 1] - (count_1[L - 2] if L >= 2 else 0)
        total_0 = R - L + 1 - total_1

        print(total_1 % 2, total_0)


solution()
