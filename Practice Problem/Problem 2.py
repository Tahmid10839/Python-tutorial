# Divide the apples

try:
    n = int(input("Enter the number of apples:"))
    mn = int(input("Enter the minimum number:"))
    mx = int(input("Enter the maximum number:"))


except Exception as e:
    print("Invalid input")
else:
    if mn>=mx:
        print("This can not be the range as minimum should be less than maximum")
    else:
        for i in range(mn,mx+1):
            if n%i==0:
                print(f"{i} is a divisor of {n}")
            else:
                print(f"{i} is not a divisor of {n}")

