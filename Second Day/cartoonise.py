import cv2
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def select_image():
    global panelA,panelB

    path= filedialog.askopenfilename()
    
    if len(path)>0:
        #image code with opencv
        #read
        image = cv2.imread(path)
        image = cv2.resize(image, (350, 350),  
               interpolation = cv2.INTER_NEAREST)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        # 2) Color
        color = cv2.bilateralFilter(image, 9, 300,300)

        # 3) Cartoon
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        

        #apply the nessecary filter

        #mask the target image

        #convert BGR2RGB
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        cartoon = cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)
        
        #convert the image to PIL format
        image = Image.fromarray(image)
        cartoon =Image.fromarray(cartoon)
        #covert to imagetk format
        
        image_disp = ImageTk.PhotoImage(image)
        cartoon_disp =ImageTk.PhotoImage(cartoon)

        if panelA is None or panelB is None:
            panelA = Label(image=image_disp)
            panelA.image =image_disp
            
            
            panelA.pack(side="left",padx=10,pady=10)

            panelB = Label(image=cartoon_disp)
            panelB.image =cartoon_disp

            
            panelB.pack(side="right",padx=10,pady=10)

        else:
            panelA.configure(image=image_disp)
            panelB.configure(image=cartoon_disp)
            panelA.image =image_disp
            panelB.image =cartoon_disp

root = Tk()
panelA= None
panelB = None

btn = Button(root,text="select an image", command = select_image)
btn.pack(side="bottom",fill = "both",expand="yes",padx="10",pady="10")

root.mainloop()