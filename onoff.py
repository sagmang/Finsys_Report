from tkinter import *
  

ws = Tk()
  
ws.title('Python Guides')
  
ws.geometry("400x300")
  
#global is_on
is_on = True
  
def Switch():
    global is_on
      
    if is_on:
        button.config(image = off)
        is_on = False
    else:
        
        button.config(image = on)
        is_on = True
  
on = PhotoImage(file = "images/on.png")
off = PhotoImage(file = "images/off.png")
  
button = Button(ws, image = on, bd = 0,
                   command = Switch)
button.pack(pady = 50)
  
ws.mainloop()