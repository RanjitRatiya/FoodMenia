def burger():
    from tkinter import Label,Frame,Button,Tk,IntVar,messagebox
    from PIL import ImageTk, Image
    from mymenu import menu
    import sqlite3
    # root = Tk()
    # root.geometry("1000x800")

    burger_frame = Frame(bg="cyan",padx=10,height=800,width=1000)
    burger_frame.place(x=0,y=0)


    def add_bison():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Bison Burger','98')")
        messagebox.showinfo('Title',"Bison Burger Added to Cart")
        db.commit()
        db.close()
    
    def add_falfel():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Falfel Burger','96')")
        messagebox.showinfo('Title',"Falfel Burger Added to Cart")
        db.commit()
        db.close()

    def add_mushroom():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Mushroom Burger','119')")
        messagebox.showinfo('Title',"Mushroom Burger Added to Cart")
        db.commit()
        db.close()
    
    def add_paneer():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Paneer Burger','129')")
        messagebox.showinfo('Title',"Paneer Burger Added to Cart")
        db.commit()
        db.close()
    
    def add_chilli():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Chilli Burger','89')")
        messagebox.showinfo('Title',"Chilli Burger Added to Cart")
        db.commit()
        db.close()
    
    def add_walnut():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Paneer Burger','139')")
        messagebox.showinfo('Title',"Walnut Burger Added to Cart")
        db.commit()
        db.close()

    back = Button(burger_frame,text="<=",font=("Calibri",15),command=menu).place(x=0,y=0) 
    
    my_image1 = ImageTk.PhotoImage(Image.open("Burgers/bison_burger.jpg"))
    my_lable1 = Label(image=my_image1).place(x="10px",y="40px")
    bison = Label(burger_frame,text="Bison Burger",font=("African",12),bg="cyan").place(x="15px",y="160px")
    bison_price = Label(text="\u20B9 98",font=("African",15),bg="cyan").place(x="30px",y="180px")
    bison_add = Button(text="Add",font=("African",15),command=add_bison).place(x="30px",y="210px")

    my_image2 = ImageTk.PhotoImage(Image.open("Burgers/falfel_burger.jpg"))
    my_lable2 = Label(image=my_image2).place(x="200px",y="40px")
    falfel = Label(burger_frame,text="Falfel Burger",font=("African",12),bg="cyan").place(x="200px",y="160px")
    falfel_price = Label(text="\u20B9 96",font=("African",15),bg="cyan").place(x="220px",y="180px")
    falfel_add = Button(text="Add",font=("African",15),command=add_falfel).place(x="220px",y="210px")

    my_image3 = ImageTk.PhotoImage(Image.open("Burgers/mushroom_burger.jpg"))
    my_lable3 = Label(image=my_image3).place(x="400px",y="40px")
    mushroom = Label(burger_frame,text="Mushroom Burger",font=("African",12),bg="cyan").place(x="395px",y="160px")
    mushroom_price = Label(text="\u20B9 119",font=("African",15),bg="cyan").place(x="430px",y="180px")
    mushroom_add = Button(text="Add",font=("African",15),command=add_mushroom).place(x="430px",y="210px")

    my_image4 = ImageTk.PhotoImage(Image.open("Burgers/paneer_king.jpg"))
    my_lable4 = Label(image=my_image4).place(x="10px",y="270px")
    paneer = Label(burger_frame,text="Paneer Burger",font=("African",12),bg="cyan").place(x="10px",y="390px")
    paneer_price = Label(text="\u20B9 129",font=("African",15),bg="cyan").place(x="30px",y="410px")
    paneer_add = Button(text="Add",font=("African",15),command=add_paneer).place(x="30px",y="440px")

    my_image5 = ImageTk.PhotoImage(Image.open("Burgers/veg_chili_cheese.jpg"))
    my_lable5 = Label(image=my_image5).place(x="200px",y="270px")
    veg_chilli = Label(burger_frame,text="Chilli Burger",font=("African",12),bg="cyan").place(x="210px",y="390px")
    veg_chilli_price = Label(text="\u20B9 89",font=("African",15),bg="cyan").place(x="230px",y="410px")
    veg_chilli_add = Button(text="Add",font=("African",15),command=add_chilli).place(x="230px",y="440px")

    my_image6 = ImageTk.PhotoImage(Image.open("Burgers/walnut-burgers.jpg"))
    my_lable6 = Label(image=my_image6).place(x="400px",y="270px")
    Walnut = Label(burger_frame,text="Walnut Burger",font=("African",12),bg="cyan").place(x="395px",y="390px")
    walnut_price = Label(text="\u20B9 139",font=("African",15),bg="cyan").place(x="430px",y="410px")
    walnut_add = Button(text="Add",font=("African",15),command=add_walnut).place(x="430px",y="440px")


    burger_frame.mainloop()

# burger()