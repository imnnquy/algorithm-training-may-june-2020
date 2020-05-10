# https://www.hackerrank.com/challenges/sansa-and-xor/problem


def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        array = list(map(int, input().strip().split()))
        answer = 0
        for i in range(N):
            if (i + 1) % 2 == 1 and (N - i) % 2 == 1:
                answer ^= array[i]

        print(answer)


solution()
