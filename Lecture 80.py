import sys

randomList = [10,'6','a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next ecntry.")
        print()
print("The reciprocal of", entry, "is", r)