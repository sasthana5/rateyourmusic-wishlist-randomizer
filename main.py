import csv
import random
f = open("user_albums_export.csv", "r")
csvreader = csv.reader(f)
list = []
f = open("output.txt", "w")
f.close()
for row in csvreader:
    f = open("user_albums_export.csv", "r")
    if row[8] == "w":
        if row[1] == str(("")):
            fullName = str(row[2])
        else:
            fullName = str(row[1]) + " " + str(row[2])
    
        album = str(row[5])
        combined = fullName + " - " + album
#        print(combined)
        list.append(combined)
        f.close()
        f = open("output.txt", "a")
        f.write((combined) + "\n")
        f.close()
    else:
        pass

randSelect = random.randint(1, (len(list)))
print("You should listen to: " + list[randSelect - 1])