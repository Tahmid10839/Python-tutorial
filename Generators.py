
'''

Iterable = __iter__() or __getitem__()
Iterator = __next__()
Iteration

'''

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

t = "Tahmid"
i = iter(t)
print(i.__next__())
print(i.__next__())

print("Fibonacci series using generators:")
def getFibonacci():
    a, b = 0, 1

    while True:
        yield b
        b = a + b
        a = b - a

for num in getFibonacci():
    if num > 100:
        break
    print(num)

print("Factorial using generators:")
def gen1(g):
    fact = 1
    start = 1
    for i in range(g):
        yield fact
        start = start + 1
        fact = fact * start

func = gen1(10)
for i in func:
    print(i)