#THIS IS PROGRAM TO CREATE OR WRITE IN EXISTING FILE

'''
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
'''



#Writing in file
#########    NOTE "w" WILL RE-WRITE WHOLE FILE    ################

filename = open('write.txt',"w")
data_to_beEntered ="HELLO MOTO \n CHEERS FOR PEACE AND CODE"
filename.write(data_to_beEntered)                               #writing in file
filename.close()                                                # Remember to close file after writing

filename = open("write.txt",'r')
print(filename.read())                                          #Reading the file to check data is entered correctly




#Appending the data at last so that the file won't get re-written

filename = open("write.txt",'a')
data_to_beEntered = "YO MY BOIS ND LADIES"
filename.write(data_to_beEntered)                               #Appending the data at last
filename.close()

filename = open("write.txt",'r')
print(filename.read())


#Taking filename and its data from user

user_input = input('Enter file name: ')
filename = open(user_input,'w')
data_to_beEntered = input('enter the data:')
filename.write(data_to_beEntered)                               
filename.close()

filename = open(user_input,'r')
print(filename.read())


#Taking filename and its data from user to continue writing in existingfile

user_input = input('Enter file name: ')
filename = open(user_input,'a')
data_to_beEntered = input('enter the data:')
filename.write(data_to_beEntered)                               
filename.close()

filename = open(user_input,'r')
print(filename.read())


#Write a file and encoding it to utf-8

filename = open('write2.txt','w',encoding='utf-8')
filename.write('this is sample data')
filename.close()

filename = open('write2.txt','r',encoding='utf-8')
print(filename.read())


#Changing the encoding of existing file and creating its new copy

with open('read.txt', 'r') as fr:
        with open('encodingchangedfile.txt', 'w', encoding='utf-8') as fw:
            for line in fr:
                fw.write(line[:-1]+'\r\n')

