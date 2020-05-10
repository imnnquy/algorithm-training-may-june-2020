# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mattey-multiplication-6/


def solution():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().strip().split())
        bin_m = "{0:b}".format(M)
        bin_m_len = len(bin_m)

        result = []
        for i in range(bin_m_len):
            if bin_m[i] == '1':
                result.append(f'({N}<<{bin_m_len - i - 1})')

        print(*result, sep=' + ')


solution()
