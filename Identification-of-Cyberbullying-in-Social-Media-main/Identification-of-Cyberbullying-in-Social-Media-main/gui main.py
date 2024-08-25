
from tkinter import *
import tkinter as tk
from PIL import Image ,ImageTk
from tkinter.ttk import *
from pymsgbox import *


root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("HOME")
# bg = Image.open(r"y11.jpg")
# bg.resize((w,h),Image.ANTIALIAS)
# print(w,h# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# #bg_lbl.bg_img
# bg_lbl.place(x=0,y=93)
# #, relwidth=1, relheight=1)
# label_l1 = tk.Label(root, text="CYBER BULLYING USING TWITTER",font=("Times New Roman", 35, 'bold'),
#                     background="black", fg="white", width=60, height=1)
# label_l1.place(x=0, y=0)



img=ImageTk.PhotoImage(Image.open("img1.png"))

img2=ImageTk.PhotoImage(Image.open("c3.jpg"))

img3=ImageTk.PhotoImage(Image.open("c1.jpg"))


logo_label=tk.Label()
logo_label.place(x=190,y=120)



# using recursion to slide to next image

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img,width=1200,height=500)
	elif x == 2:
		logo_label.config(image=img2,width=1200,height=500)
	elif x == 3:
		logo_label.config(image=img3,width=1200,height=500)
	x = x+1
	root.after(2000, move)

# calling the function
move()
#

#marquee
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=Canvas(root,bg="black")
canvas.pack()
text_var="CYBER BULLYING USING TWITTER"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 100
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling


'''
def marquee_fun(widget, widget_w, widget_h, total_w, total_h, direction, speed, position=0):
    if direction=='right':
        if position>=total_w-widget_w:
            position=0
        position = position + speed
        widget.place(x=position)
        
    widget.after(10, lambda: marquee_fun(widget, widget_w, widget_h, total_w, total_h, direction, speed))

w = tk.Label(root, text="Crop Prediction Using Machine Learning",background="#17202A",foreground="white",font=("Times new roman",19,"bold"))
w.place(x=0,y=15, width=150, height=30)


w.after(100, lambda:marquee_fun(w, 150, 30, 500, 500, 'right', 2))

'''


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","register.py"])

def window():
    root.destroy()



button1 = tk.Button(root, text="Login", command=Login, width=12, height=2,bd=5,font=('times', 20, ' bold '), bg="gray", fg="white")
button1.place(x=400, y=650)

button2 = tk.Button(root, text="Register",command=Register,width=12, height=2,bd=5,font=('times', 20, ' bold '), bg="gray", fg="white")
button2.place(x=700, y=650)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=2,bd=5,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=1000, y=650)



root.mainloop()
