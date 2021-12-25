
# No od guesses
# print no of guesses left
# No of guesses he took to finish
# Game over

num = 18
no = 1
print("-----This is a Guessing Game------")
print("You have 5 guesses")
while(no<=5):
    a = int(input("Enter a number:"))
    if a<18:
        print("You have entered smaller numer please enter greater number")
    elif a>18:
        print("You have entered greater number please enter smaller number:")
    else:
        print("Congratulations.You have won")
        print("You have finished it with",no,"guesses take")
        break
    print(5-no,"guesses left")
    no =no+1

if (no>5):
    print("Game Over")



