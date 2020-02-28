from tkinter import *

root = Tk()
root.title("Grammar Checker")
root.geometry("800x400")

f1 = Frame(root, width=200, height=400)
f1.config(background= "#b7e9fd")
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=400)
f2.pack()

l0=Label(f2,text="")
l0.grid(row=0,columnspan=2)


b1 = Button(f2, text="Browse files", command=lambda: e.inputfile(root), width=40, height=1)
b1.grid(row=1, column=0, padx=2, pady=2, sticky=W, columnspan=2)
b1.config(relief="solid")

l20=Label(f2,text="Number of files selected: ")
l20.grid(row=2,column=0,padx=2,pady=2,sticky=W)

l21=Label(f2,text="")
l21.grid(row=2,column=1,padx=2,pady=2,sticky=W)

l30=Label(f2,text="File Selected:")
l30.grid(row=3,column=0,padx=2,pady=2,sticky=NW)

l31=Label(f2,text="")
l31.grid(row=3, column=1, padx=2, pady=2, sticky=W)


b41=Button(f2,text="Go!",command=None,width=40,height=1)
b41.grid(row=4, column=0, padx=2, pady=2, sticky=W, columnspan=2)
b41.config(relief="solid")

l50 = Label(f2, text="")
l50.grid(row=5, column=0, padx=2, pady=2, sticky=W)

root.mainloop()