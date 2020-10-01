from tkinter import Tk     
from tkinter.filedialog import askopenfilename

Tk().withdraw()                                                           # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes = (('text files', 'txt'),))          # show an "Open" dialog box and allows only text file to be selected and return the path to the selected fill


file= open(filename,"r",encoding='utf-8') 
file_contents = file.read()

print(file_contents)

