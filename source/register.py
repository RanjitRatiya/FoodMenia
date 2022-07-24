
def register_form():
    import sqlite3
    from tkinter import Button, Checkbutton, Entry, Frame, Label, Radiobutton, Tk, font,StringVar,messagebox,IntVar
    from homepage import homepage
    from login import login_form
    # root = Tk()
    # root.geometry("1000x800")
    register_frame = Frame(bg="cyan")
    register_frame.place(x=0,y=0,height="800",width="1000")
    r1 = StringVar()
    r2 = StringVar()
    r3 = StringVar()
    r4 = StringVar()
    r5 = StringVar()
    r6 = StringVar()
    gender= IntVar()
    check = IntVar()
    
    
    back = Button(register_frame,text="<=",font=("Calibri",15),command=homepage).place(x=0,y=0)
    exit_btn = Button(register_frame,text="X",font=("Calibri",15),command=exit).place(y="0px",x="720px")

    name = Label(register_frame,text=("Full Name"),font=("Calibri",15),bg="cyan").place(x="345px")
    name_field = Entry(register_frame,font=("Calibri",15),textvariable=r1).place(x="345px",y="30px")

    address = Label(register_frame,text=("Address"),font=("Calibri",15),bg="cyan").place(x="345px",y="60px")
    address_field = Entry(register_frame,font=("Calibri",15),textvariable=r2).place(x="345px",y="90px")

    mobile_no = Label(register_frame,text=("Mobile No."),font=("Calibri",15),bg="cyan").place(x="345px",y="120px")
    mobile_no_field = Entry(register_frame,font=("Calibri",15),textvariable=r3).place(x="345px",y="150px")

    gender = Label(register_frame,text=("Gender"),font=("Calibri",15),bg="cyan").place(x="345px",y="180px")
    male = Radiobutton(register_frame,text=("Male"),font=("Calibri",15),bg="cyan",value=1,variable=gender).place(x="345px",y="210px")
    female = Radiobutton(register_frame,text=("Female"),font=("Calibri",15),bg="cyan",value=2,variable=gender).place(x="420px",y="210px")

    email = Label(register_frame,text=("Email"),font=("Calibri",15),bg="cyan").place(x="345px",y="250px")
    email_field = Entry(register_frame,font=("Calibri",15),textvariable=r4).place(x="345px",y="280px")

    password = Label(register_frame,text=("Password"),font=("Calibri",15),bg="cyan").place(x="345px",y="310px")
    password_field = Entry(register_frame,font=("Calibri",15),show='*',textvariable=r5).place(x="345px",y="340px")

    confirm_password = Label(register_frame,text=("Confirm Password"),font=("Calibri",15),bg="cyan").place(x="345px",y="370px")
    confirm_password_field = Entry(register_frame,font=("Calibri",15),show='*',textvariable=r6).place(x="345px",y="400px")

    t_c = Checkbutton(register_frame,text=("Agree Terms & Conditions"),font=("Calibri",15),bg="cyan",variable=check).place(x="345px",y="430px")

    def regis1():
        # db = sqlite3.connect('Burger.db')
        # cr = db.cursor()
        # use = cr.execute("insert into regis_table values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"','"+r4.get()+"','"+r5.get()+"','"+r6.get()+"')")
        # for i in use:
        # break
        if (r1.get()==""):
            messagebox.showerror('Error',"Fill all Fields")
            clear1()
        elif (r2.get()==""):
            messagebox.showerror('Error',"Fill all Fields")
            clear1()
        elif (r3.get()==""):
            messagebox.showerror('Error',"Fill all Fields")
            clear1()
        elif (r4.get()==""):
            messagebox.showerror('Error',"Fill all Fields")
            clear1()
        elif (r5.get()==""):
            messagebox.showerror('Error',"Fill all Fields")
            clear1()
        elif (r6.get()==""):
            messagebox.showerror('Error',"Fill all Fields")
            clear1()
        else:
            db = sqlite3.connect('Burger.db')
            cr = db.cursor()
            cr.execute("insert into regis_table values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"','"+r4.get()+"','"+r5.get()+"','"+r6.get()+"')")
            messagebox.showinfo("Welcome","User Registered...")
            db.commit()
            db.close()
            r1.set("")
            r2.set("")
            r3.set("")
            r4.set("")
            r5.set("")
            r6.set("")
            login_form()
    
    def clear1():
        r1.set("")
        r2.set("")
        r3.set("")
        r4.set("")
        r5.set("")
        r6.set("")


    register = Button(register_frame,text=("Register"),font=("Calibri 15 bold"),command=regis1,activebackground='lightblue').place(x="354px",y="470px")
    clear = Button(register_frame,text=("Clear"),font=("Calibri 15 bold"),command=clear1).place(x="450px",y="470px")

    register_frame.mainloop()
    
# register_form()