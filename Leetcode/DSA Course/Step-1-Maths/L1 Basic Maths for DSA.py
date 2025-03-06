# Count digits

# Reverse a number

# Check palindrome

# Armstrong Number
# 371 = 3³ + 7³ + 1³
# 1634 = 1³ + 6³ + 3³ + 4³

# Print all divisors
n = 36
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print(divisors)

divisors = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if n // i != i:
            divisors.append(n // i)
divisors.sort()
print(divisors)

# Prime number check
# Exactly 2 factors 1 & number itself

n = 7
cnt = 0
for i in range(1, int(n ** .5) + 1):
    if n % i == 0:
        cnt += 1
        if n // i != i:
            cnt += 1
if cnt == 2:
    print("true")
else:
    print("false")

# GCD/HCF Greatest Common Divisor/ Highest Common Factor

n1 = 20
n2 = 40
ans = 0
for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        ans = i
print(ans)

# Euclidean Algorithm
# n1, n1
# gcd(n1, n2) = gcd(n1 - n2, n2)
# gcd(a, b) = gcd(a - b, b)
# a > b
# gcd(a, b) = gcd(a % b, b)

a = 40
b = 20

while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(max(a, b))
