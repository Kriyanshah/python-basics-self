f = open("file.txt", "r") # Open the file in read mode
"""lines = f.readlines() # Read the data of the file line by line
print(lines, type(lines)) # Print the data and its type"""

                       # OR

"""line1 = f.readline() # Read the data of the file line by line
print(line1, type(line1)) # Print the data and its type
line2 = f.readline() # Read the data of the file line by line
print(line2, type(line2)) # Print the data and its type
line3 = f.readline() # Read the data of the file line by line
print(line3, type(line3)) # Print the data and its type
line4 = f.readline() # Read the data of the file line by line
print(line4, type(line4)) # Print the data and its type
line5 = f.readline() # Read the data of the file line by line
print(line5, type(line5)) # Print the data and its type"""

                       # OR

line = f.readline() # Read the data of the file line by line
while(line != ""):
    print(line, end="") # Print the data and its type
    line = f.readline() # Read the data of the file line by line



f.close() # Close the file