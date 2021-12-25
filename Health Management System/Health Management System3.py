
client_list = {1:"Harry",2:"Rohan",3:"Hammad"}
log_list = {1:"Exercise",2:"Food"}

def getdate():
    import datetime
    return datetime.datetime.now()

print("--------Health Management System------")

try:
    while(True):
        print("Select Client Name")
        for key, value in client_list.items():
            print("Press", key, "for", value)
        client_name = int(input())
        print("Selected Client:", client_list[client_name])
        print("Press 1 for Log")
        print("Press 2 for Retrieve")
        o = int(input())
        if o == 1:
            for key, value in log_list.items():
                print("Press", key, "to log", value)
            log_name = int(input())
            f = open(client_list[client_name] + "-" + log_list[log_name] + ".txt", "a")
            print("Selected job:", log_list[log_name])
            k = "y"
            while (k == "y"):
                print("Enter", log_list[log_name], ":")
                mytext = input()
                f.write("[" + str(getdate()) + "]:" + mytext+"\n")
                k=input("Add more?y/n :")
                continue
            f.close()
        elif o == 2:
            for key, value in log_list.items():
                print("Press", key, "to retrieve", value)
            op = int(input())
            print(client_list[client_name]+"-"+log_list[op]+" Report:")
            f = open(client_list[client_name] + "-" + log_list[op] + ".txt")
            contents = f.readlines()
            for line in contents:
                print(line,end="")
            f.close()
        else:
            print("Invalid input")
        ex= input("Do you want to continue?y/n:")
        if (ex=='y'):
            continue
        else:
            break


except Exception as e:
    print("Invalid Input")

print("Thank You for using Health Management System")