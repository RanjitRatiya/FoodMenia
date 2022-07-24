def homepage():
    from tkinter import Button, Label, LabelFrame,Tk,Frame
    from PIL import Image,ImageTk
    from register import register_form
    from login import login_form
    
    # homepage_frame = Tk()
    # homepage_frame.geometry("1000x800")
    homepage_frame = Frame(bg="cyan")
    homepage_frame.place(x=0,y=0,height="800",width="1000")
    exit_btn = Button(homepage_frame,text="X",font=("Arial",20),command=exit).place(y="5px",x="710px")
    my_image1 = ImageTk.PhotoImage(Image.open("Burgers/dp.jfif"))
    my_lable1 = Label(image=my_image1).place(x="270px",y="80px")
    slg = Label(homepage_frame,text=("Welcome to Maharaja Burger"),font=("Calibri 35 bold"),bg="cyan").pack(pady="230px")

    register = Button(homepage_frame,text="Register",font=("Calibri 15 bold"),command=register_form).place(x="230px",y="300px")

    login = Button(homepage_frame,text="Login",font=("Calibri 15 bold"),command=login_form).place(x="420px",y="300px")
    homepage_frame.mainloop()
# homepage()