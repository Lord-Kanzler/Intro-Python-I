# Write a program to determine if a number, given on the command line, is
# prime.

# 1. How can you optimize this program?
# 2. Implement[The Sieve of
#              Eratosthenes](https: // en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
# of the oldest algorithms known(ca. 200 BC).

# Testing
num = int(input("Enter a integer number: "))
# given number is greater than 1
if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2, num):

        # If num is divisible by any number between 2 and n / 2, it is not
        # prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")


# optimized to to be wrapped in a function instead of for loops.
num = int(input("Enter a integer number: "))


def Prime(num):

    # For corner cases
    if num <= 1:
        return False
        # print("false")

    if num <= 3:
        return True
        # print("true")

    # This is checked so that we can skip middle five numbers in below loop
    if num % 2 == 0 or num % 3 == 0:
        return False
        # print("false")

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
            # print("false")
        i = i + 6

    return True
    # print("true")


# Program output:
if Prime(num):
    print("IS PRIME!")
else:
    print("NOT PRIME!")
