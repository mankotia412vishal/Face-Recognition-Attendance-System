"""

from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
# win = Tk()

m_root = Tk()
m_root.wm_state('zoomed')

label_time = Label(m_root,file="pandu2.jpg", anchor="e", justify="right").grid()

m_root.mainloop()


"""


"""
from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 400, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("pandu4.jpg"))  
canvas.create_image(10, 10, anchor=NW, image=img) 
root.mainloop() 

"""

from tkinter import *  
from PIL import ImageTk,Image  
oot =tk.Tk() 	
# root = tk.Tk() 
canvas = tk.Canvas(root, width = 500, height = 500) 
canvas.pack()
 
img = ImageTk.PhotoImage(Image.open("pandu4.jpg")) 
canvas.create_image(5,5, anchor='nw', image=img) 
root.mainloop()