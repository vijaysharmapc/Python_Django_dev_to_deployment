#Open a file, this will create a new file and keep it in w or write mode
myFile = open('myfile.txt', 'w')

print(myFile.name)
print(myFile.closed)
print(myFile.mode)

#write to the file
myFile.write('I love Python')
myFile.write('I love data too')
myFile.close()

# append
myFile = open('myfile.txt', 'a')
myFile.write('I also like bash & php')
myFile.close()

# read
myFile = open('myfile.txt', 'r') # r+ read and write
print(myFile.read(10))
myFile.close()
