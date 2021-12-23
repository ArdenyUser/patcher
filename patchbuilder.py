filea = input("What is the original file?")
fileb = input("What is the patched file?")
x = 0
i = 0
while i != 23:

  file = open(filea)
  content = file.readlines()
  fdata = content[x]
  file.close
  
  file = open(fileb)
  content = file.readlines()
  fdatb = content[x]
  file.close
  
  if fdata != fdatb:
    file1 = open("myfile.txt", "a")  # append mode
    file1.write(filea)
    file1.write(x)
    file1.write(fdatb + "\n")
    file1.close()
    print(x)
    x = x + 1
