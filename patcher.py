fil = input("Select a .PAT file: ")
file1 = open(fil, 'r')
Lines = file1.readlines()
 
count = 1
for line in Lines:
    if count == 1:
      dator = line
    if count == 2:
      linenum = line
    if count == 3:
      myfile = open(dator, 'a')
      myfile.writelines(line)[linenum]
      myfile.close()
      count = 1
    count += 1
