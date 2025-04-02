#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

file = open("daily.txt", "r")
lines = file.readlines()
print(lines)

#change the words in the file to uppercase
lines_upper = []
for line in lines:
    lines_upper.append(line.upper())
print(lines_upper)

#write the new file with the modified lines
file = open("updateddaily.txt", "w")
file.writelines(lines_upper)
file.close()

#error handling
try:
    file = open("errorhandle.tt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")


