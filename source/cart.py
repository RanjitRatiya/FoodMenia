def cart():
    from tkinter import Label,Tk,Frame,Button,messagebox
    import sqlite3
    from mymenu import menu
    from payment2 import payment_done
    # root = Tk()
    # root.geometry("1000x800")

    cart_frame = Frame(bg="cyan")
    cart_frame.place(x=0,y=0,height=800,width=1000)

    back = Button(cart_frame,text="<=",font=("Calibri",15),command=menu).place(x=0,y=0)

    conn = sqlite3.connect('Burger.db')
    c = conn.cursor()
    c.execute('select * from cart')
    r = c.fetchall()

    # flag=0
    num=2
    total_price = 0
    for i in r:
        item = Label(cart_frame,text=i[0],font='time 15 bold',fg="black",bg="cyan").grid(row=num,column=0,padx=90,pady=20)

        price = Label(cart_frame,text=i[1],font='time 15 bold',fg="black",bg="cyan").grid(row=num,column=1,padx=90,pady=20)
        num+=1
        total_price=total_price+i[1]

    conn.commit()
    conn.close()

    total_la = Label(cart_frame,text='Total Amount : ',font='time 15 bold',fg="black",bg="cyan").place(y="500px",x="230px")    
    total_va = Label(cart_frame,text=(total_price,"\u20B9"),font='time 15 bold',fg="black",bg="cyan").place(y="500px",x="350px")
    
    def total():
        messagebox.showinfo("Order",f"Your Order is placed Successfully.\n Total Amount is {total_price} \u20B9")
        payment_done()
    
    conn = sqlite3.connect('Burger.db')
    c = conn.cursor()
    c.execute('INSERT INTO cartB SELECT * FROM cart')
    conn.commit()
    conn.close()
    
    payment = Button(cart_frame,text="Place Order",font="calibri 15 bold",command=total).place(y="550px",x="320px")
    # print(total_price)
    

    cart_frame.mainloop()
# cart()