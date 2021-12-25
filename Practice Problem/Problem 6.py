
# Guess the number
import random
def guess(a,b,actual):
    g = int(input(f"Guess a number between {a} and {b}:"))
    n = 1
    while g!=actual:
        if g>actual:
            print("Guess wrong")
            g = int(input("Enter a smaller number:"))
            n+=1
        else:
            print("Guess wrong")
            g = int(input("Enter a bigger number:"))
            n+=1
    print("Guess correct")
    print(f"You have completed the game with {n} guesses\n")
    return n


if __name__ == '__main__':
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    actual1 = random.randint(a,b)
    print("-----Player1's Turn------")
    g1 = guess(a,b,actual1)
    print("------Player2's Turn------")
    actual2 = random.randint(a,b)
    g2 = guess(a,b,actual2)

    if g1<g2:
        print("Player1 won the match\n")
    elif g1>g2:
        print("Player2 won the match\n")
    else:
        print("It's a tie")
    print(f"Player1 has the number {actual1} and Player2 has the number{actual2}")
