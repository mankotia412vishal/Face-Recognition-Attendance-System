try:
    import Tkinter as tkinter
except:
    import tkinter
from PIL import Image, ImageTk

def updateRoot(imagen):
    # resize the image to fill the whole screen
    pilImage = Image.open(imagen)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    image = ImageTk.PhotoImage(pilImage.resize((w,h)))
    # update the image
    canvas.itemconfig(imgbox, image=image)
    # need to keep a reference of the image, otherwise it will be garbage collected
    canvas.image = image

root = tkinter.Tk()
# root.attributes('-fullscreen', 1)
root.bind('<Escape>', lambda _: root.destroy())

canvas = tkinter.Canvas(root, highlightthickness=0)
canvas.pack(fill=tkinter.BOTH, expand=1)
imgbox = canvas.create_image(0, 0, image=None, anchor='nw')

# show the first image
updateRoot('pandu.webp')
# change the image 5 seconds later
root.after(5000, updateRoot, 'pandu.webp')

root.mainloop()