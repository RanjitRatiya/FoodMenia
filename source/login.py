def login_form():
    from tkinter import Button, Entry, Frame, Label, Tk,StringVar,messagebox
    import sqlite3
    from homepage import homepage
    from mymenu import menu

    # root = Tk()
    # root.geometry("1000x800")
    login_frame = Frame(bg="cyan")
    login_frame.place(x=0,y=0,height="800",width="1200")
    g1 = StringVar()
    g2 = StringVar()
    back = Button(login_frame,text="<=",font=("Calibri",15),command=homepage).place(x=0,y=0)
    exit_btn = Button(login_frame,text="X",font=("Calibri",15),command=exit).place(y="0px",x="720px")
    name = Label(login_frame,text=("Email ID"),font=("Calibri",15),bg="cyan").place(x="345px",y="20px")
    name_field = Entry(login_frame,font=("Calibri",15),textvariable=g1).place(x="345px",y="50px")

    password = Label(login_frame,text=("Password"),font=("Calibri",15),bg="cyan").place(x="345px",y="80px")
    password = Entry(login_frame,font=("Calibri",15),show='*',textvariable=g2).place(x="345px",y="110px")

    def login1():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        r = cr.execute("select * from regis_table where UEMAIL='"+g1.get()+"' AND UCPWD='"+g2.get()+"'")
        for r1 in r:
            messagebox.showinfo('Title','Welcome...')
            menu()
            break
        else:
            messagebox.showerror('Title','Invalid Email Id or Password.')
        db.commit()
        db.close()
        g1.set("")
        g2.set("")

    def clear2():
        g1.set("")
        g2.set("")
    login = Button(login_frame,text=("Login"),font=("Calibri 15 bold"),command=login1).place(x="345px",y="150px")
    clear = Button(login_frame,text=("Clear"),font=("Calibri 15 bold"),command=clear2).place(x="435px",y="150px")
    login_frame.mainloop()
# login_form()