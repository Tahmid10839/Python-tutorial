yearage = int(input("Enter the Age/Year of birth:"))
isage = False
isyear = False

if len(str(yearage))==4:
    isyear = True

elif len(str(yearage))==2:
    isage = True
else:
    print("There is a problem with your Age/Year of birth.")
    exit()


if (yearage<1900 and isyear):
    print("You seem to be the oldest person alive")
    exit()

if (yearage>2020):
    print("You are not yet born")
    exit()

if isage:
    yearage = 2020 - yearage

print(f"You will be 100 years old in {yearage+100}")

iyear = int(input("Enter the year you want to know your age:"))
print(f"You will be {iyear-yearage} years old in {iyear}")




