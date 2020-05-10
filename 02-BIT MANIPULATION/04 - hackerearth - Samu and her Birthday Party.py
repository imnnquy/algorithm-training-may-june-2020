# https://www.hackerearth.com/ru/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/samu-and-her-birthday-party-1/


def solution():
    T = int(input())
    friends = []
    for _ in range(T):
        N, K = map(int, input().strip().split())
        for _ in range(N):
            friends.append(int(input(), 2))

        min_dishes = K
        for i in range(1, 1 << K):
            all_friends_fed = True
            for friend in friends:
                if i & friend == 0:
                    all_friends_fed = False
                    break
            if all_friends_fed:
                min_dishes = min(min_dishes, bin(i).count('1'))

        print(min_dishes)


solution()
