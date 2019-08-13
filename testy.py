count =0
file = input("Enter file name :")
try:
    open_file = open(file)
except:
    if file == "na na boo boo":  # fragment z na na boo boo
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()

    print("problem with open file")
    exit()

for line in open_file:
    count = count + 1

print("There were", count, " subject lines in ", file)