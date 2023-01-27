f1 = open("text.txt", "r")
f2 = open("TEXT2.txt", "r")
lines1 = f1.readlines()
lines2 = f2.readlines()
for i in range(len(lines1)):
    print(lines1[i].strip('\n') + lines2[i].strip('\n'))
f1.close()
f2.close()