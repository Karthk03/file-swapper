input1 = input("enter the first file: ")
input2 = input("enter the second file: ")

file1 = open(input1, 'r')
file2 = open(input2, 'r')

file1Txt = file1.read()
file2Txt = file2.read()

file1 = open(input1, 'w')
file2 = open(input2, 'w')

file1.write(file2Txt)
file2.write(file1Txt)