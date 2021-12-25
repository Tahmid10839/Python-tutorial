import time
def searcher():
    book = "This is Tahmid and here is your book"
    time.sleep(3)

    while True:
        text = (yield)
        if text in book:
            print("Found")
        else:
            print("Not Found")

search = searcher()
inp = input("Enter the word you want to search:")
print("Search started")
print("Searching....")
next(search)
time.sleep(4)
print("Search complete")
time.sleep(1)
search.send(inp)
time.sleep(1)
input("Press any key to search again")
inp = input("Enter the word you want to search:")
print("Search started")
print("Searching....")
time.sleep(4)
print("Search complete")
time.sleep(1)
search.send(inp)
print("Enough for today")

