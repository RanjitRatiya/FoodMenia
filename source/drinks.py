def drinks():
    from tkinter import Label,Frame,Button,Tk,messagebox
    import sqlite3
    from PIL import ImageTk, Image
    from mymenu import menu
    # root = Tk()
    # root.geometry("1000x800")

    drinks_frame = Frame(bg="cyan")
    drinks_frame.place(x=0,y=0,height=800,width=1000)

    def add_pepsi_can():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Pepsi Can','40')")
        messagebox.showinfo('Title',"Pepsi Can Added to Cart")
        db.commit()
        db.close()
    
    def add_pepsi_medium():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Pepsi (Medium)','75')")
        messagebox.showinfo('Title',"Pepsi (Medium) Added to Cart")
        db.commit()
        db.close()

    def add_chocolate():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Chocolate Shake','85')")
        messagebox.showinfo('Title',"Chocolate Shake Added to Cart")
        db.commit()
        db.close()
    
    def add_ice_tea():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Ice Tea','65')")
        messagebox.showinfo('Title',"Ice Tea Added to Cart")
        db.commit()
        db.close()
    
    def add_coffee():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Coffee','55')")
        messagebox.showinfo('Title',"Coffee Added to Cart")
        db.commit()
        db.close()
    
    def add_pepsi_king():
        db = sqlite3.connect('Burger.db')
        cr = db.cursor()
        cr.execute("insert into cart values('Pepsi (King)','75')")
        messagebox.showinfo('Title',"Pepsi (King) Added to Cart")
        db.commit()
        db.close()

    back = Button(drinks_frame,text="<=",font=("Calibri",15),command=menu).place(x=0,y=0) 

    my_image1 = ImageTk.PhotoImage(Image.open("Drinks/pepsi_can.jpg"))
    my_lable1 = Label(image=my_image1).place(x="10px",y="40px")
    pepsi_can = Label(drinks_frame,text="Pepsi Can",font=("African",12),bg="cyan").place(x="30px",y="160px")
    pepsi_can_price = Label(drinks_frame,text="\u20B9 40",font=("African",12),bg="cyan").place(x="40px",y="180px")
    pepsi_can_add = Button(text="Add",font=("African",15),command=add_pepsi_can).place(x="40px",y="200px")

    my_image2 = ImageTk.PhotoImage(Image.open("Drinks/pepsi_medium.jpg"))
    my_lable2 = Label(image=my_image2).place(x="200px",y="40px")
    pepsi_medium = Label(drinks_frame,text="Pepsi (Medium)",font=("African",12),bg="cyan").place(x="200px",y="160px")
    pepsi_medium_price = Label(drinks_frame,text="\u20B9 50",font=("African",12),bg="cyan").place(x="240px",y="180px")
    pepsi_medium_add = Button(text="Add",font=("African",15),command=add_pepsi_medium).place(x="230px",y="200px")

    my_image3 = ImageTk.PhotoImage(Image.open("Drinks/pepsi_large.jpg"))
    my_lable3 = Label(image=my_image3).place(x="400px",y="40px")
    pepsi_large = Label(drinks_frame,text="Pepsi (King)",font=("African",12),bg="cyan").place(x="415px",y="160px")
    pepsi_large_price = Label(drinks_frame,text="\u20B9 75",font=("African",12),bg="cyan").place(x="440px",y="180px")
    pepsi_large_add = Button(text="Add",font=("African",15),command=add_pepsi_king).place(x="430px",y="200px")

    my_image4 = ImageTk.PhotoImage(Image.open("Drinks/chocolate_shake.jpg"))
    my_lable4 = Label(image=my_image4).place(x="10px",y="250px")
    shake = Label(drinks_frame,text="Chocolate Shake",font=("African",12),bg="cyan").place(x="10px",y="370px")
    shake_price = Label(drinks_frame,text="\u20B9 85",font=("African",12),bg="cyan").place(x="55px",y="390px")
    shake_add = Button(text="Add",font=("African",15),command=add_chocolate).place(x="40px",y="410px")

    my_image5 = ImageTk.PhotoImage(Image.open("Drinks/ice_tea.jpg"))
    my_lable5 = Label(image=my_image5).place(x="200px",y="250px")
    ice_tea = Label(drinks_frame,text="Ice Tea",font=("African",12),bg="cyan").place(x="230px",y="370px")
    ice_tea_price = Label(drinks_frame,text="\u20B9 65",font=("African",12),bg="cyan").place(x="240px",y="390px")
    ice_tea_add = Button(text="Add",font=("African",15),command=add_ice_tea).place(x="230px",y="410px")

    my_image6 = ImageTk.PhotoImage(Image.open("Drinks/coffee.jpg"))
    my_lable6 = Label(image=my_image6).place(x="400px",y="250px")
    coffee = Label(drinks_frame,text="Coffee",font=("African",12),bg="cyan").place(x="430px",y="370px")
    coffee_price = Label(drinks_frame,text="\u20B9 55",font=("African",12),bg="cyan").place(x="440px",y="390px")
    add = Button(text="Add",font=("African",15),command=add_coffee).place(x="430px",y="410px")

    drinks_frame.mainloop()

# drinks()