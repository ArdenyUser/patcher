fil = input("Select a .PAT file: ")
file1 = open(fil, 'r')
Lines = file1.readlines()

countedarchive = 0
counted = 0
count = 1
for line in Lines:
    if count == 1:
      if counted > countedarchive:
        dator = line
    if count == 2:
      if counted > countedarchive:
        linenum = line
    if count == 3:
      if counted > countedarchive:
        writedata = line
        countedarchive = counted
        break
    count += 1
    counted += 1

file1.close()
myfile = open(dator, 'a')
myfile.writelines(writedata)[linenum]
myfile.close()
