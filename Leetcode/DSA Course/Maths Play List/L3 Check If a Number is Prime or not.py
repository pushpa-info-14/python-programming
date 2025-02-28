def is_prime(n):
    cnt = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
    if cnt == 2:
        print("yes")
    else:
        print("no")


is_prime(7)
is_prime(8)
is_prime(11)
