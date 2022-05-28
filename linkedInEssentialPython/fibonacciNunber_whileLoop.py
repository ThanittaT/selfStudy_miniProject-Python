words = ['one','two','three','four']

a,b = 0,1
while b < 1000:
  print(b, end = ' ', flush = True)
  a, b = b, a+b    #This is fibonucci operation
print()

"""
------Expected Result: While-Loop----

1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
"""

for i in words:
  print(i)

"""
---------Expected Result: For-Loop------
one
two
three
four
"""