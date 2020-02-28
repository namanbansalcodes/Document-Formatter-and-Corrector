from tkinter import *
from tkinter import filedialog
import os
import docx

class Engine():
    add = []  #stores selected file addresses
    filename = []  #stores selected file names
    doc = None  #doc object to work on current word file
    docf=None   #Final doc object
    n = 0  #number of lines in the doc file
    N = 0  #total number of files selected

    def __init__(self):
        pass

    def inputfile(self, root):
        del self.add[::], self.filename[::]
        
        s = filedialog.askopenfilenames()

        #seperating filename from the entire addresses
        for i in s:
            i = i[::-1]
            temp = 0
            
            for j in range(len(i)):
                if i[j] == "/":
                    temp = j
                    break
            
            temp = len(i) - temp
            i = i[::-1]
            
            self.add.append(i[:temp])
            self.filename.append(i[temp:])
        
        self.N=len(self.add)

        l21.config(text=str(self.N))

        temp=""
        for i in self.filename:
            temp=temp+ i + "\n"
        temp=temp[:-1]

        l31.config(text=temp)

    
    def enginecontrol(self):
        for i in range(self.N):
            self.loaddoc(i)
            #symspellpy correction
            #punctuation correction
            #language-check correction

    
    def loaddoc(self, i):
        os.chdir(self.add[i])  #changes the working directory
        
        self.doc = docx.Document(self.filename[i])
        self.doc.save("temp.docx")  #creating a copy of document so that original doc is not lost

        self.doc = docx.Document(self.filename[i])
        self.n = len(self.doc.paragraphs)
        
        self.docf=docx.Document()   #initializing result document 

e=Engine()
root = Tk()
root.title("Document Formatter and Corrector")
root.geometry("800x400")

f1 = Frame(root, width=200, height=400)
f1.config(background= "#b7e9fd")
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=400)
f2.pack()

l0=Label(f2,text="")
l0.grid(row=0,columnspan=2)


b1 = Button(f2, text="Browse files",command= lambda:e.inputfile(root), width=40, height=1)
b1.grid(row=1, column=0, padx=2, pady=2, sticky=W, columnspan=2)
b1.config(relief="solid")

l20=Label(f2,text="Number of files selected: ")
l20.grid(row=2,column=0,padx=2,pady=2,sticky=W)

l21=Label(f2,text="")
l21.grid(row=2,column=1,padx=2,pady=2,sticky=W,columnspan=2)

l30=Label(f2,text="File Selected:")
l30.grid(row=3,column=0,padx=2,pady=2,sticky=NW)

l31=Label(f2,text="")
l31.grid(row=3, column=1, padx=2, pady=2, sticky=W)

b41=Button(f2,text="Go!",command=lambda:e.enginecontrol(),width=40,height=1)
b41.grid(row=4, column=0, padx=2, pady=2, sticky=W, columnspan=2)
b41.config(relief="solid")

l50 = Label(f2, text="")
l50.grid(row=5, column=0, padx=2, pady=2, sticky=W)


root.mainloop()
