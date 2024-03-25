from main import agent
from customtkinter import *
from PIL import Image
import tkinter

app = CTk()
app.title("Ai Assistant")
app.geometry("600x480")
app.resizable(0,0)

frame = CTkFrame(master=app, width=600, height=480, fg_color="#778DA9",bg_color="#778DA9")
frame.pack_propagate(0)
frame.pack(expand=True)

chat_image_data= Image.open("robot.png")
chat_image=CTkImage(dark_image=chat_image_data, light_image=chat_image_data,size=(50,50))


def query_and_display():
    text1 = entry1.get()
    if text1.lower() == "q":
        app.quit()  
    else:
        result = agent.query(text1)
        image.place(relx=0.1, rely=0.1,anchor=tkinter.E)
        window.delete("1.0", "end")
        window.place(relx=0.62, rely=0.1,anchor=tkinter.E)
        window.insert(tkinter.END, f"Q: {text1} ? ")
        window2.delete("1.0", "end")
        window2.place(relx=0.62, rely=0.38,anchor=tkinter.E)
        window2.insert(tkinter.END, f" {result}")
        


entry1=CTkEntry(master=frame, 
         width=480, 
         fg_color="#EEEEEE", 
         border_color="#808080", 
         border_width=1, 
         text_color="#000000",
         placeholder_text="Enter a request")
entry1.pack(side="left", padx=(25, 10), pady=(420, 10))

window_buttom=CTkButton(master=frame, 
          width=80, 
          fg_color="#32CD32", 
          border_color="#601E88", 
          border_width=1, 
          text_color="#000000",
          text="Submit",
          command=query_and_display)
window_buttom.pack(side="right", padx=(5, 10), pady=(420, 10))


image=CTkLabel(master=frame, 
        text="",
        anchor="w", 
        justify="left", 
        image=chat_image, 
        compound="center"
        )

window=CTkTextbox(master=frame,
          height=50,
          width=300,                           
          fg_color="#32CD32",                   
        )

window2=CTkTextbox(master=frame,
        height=200,
        width=300,              
        fg_color="#FFF",
        activate_scrollbars=False                   
        )

app.mainloop()