import tkinter

screen = tkinter.Tk()

screen.geometry("400x400")
#tkinter variable
email_var = tkinter.StringVar()
password_var = tkinter.StringVar()
msg_var = tkinter.StringVar()

#python function
def myfun():
    msg_var.set(email_var.get())

#label display
lbl = tkinter.Label(screen,text="Login Form",font=('Arial',26,'bold'))
lbl.pack()

#email display
e1_lbl = tkinter.Label(screen,text="Enter Email",font=('Arial',8,'bold'))
e1_lbl.place(x=50,y=55)
e1=tkinter.Entry(screen,textvariable=email_var)
e1.place(x=180,y=60)

#password display
e2_lbl = tkinter.Label(screen,text="Enter Password",font=('Arial',8,'bold'))
e2_lbl.place(x=50,y=95)
e2=tkinter.Entry(screen,textvariable=password_var)
e2.place(x=180,y=102)

#button dispaly
btn = tkinter.Button(screen,text="Sign In",font=('Arial',8,'bold'),command=myfun)
btn.place(x=180,y=130)

#final message display
lbl_msg = tkinter.Label(screen,text="Message",textvariable=msg_var)
lbl_msg.place(x=180,y=160)

screen.mainloop()
