from rembg import remove
from PIL import Image as img

import time
from tkinter import *
import tkinter as tk




root = Tk()
root.title("Background Remover")
root.geometry("550x300+300+200")
root.resizable(False, False)


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
            white_background = img.new('RGB', output.size, (255, 255, 255))
            white_background.paste(output, mask=output)
            white_background.save("img/"+white_output_path)

            progress_label.config(text = "Background Removed Successfully...")
            progress_label.place(x= 18, y =230)
            
            break
        except FileNotFoundError as e:
            
            progress_label.config(text = "The File you provided does not exist")
            break
        except Exception as e:
            print(f"Error: {e}")





baseColor = "#ffffff"
root.configure(bg = baseColor) 

#search box 
search_image = PhotoImage(file = "search.png")
image_search = Label(image = search_image, bg = baseColor)
image_search.place(x = 20, y = 20)

#input field
search_field = tk.Entry(root, justify="center", width= 17, font = ("poppins", 25, "bold"), bg= baseColor)
search_field.place(x = 50, y = 40)
search_field.focus()
#remove button
remove_icon = PhotoImage(file = "icon_remove.png")
remove_icon = remove_icon.subsample(10,10)
remove_button = Button(root, image = remove_icon, borderwidth = 0, cursor="hand2", command=remove_background)


remove_button.place(x = 400, y = 39)


notif = PhotoImage(file = "box.png")
msg_notif = Label(image = notif, bg = baseColor)
msg_notif.pack(padx = 5, pady = 5, side = BOTTOM)

progress_label = Label(text="...", font=("arial", 20, "bold"),bg="#1fa9e5", fg = "white")
progress_label.place(x=225, y = 230)



root.mainloop()
