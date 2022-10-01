x = 10
y = 20


def Sum(a, b):
    return a + b

print(Sum(x, y))

def powerSq(a, b=2): # default argument is passed here
    return a ** b  # ** is power function

print(powerSq(4, 3))
print(powerSq(4))
