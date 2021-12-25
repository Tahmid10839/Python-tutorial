
def fact_recursive(n):
    if n==1:
        return 1
    return n*fact_recursive(n-1)

n = int(input("Enter a Number:"))
print(fact_recursive(n))


def fact_iterative(n):
    fact=1
    for i in range(n):
        fact = fact*(i+1)
    return fact


n = int(input("Enter a Number:"))
print(fact_iterative(n))
