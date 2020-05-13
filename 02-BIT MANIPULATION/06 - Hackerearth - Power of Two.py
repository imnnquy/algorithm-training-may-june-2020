# https://www.hackerearth.com/challenges/competitive/thoughtworks-singapore-codeathon-2015/algorithm/power-of-two-4/


def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        array = list(map(lambda ai: bin(int(ai))[2:], input().strip().split()))
        result = False
        for x in range(30):
            and_sum = (1 << 30) - 1
            for a_i in array:
                if len(a_i) >= x and a_i[len(a_i) - x - 1] == '1':
                    and_sum &= int(a_i, 2)
            if and_sum == (1 << x):
                result = True
                break
        if result:
            print('YES')
        else:
            print('NO')


solution()
