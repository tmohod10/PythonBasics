# open function returns an object with a cursor
# once we have completed reading the file
# reading again will not output anything as our first
# time cursor has already read the file and is pointing
# to the End Of the File (EOF)

my_file = open("test.txt")

# print(my_file.read())
# seek(index) will move the cursor to given index
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# cursor reads one line at a time
# and then starts with next line
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# This is read and add all the lines in a list
print(my_file.readlines())
