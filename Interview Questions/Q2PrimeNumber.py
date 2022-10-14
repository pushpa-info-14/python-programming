

def is_prime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, int(num/2)):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


is_prime(407)
is_prime(209)
is_prime(19)
