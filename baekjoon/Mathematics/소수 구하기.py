import sys

def is_prime(n):
    if n == 1:
        return (0)
    i = 2
    while i * i <= n:
        if n % i == 0:
            return (0)
        i += 1
    return (1)

M, N= map(int, input().split())

if M == 2:
    sys.stdout.write(str(M) + '\n');
if M == 1 and N >= 2:
    sys.stdout.write(str(2) + '\n')
    M += 2
if M % 2 == 0:
    M += 1
i = M
while i <= N:
    if is_prime(i):
        sys.stdout.write(str(i) + '\n')
    i += 2
