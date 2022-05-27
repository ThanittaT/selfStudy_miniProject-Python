
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("This number is a prime.")
        else:
            print("It's not a prime number")

#-----This code for input checking number from user
n = int(input("Check this number:  "))
prime_checker(number=n)

"""
----------Expected Result:-----------
:::::::::::::
1.When input = 6
Check this number:  6
It's not a prime number
It's not a prime number
It's not a prime number
It's not a prime number

:::::::::::::

2.When input = 3
Check this number:  3
This number is a prime.

:::::::::::::

3.When input = 4
Check this number:  4
It's not a prime number
It's not a prime number

:::::::::::::
4.When input = 5
Check this number:  5
This number is a prime.
This number is a prime.
This number is a prime.

"""
