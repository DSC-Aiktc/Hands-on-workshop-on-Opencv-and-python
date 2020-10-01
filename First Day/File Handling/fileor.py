# Opening of file and reading it
'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

        "r" - Read - Default value. Opens a file for reading, error if the file does not exist
        "a" - Append - Opens a file for appending, creates the file if it does not exist
        "w" - Write - Opens a file for writing, creates the file if it does not exist
        "x" - Create - Creates the specified file, returns an error if the file exists

'''
#opening the file and reading it
filename = open('read.txt',"r")
for i in filename:
    print(i)


#reading the data using read() method

filename = open('read.txt',"r")
filedata = filename.read()
print(filedata)

#reading only few line of file opened

filname =  open('read.txt',"r")
few_fileData = filname.read(10)     #THIS WILL READ ONLY FIRST 10 LINES
print(few_fileData)
#Reading only one line using readline() method

filename= open('read.txt',"r")
one_line_data = filename.readline()
print(one_line_data)                # THIS WILL ONLY PRINT THE FIRST LINE
other_line_data = filename.readline()
print(other_line_data)              #THIS WILL ONLY PRINT THE SECOND LINE DATA

#Reading a file by user input

filename = open(input("ENTER THE FILE NAME: "),"r")
data = filename.read()
print(data)

#Reading  a UTF-8 file
'''
The encoding that this file uses. When Unicode strings are written to a file, 
they will be converted to byte strings using this encoding.
'''

filename =open('63247-0.txt',"r",encoding='utf-8')
encoded_fileData = filename.read()
print(encoded_fileData)



