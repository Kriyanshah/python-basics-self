f = open("file.txt")
print(f.read())
f.close()

# this code aslo be written as :
with open("file.txt") as f:
    print(f.read())
# you dont need to close the file 