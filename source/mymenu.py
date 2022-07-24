def menu():
    from tkinter import Label,Tk,Frame,Button
    from PIL import ImageTk,Image
    from burger import burger
    from combo import combo
    from drinks import drinks
    from fries import fries
    from cart import cart
    # root = Tk()
    # root.geometry("1000x800")
    menu_frame = Frame(bg="cyan",height=800,width=1000)
    menu_frame.place(x=0,y=0)
    cart_lable = Button(menu_frame,text=("🛒"),font=("Arial",20),command=cart).place(height="50px",x="700px")
    my_image1 = ImageTk.PhotoImage(Image.open("Menu/Burger.png"))
    my_lable1 = Label(image=my_image1).place(x="20px",y="40px")
    Burger = Button(text="Burgers",font=("African",20),command=burger).place(x="70px",y="290px")

    my_image2 = ImageTk.PhotoImage(Image.open("Menu/Drinks.jpg"))
    my_lable2 = Label(image=my_image2).place(x="400px",y="30px")
    Drinks = Button(text="Drinks",font=("African",20),command=drinks).place(x="450px",y="310px")

    my_image4 = ImageTk.PhotoImage(Image.open("Menu/Fries.jpg"))
    my_lable4 = Label(image=my_image4).place(x="20px",y="370px")
    Fries = Button(text="Fries",font=("African",20),command=fries).place(x="80px",y="540px")

    my_image6 = ImageTk.PhotoImage(Image.open("Menu/Combo.jpg"))
    my_lable6 = Label(image=my_image6).place(x="400px",y="370px")
    Combo_Offers = Button(text="Combo Offers",font=("African",20),command=combo).place(x="410px",y="540px")

    menu_frame.mainloop()
# menu()