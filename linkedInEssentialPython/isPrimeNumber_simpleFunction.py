# --This is simple function
def function(n):
    print(n)


function(43)  # --This is call function

"""
-----Expected Result: ----
43
"""


# --This function with set parameter equal 1
def function_with_index(n=1):
    print(n)


function_with_index()

"""
------Expected Result: ------
1
"""


# --This is function for checking prime number
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


n = 5
if isprime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not prime number.")

"""
------Expected Result: isPrime number----
5 is a prime number.
"""


# --This is function for checking prime number
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_prime():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)


n = 5
if isprime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not prime number.")

list_prime()

"""
---------Expected Result: For list_prime function---
43
1
5 is a prime number.
5 is a prime number.
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
"""