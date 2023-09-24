def solve(s):
    n = len(s)
    half = n // 2
    sum1, sum2 = 0, 0

    for i in range(half):
        sum1 += ord(s[i]) - ord('A')
        sum2 += ord(s[i + half]) - ord('A')

    result = []
    for i in range(half):
        c1 = ord(s[i]) - ord('A')
        c2 = ord(s[i + half]) - ord('A')
        c = (c1 + sum1) % 26
        c = (c + c2 + sum2) % 26
        result.append(chr(c + ord('A')))

    return ''.join(result)

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        print(solve(s))
