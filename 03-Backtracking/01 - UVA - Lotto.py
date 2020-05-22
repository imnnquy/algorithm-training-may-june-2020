# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=382


def backtrack(prev, res, array):
    if len(res) == 6:
        print(*res)
    else:
        for i in range(prev + 1, len(array)):
            res.append(array[i])
            backtrack(i, res, array)
            res.pop(-1)


def solution():
    is_first = True
    while True:
        line = list(map(int, input().strip().split()))
        if line[0] == 0:
            return

        if not is_first:
            print()
        else:
            is_first = False

        backtrack(-1, [], line[1:])


solution()
