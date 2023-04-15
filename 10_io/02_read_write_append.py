# Preferred way to open a file object and
# not to worry about closing the file object

# mode "r" (read) is by default
# for read and write use "r+"

# when we write() to file, the cursor resets and,
# it overrides the existing content if present

# to avoid override, use "a" (append) mode
with open("test.txt", mode="r+") as my_file:
    text = my_file.write(":D")
    print(text)

# "r+" mode gave an error while writing to a file
# because we are reading first and then writing
# only writing to file in "r+" mode works fine

# "r" mode will not work in case the file doesn't exist
# "w" mode will create a file if the file doesn't exist

with open("happy.txt", mode="w") as my_file1:
    text = my_file1.write(":)")





