path = "E:\\Drive\\Mega@Simulation365\\Data Analytics\\Labs\\Python Dev\\basics\\files\\file1.txt"
with open(path,"r") as file1:
    print(file1.name)
    print(file1.mode)
    for line in file1:
        file_stuff = file1.readline()
        print(file_stuff)
with open(path, "w") as file1:
    file1.write("File line 1 is written/n")
    file1.write("File line 1 is written/n")