
# Palindromify the list

def next_palindrome(n):
    n+=1
    while is_palindrome(n)==False:
        n+=1
    return n
def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__ == '__main__':
    size = int(input("Enter the size of your list:"))
    l = []
    for i in range(size):
        l.append(int(input("Enter the number:")))

    print(f"The original list: {l}")

    print(f"Output List: {[l[i] if l[i]<10 else next_palindrome(l[i]) for i in range(len(l))]}")

