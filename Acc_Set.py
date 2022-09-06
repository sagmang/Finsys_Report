from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1366x768+0+0")

window.title("Welcome to LikeGeeks app")
acc_frame = Frame(window)
acc_frame.grid(row=0,column=0,sticky='nsew')

def acc_responsive_widgets(event):
    dwidth = event.width
    dheight = event.height
    dcanvas = event.widget

    r1 = 25
    x1 = dwidth/63
    x2 = dwidth/1.021
    y1 = dheight/14 
    y2 = dheight/0.32

    dcanvas.coords("aspoly1",x1 + r1,y1,
    x1 + r1,y1,
    x2 - r1,y1,
    x2 - r1,y1,     
    x2,y1,     
    #--------------------
    x2,y1 + r1,     
    x2,y1 + r1,     
    x2,y2 - r1,     
    x2,y2 - r1,     
    x2,y2,
    #--------------------
    x2 - r1,y2,     
    x2 - r1,y2,     
    x1 + r1,y2,
    x1 + r1,y2,
    x1,y2,
    #--------------------
    x1,y2 - r1,
    x1,y2 - r1,
    x1,y1 + r1,
    x1,y1 + r1,
    x1,y1,
    )

    dcanvas.coords("asbutton1",dwidth/3.1,dheight/5)
    dcanvas.coords("asbutton2",dwidth/1.485,dheight/5)

    dcanvas.coords("ashline",dwidth/21,dheight/3,dwidth/1.055,dheight/3)

    dcanvas.coords("aslabel1",dwidth/13,dheight/2.5)
    dcanvas.coords("aslabel2",dwidth/13.85,dheight/1.85)
    dcanvas.coords("aslabel3",dwidth/1.935,dheight/1.85)
    dcanvas.coords("aslabel4",dwidth/13.95,dheight/1.42)
    dcanvas.coords("aslabel5",dwidth/1.935,dheight/1.42)
    dcanvas.coords("aslabel6",dwidth/18,dheight/1.14)
    dcanvas.coords("aslabel7",dwidth/1.935,dheight/1.14)
    dcanvas.coords("aslabel8",dwidth/13.6,dheight/0.95)
    dcanvas.coords("aslabel9",dwidth/13,dheight/0.82)
    dcanvas.coords("aslabel10",dwidth/18,dheight/0.73)
    dcanvas.coords("aslabel11",dwidth/1.97,dheight/0.73)
    dcanvas.coords("aslabel12",dwidth/15,dheight/0.65)
    dcanvas.coords("aslabel13",dwidth/1.935,dheight/0.65)

    dcanvas.coords("asentry1",dwidth/13.8,dheight/1.665)
    dcanvas.coords("asentry2",dwidth/1.93,dheight/1.665)
    dcanvas.coords("asentry3",dwidth/13.8,dheight/1.3)
    dcanvas.coords("asentry4",dwidth/1.93,dheight/1.3)
    dcanvas.coords("asentry5",dwidth/13.8,dheight/1.06)
    dcanvas.coords("asentry6",dwidth/1.93,dheight/1.06)
    dcanvas.coords("asentry7",dwidth/13.8,dheight/0.9)
    dcanvas.coords("asentry8",dwidth/13.8,dheight/0.7)
    dcanvas.coords("asentry9",dwidth/1.93,dheight/0.7)
    dcanvas.coords("asentry10",dwidth/13.8,dheight/0.621)
    dcanvas.coords("asentry11",dwidth/1.93,dheight/0.621)


acc_canvas=Canvas(acc_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

acc_frame.grid_rowconfigure(0,weight=1)
acc_frame.grid_columnconfigure(0,weight=1)

vertibar=Scrollbar(acc_frame, orient=VERTICAL)
vertibar.grid(row=0,column=1,sticky='ns')
vertibar.config(command=acc_canvas.yview)

acc_canvas.bind("<Configure>", acc_responsive_widgets)
acc_canvas.config(yscrollcommand=vertibar.set)
acc_canvas.grid(row=0,column=0,sticky='nsew')


acc_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aspoly1"))

acc_btn1=Button(acc_canvas,text='ACCOUNTS AND SETTINGS', width=28,height=1,foreground="white",background="#1b3857",font='arial 20',activebackground='#24a0ed', activeforeground='white')
window_acc_btn1 = acc_canvas.create_window(0, 0, anchor="nw", window=acc_btn1,tags=('asbutton1'))

acc_btn2=Button(acc_canvas,text='▼', width=2,height=1,foreground="#24a0ed",background="#1b3857",font='arial 20',activebackground='#24a0ed', activeforeground='white')
window_acc_btn2 = acc_canvas.create_window(0, 0, anchor="nw", window=acc_btn2,tags=('asbutton2'))

acc_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ashline"))

label_1 = Label(acc_canvas,width=10,height=2,text="Personal Info", font=('arial 18'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel1'))

label_1 = Label(acc_canvas,width=10,height=2,text="First Name", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel2'))

acc_entry_1=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_1 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_1, tags=('asentry1'))

label_1 = Label(acc_canvas,width=10,height=2,text="Last Name", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel3'))

acc_entry_2=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_2 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_2, tags=('asentry2'))

label_1 = Label(acc_canvas,width=7,height=2,text="E-mail", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel4'))

acc_entry_3=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_3 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_3, tags=('asentry3'))

label_1 = Label(acc_canvas,width=10,height=2,text="Username", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel5'))

acc_entry_4=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_4 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_4, tags=('asentry4'))

label_1 = Label(acc_canvas,width=28,height=2,text="Enter your Current Password", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel6'))

acc_entry_5=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_5 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_5, tags=('asentry5'))

label_1 = Label(acc_canvas,width=18,height=2,text="Enter New Password", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel7'))

acc_entry_6=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_6 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_6, tags=('asentry6'))

label_1 = Label(acc_canvas,width=18,height=2,text="Re-type New Password", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel8'))

acc_entry_7=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_7 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_7, tags=('asentry7'))

label_1 = Label(acc_canvas,width=11,height=2,text="Company Info", font=('arial 18'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel9'))

label_1 = Label(acc_canvas,width=18,height=2,text="Company Name", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel10'))

acc_entry_8=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_8 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_8, tags=('asentry8'))

label_1 = Label(acc_canvas,width=18,height=2,text="Company Address", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel11'))

acc_entry_9=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_9 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_9, tags=('asentry9'))

label_1 = Label(acc_canvas,width=5,height=2,text="City", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel12'))

acc_entry_10=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_10 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_10, tags=('asentry10'))

label_1 = Label(acc_canvas,width=6,height=2,text="State", font=('arial 12'),background="#1b3857",fg="white") 
window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel13'))

acc_entry_11=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
window_acc_entry_11 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_11, tags=('asentry11'))

window.mainloop()