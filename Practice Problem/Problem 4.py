
# The next Palindrome

def next_palindrome(n):
    n = n+1
    while is_palindrome(n)==False:
        n += 1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]
if __name__ == '__main__':
    n = int(input("Enter the number of test cases:"))
    l = []
    for i in range(n):
        l.append(int(input("Enter the number:")))

    for i in range(len(l)):
        print(f"Next Palindrome for {l[i]} is {next_palindrome(l[i])}")
