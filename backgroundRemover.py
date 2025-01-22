from rembg import remove
from PIL import Image as img

import time
from tkinter import *
import tkinter as tk




root = Tk()
root.title("Background Remover")
root.geometry("550x300+300+200")
root.resizable(False, False)



xColor = 255
yColor = 255
zColor = 255

def white():
    progress_label.config(text = "White", bg="#ffffff", fg = "black")
    progress_label.place(x= 210, y =230)
    root.focus_set()
def black():
    global xColor
    global yColor
    global zColor
    xColor = 0
    yColor = 0
    zColor = 0
    progress_label.config(text = "Black", bg="#000000", fg="white")
    progress_label.place(x= 210, y =230)
    root.focus_set()
def red():
    global xColor
    global yColor
    global zColor
    xColor = 255
    yColor = 0
    zColor = 0
    progress_label.config(text = "Red", bg="#ff0000", fg="white")
    progress_label.place(x= 210, y =230)
    root.focus_set()
def aquamarine():
    global xColor
    global yColor
    global zColor
    xColor = 127
    yColor = 255
    zColor = 212
    progress_label.config(text = "Aquamarine", bg="#7FFFD4", fg="black")
    progress_label.place(x= 210, y =230)
    root.focus_set()
    



def remove_background():
    
    progress_label.config(text = "Removing Background...")
    progress_label.place(x= 18, y =230)
    while True:
        
        try:
            input_path = search_field.get()
            output_path = "bg_remove_"+search_field.get()
            white_output_path = "bg_white_"+search_field.get()

            

            input = img.open(input_path)
            output = remove(input)
            output.save("img/"+output_path)

            #creating white background
            white_background = img.new('RGB', output.size, (xColor, yColor, zColor))
            white_background.paste(output, mask=output)
            white_background.save("img/"+white_output_path)

            progress_label.config(text = "Background Removed Successfully...")
            progress_label.place(x= 18, y =230)
            
            break
        except FileNotFoundError as e:
            
            progress_label.config(text = "The File you provided does not exist")
            break
        except Exception as e:
            progress_label.config(text = "Image Path Cannot Be Empty")
            break


def clear_placeholder(event):
    if search_field.get() == "Enter Image Path":
        search_field.delete(0, tk.END)
        search_field.config(fg="black")

def restore_placeholder(event):
    if search_field.get() == "":
        search_field.insert(0, "Enter Image Path")
        search_field.config(fg="gray")




baseColor = "#ffffff"
root.configure(bg = baseColor) 

#search box 
search_image = PhotoImage(file = "search.png")
image_search = Label(image = search_image, bg = baseColor)
image_search.place(x = 20, y = 20)

#input field
search_field = tk.Entry(root, takefocus=False,justify="center", width= 17, font = ("poppins", 25, "bold"), bg= baseColor)
search_field.insert(0, "Enter Image Path")
search_field.config(fg="gray")
search_field.bind("<FocusIn>", clear_placeholder)
search_field.bind("<FocusOut>", restore_placeholder)
search_field.place(x = 50, y = 40)



#remove button
remove_icon = PhotoImage(file = "icon_remove.png")
remove_icon = remove_icon.subsample(10,10)
remove_button = Button(root, image = remove_icon, borderwidth = 0, cursor="hand2", command=remove_background)
remove_button.focus_set()
remove_button.place(x = 400, y = 39)


#Custom background color
custom_background = Label(text="Choose Custom\nBackground: ", font=("arial", 20, "bold"),bg="#1fa9e5", fg = "white")
custom_background.place(x=40, y = 100)

#Button colors
defaultColorBtn = Button(root, text="   ", font=("arial", 10, "bold"), bg="#ffffff", fg="white", cursor="hand2", command=white)
defaultColorBtn.place(x = 265, y = 140)

blackColor = Button(root, text="   ", font=("arial", 10, "bold"), bg="#000000", fg="white", cursor="hand2",command=black)
blackColor.place(x = 290, y = 140)

redColor = Button(root, text="   ", font=("arial", 10, "bold"), bg = "#ff0000", fg = "white", cursor="hand2",command=red)
redColor.place(x = 315, y = 140)

aquamarineClr = Button(root, text="   ", font=("arial", 10, "bold"), bg = "#7FFFD4", fg = "white", cursor="hand2", command=aquamarine)
aquamarineClr.place(x = 340, y = 140)

notif = PhotoImage(file = "box.png")
msg_notif = Label(image = notif, bg = baseColor)
msg_notif.pack(padx = 5, pady = 5, side = BOTTOM)

#display progress
progress_label = Label(text="...", font=("arial", 20, "bold"),bg="#1fa9e5", fg = "white")
progress_label.place(x=225, y = 230)




root.mainloop()
