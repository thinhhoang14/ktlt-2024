print("input the radius of the circle")
x = int(input())

# The following will call the Circle function using the value the user entered.
# Notice that this variable is called X' while the function uses 'Radius'. The value of
# 'x' is passed to the function.
print("Area is" + Circle(x))
