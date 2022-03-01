# Day 5
# Problem 5
# Date 14 Feb 2022
# Time 6:30 AM

# implement car and cdr


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    return f.__closure__[0].cell_contents


def cdr(f):
    return f.__closure__[1].cell_contents


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
