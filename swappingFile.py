f1 = input("enter file1 name ")
f2 = input("enter file2 name ")
def swapFileData(file1, file2):
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as c:
        c.write(data_b)
    with open(file2, 'w') as d:
        d.write(data_a)

swapFileData(f1,f2)