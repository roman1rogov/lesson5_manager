import  math
def func(x):
    if x < 4:
        return x
y = filter(func, (3, 4, 9, 1))

print(list(y))


def f(x,y):
    return x + y
a = map(f,[2, 6, 1],[4, 3, 1])
print(list(a))

def math_pi():
    return math.pi
k = math.pi
print(k)

def math_sqrt():
    return math.sqrt(20)
print(math_sqrt())

def math_pow():
    return math.pow(2,3)
print(math_pow())

def math_hypot():
    return math.hypot(2,4)
print(math_hypot())




