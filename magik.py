from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("Image thiny")
root.geometry("500x500")
root.configure(background="lightblue")

imagg = Label(root, bg="lightblue",highlightthickness=1)

imagg.place(relx=0.5,rely=0.21,anchor=CENTER)

img_path = ""

def openimg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes=(("Image files","*.png"),))
    print(img_path)
    img = ImageTk.PhotoImage(Image.open(img_path))
    imagg["image"] = img
    img.close()

def rotateimage():
    global img_path
    im = Image.open(img_path)
    new_img = im.rotate(180)
    img = ImageTk.PhotoImage(new_img)
    imagg["image"] = img
    img.close()
    

btn=Button(root, text="open image", command=openimg, bg="azure")
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
btn2=Button(root,text="rotate image", command=rotateimage, bg="azure")
btn2.place(relx=0.5, rely=0.8, anchor=CENTER)
nocopyrighting = Label(root, text="This is created by Leo Yan, no copyrighting okay dude?")
nocopyrighting.place(relx=0.5,rely=0.95,anchor=CENTER)
root.mainloop()