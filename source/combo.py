def combo():
    from tkinter import Label,Frame,Button,Tk,messagebox
    from PIL import ImageTk, Image
    import sqlite3
    from mymenu import menu
    # root = Tk()
    # root.geometry("1000x800")

    combo_frame = Frame(bg="cyan")
    combo_frame.place(x=0,y=0,height="800",width="1000")

    def add_paneer_overloaded():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Paneer Overloaded','139')")
        messagebox.showinfo('Title',"Paneer Overloaded Added to Cart")
        db.commit()
        db.close()
    
    def add_regular():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Regular Combo','239')")
        messagebox.showinfo('Title',"Regular Combo Added to Cart")
        db.commit()
        db.close()

    def add_maharaja():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Maharaja Combo','499')")
        messagebox.showinfo('Title',"Maharaja Combo Added to Cart")
        db.commit()
        db.close()
    

    back = Button(combo_frame,text="<=",font=("Calibri",15),command=menu).place(x=0,y=0) 

    my_image1 = ImageTk.PhotoImage(Image.open("combo/paneer_overloaded_burger.jpg"))
    my_lable1 = Label(image=my_image1).place(x="10px",y="40px")
    paneer_overloaded = Label(combo_frame,text="Paneer Overloaded",font=("African",12),bg="cyan").place(x="40px",y="165px")
    paneer_overloaded_price = Label(combo_frame,text="\u20B9 139",font=("African",12),bg="cyan").place(x="75px",y="180px")
    paneer_overloaded_add = Button(text="Add",font=("African",15),command=add_paneer_overloaded).place(x="75px",y="200px")

    my_image2 = ImageTk.PhotoImage(Image.open("combo/combo1.jpg"))
    my_lable2 = Label(image=my_image2).place(x="400px",y="40px")
    combo_regular = Label(combo_frame,text="Regular Combo",font=("African",12),bg="cyan").place(x="450px",y="160px")
    combo_regular_price = Label(combo_frame,text="\u20B9 239",font=("African",12),bg="cyan").place(x="470px",y="180px")
    combo_regular_add = Button(text="Add",font=("African",15),command=add_regular).place(x="470px",y="200px")

    my_image3 = ImageTk.PhotoImage(Image.open("combo/Maharaja_combo.jpg"))
    my_lable3 = Label(image=my_image3).place(x="210px",y="270px")
    maharaja_combo = Label(combo_frame,text="Maharaja Combo",font=("African",12),bg="cyan").place(x="270px",y="420px")
    maharaja_combo_price = Label(combo_frame,text="\u20B9 499",font=("African",12),bg="cyan").place(x="315px",y="440px")
    maharaja_add = Button(text="Add",font=("African",15),command=add_maharaja).place(x="315px",y="460px")

    combo_frame.mainloop()
# combo()