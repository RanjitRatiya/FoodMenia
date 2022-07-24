def payment_done():

    from tkinter import Tk,Radiobutton,IntVar,messagebox,Label,Button,Frame
    import sqlite3
    from mymenu import menu
    # from cart import set_price

    def sel():
    #    selection = "You selected the option " + str(var.get())
    #    label.config(text = selection)
        conn = sqlite3.connect('Burger.db')
        c = conn.cursor()
        c.execute('delete from cart')
        conn.commit()
        conn.close()
        order = str(var.get())
        if order == '1':
            messagebox.showinfo('Payment',"Your order placed through Cash on Delievery.")
        elif order == '2':
            messagebox.showinfo('Payment','Your order placed through Debit Card.')
        elif order == '3':
            messagebox.showinfo('Payment','Your order placed through Credit Card.')
        else:
            messagebox.showinfo('Payment','Default order placed through Cash on Delievery.')
        menu()
    

    # root = Tk()

    payment_frame = Frame(bg="cyan")
    payment_frame.place(x=0,y=0,height="800",width="1000")

    var = IntVar()

    payment_gateway = Label(payment_frame,font="Calibri 45 bold",text='Payment Gateway',bg='cyan',fg='black').place(x="200px",y="10px")

    opt = Label(payment_frame,font="Calibri 30 bold",text='Choose Your Option',bg='cyan',fg='black').place(x="240px",y="80px")

    cod= Radiobutton(payment_frame, text="Cash on Delievery", variable=var, value=1,bg="cyan",font='Calibri 20 bold').place(x="260px",y="150px")

    debit = Radiobutton(payment_frame, text="Debit Card", variable=var, value=2,bg="cyan",font='Calibri 20 bold').place(x="260px",y="200px")

    credit = Radiobutton(payment_frame, text="Credit Card", variable=var, value=3,bg="cyan",font='Calibri 20 bold').place(x="260px",y="250px")

    # label = Label(payment_frame)
    # label.pack()
    b1 = Button(payment_frame,text='Make Payment',command=sel,font='Calibri 20 bold').place(x="270px",y="350px")
    # set_price()
    payment_frame.mainloop()

# payment_done()