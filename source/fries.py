def fries():
    from tkinter import Frame, Label,Button,Tk,messagebox
    from PIL import ImageTk, Image
    import sqlite3
    from mymenu import menu
    # root= Tk()
    # root.geometry("1000x800")

    fries_frame = Frame(bg="cyan",padx=10)
    fries_frame.place(x=0,y=0,height="800",width="1000")

    def add_fries_regular():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Fries (Regular)','60')")
        messagebox.showinfo('Title',"Fries (Regular) Added to Cart")
        db.commit()
        db.close()
    
    def add_fries_king():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Fries (King)','75')")
        messagebox.showinfo('Title',"Fries (King) Added to Cart")
        db.commit()
        db.close()

    def add_cheese_fries():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Cheese Fries','85')")
        messagebox.showinfo('Title',"Cheese Fries Added to Cart")
        db.commit()
        db.close()
    
    def add_peri_regular():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Peri Peri (Regular)','65')")
        messagebox.showinfo('Title',"Peri Peri (Regular) Added to Cart")
        db.commit()
        db.close()
    
    def add_peri_king():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Peri Peri (King)','85')")
        messagebox.showinfo('Title',"Peri Peri (King) Added to Cart")
        db.commit()
        db.close()
    
    def add_italian_fries():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Italian Fries','85')")
        messagebox.showinfo('Title',"Itilian Fries Added to Cart")
        db.commit()
        db.close()

    back = Button(fries_frame,text="<=",font=("Calibri",15),command=menu).place(x=0,y=0) 

    my_image1 = ImageTk.PhotoImage(Image.open("Fries/fries_small.jpg"))
    my_lable1 = Label(image=my_image1).place(x="10px",y="40px")
    fries_small = Label(fries_frame,text="Fries (Regular)",font=("African",12),bg="cyan").place(x="15px",y="160px")
    fries_small_price = Label(fries_frame,text="\u20B9 60",font=("African",12),bg="cyan").place(x="40px",y="180px")
    fries_small_add = Button(text="Add",font=("African",15),command=add_fries_regular).place(x="40px",y="200px")

    my_image2 = ImageTk.PhotoImage(Image.open("Fries/fries_large.jpg"))
    my_lable2 = Label(image=my_image2).place(x="200px",y="40px")
    fries_king = Label(fries_frame,text="Fries (King)",font=("African",12),bg="cyan").place(x="220px",y="160px")
    fries_king_price = Label(fries_frame,text="\u20B9 75",font=("African",12),bg="cyan").place(x="230px",y="180px")
    fries_king_add = Button(text="Add",font=("African",15),command=add_fries_king).place(x="225px",y="200px")

    my_image3 = ImageTk.PhotoImage(Image.open("Fries/cheese_fries.jpg"))
    my_lable3 = Label(image=my_image3).place(x="400px",y="40px")
    cheese_fries = Label(fries_frame,text="Cheese Fries",font=("African",12),bg="cyan").place(x="415px",y="160px")
    cheese_fries_price = Label(fries_frame,text="\u20B9 85",font=("African",12),bg="cyan").place(x="440px",y="180px")
    cheese_fries_add = Button(text="Add",font=("African",15),command=add_cheese_fries).place(x="430px",y="200px")

    my_image4 = ImageTk.PhotoImage(Image.open("Fries/peri_peri_small.jpg"))
    my_lable4 = Label(image=my_image4).place(x="10px",y="250px")
    peri_peri_small = Label(fries_frame,text="Peri Peri (Regular)",font=("African",12),bg="cyan").place(x="10px",y="370px")
    peri_small_price = Label(fries_frame,text="\u20B9 65",font=("African",12),bg="cyan").place(x="40px",y="390px")
    peri_small_add = Button(text="Add",font=("African",15),command=add_peri_regular).place(x="40px",y="410px")

    my_image5 = ImageTk.PhotoImage(Image.open("Fries/peri_peri_king.jpg"))
    my_lable5 = Label(image=my_image5).place(x="200px",y="250px")
    peri_peri_king = Label(fries_frame,text="Peri Peri (King)",font=("African",12),bg="cyan").place(x="205px",y="370px")
    peri_king_price = Label(fries_frame,text="\u20B9 85",font=("African",12),bg="cyan").place(x="230px",y="390px")
    peri_king_add = Button(text="Add",font=("African",15),command=add_peri_king).place(x="230px",y="410px")

    my_image6 = ImageTk.PhotoImage(Image.open("Fries/itilian_fries.jpg"))
    my_lable6 = Label(image=my_image6).place(x="400px",y="250px")
    itilian_fries = Label(fries_frame,text="Itilian Fries",font=("African",12),bg="cyan").place(x="410px",y="370px")
    itilian_price = Label(fries_frame,text="\u20B9 85",font=("African",12),bg="cyan").place(x="430px",y="390px")
    itilian_add = Button(text="Add",font=("African",15),command=add_italian_fries).place(x="430px",y="410px")


    fries_frame.mainloop()
# fries()