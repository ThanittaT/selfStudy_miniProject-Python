x = 42
y = 73

# ---This is simple type Syntax
# if x < y:
#  print('x < y : x is {} and y is {}'.format(x,y))


# ----This is easiest Syntax
if x < y:
    print('x < y : x is {} and y is {}'.format(x, y))
elif x > y:
    print('x > y : x is {} and y is {}'.format(x, y))
elif x == y:
    print('x = y : x is {} and y is {}'.format(x, y))
else:
    print('Do something else.')

"""
---------Expected Result: Section#2.2-------
x < y : x is 42 and y is 73

"""
