def makeZero(A, n):
    xor = 0
    isZero = True

    for i in range(n):
        if A[i] > 0:
            isZero = False
        xor ^= A[i]

    if isZero:
        return "YES"
    elif xor == 0:
        return "YES"
    else:
        return "NO"

# Example usage
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print(makeZero(A, n))
