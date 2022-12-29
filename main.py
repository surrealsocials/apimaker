#main.py

#apimaker.make("api.py","C:\\Users\\surre\\venv\\main.py","C:\\Users\\surre\\venv")
#apimaker.addhere(__file__)

# Import Module
import os
from tkinter import *
from tkinter import filedialog as fd
import apimaker


# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "name")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)

def go():
	dirname=fd.askdirectory()
	filelist=[]
	filez = fd.askopenfilenames(title='Choose files')
	for file in filez:
		file=file.split('/')[len(file.split('/'))-1]
		filelist.append(file)

	apimaker.make(txt.get(),filelist,dirname)





# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			fg = "red", command=go)
# Set Button Grid
btn.grid(column=2, row=0)




# Execute Tkinter
root.mainloop()
