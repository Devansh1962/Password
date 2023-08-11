# password generator

from tkinter import*
import random
import string
def get_pass():
    pass1=string.ascii_letters + string.digits + string.punctuation
    password = ""
    for x in range (passint.get()): #loop to generate the user given length for password
        password = password + random.choice(pass1)
        passtr.set(password)

def destroy():
    p=entry3.config()
    p.destroy()



root = Tk()
root.geometry("400x400")
root.title("PASSWORD GENERATOR")
root.resizable(0,0)
label1=Label(root,text="PASSWORD GENERATOR",fg="blue", font="lucida 15 bold")
label1.pack(pady=15)
label2=Label(root, text = "Enter user name:",font=4)
label2.place(x=10,y=70)
entry1=Entry(root,width=25)
entry1.place(x=180,y=70)
label3=Label(root,text = "Enter password length:", font=4)
label3.place(x=10,y=110)
passint=IntVar()
entry2=Entry(root,textvariable=passint,width=25)
entry2.place(x=180,y=110)
label4=Label(root,text = "Generated password:",font=4)
label4.place(x=10,y=150)
passtr=StringVar()
entry3=Entry(root,textvariable=passtr,width=25)
entry3.place(x=180,y=150)
button1=Button(root,text = "GENERATE PASSWORD",bg="sky blue",font=4,command=get_pass)
button1.place(x=170,y=200)
button2=Button(root,text = "ACCEPT",fg="blue",font=4)
button2.place(x=200,y=240)
button3=Button(root,text = "RESET",fg="blue",font=4,command=destroy)
button3.place(x=205,y=280)
root.mainloop()
