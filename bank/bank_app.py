from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from signup import Signup
from login import Login
from credit import CREDIT
from debit import DEBIT
from profile import PROFILE

class Bank(Signup,Login,CREDIT,DEBIT,PROFILE):

    def __init__(self,master):
        Signup.__init__(self)
        Login.__init__(self)
        CREDIT.__init__(self)
        DEBIT.__init__(self)
        PROFILE.__init__(self)


        self.master = master()
        self.master.title('BANK Application')
        self.ws=self.master.winfo_screenwidth()
        self.hs=self.master.winfo_screenheight()
        self.master.wm_minsize(self.ws,self.hs)
        self.master.configure(background='#666666')
        self.menu_forget = False
        self.upd_pass=False
        self.upd_name=False

    def run(self):
        self.main_frame()

    def menu(self):

        self.menu = tk.Frame(self.master,bg="#777777")

        self.m_l1 = Label(self.menu,text='Welcome {}'.format(self.user),bg="#777777",font=('Times','20','bold'),fg="#ffffff")
        self.m_l1.grid(row=0,column=0,padx=60,pady=10)

        self.m_b1 = tk.Button(self.menu,text='DEBIT',bg="#777777",width=10,font=('Times','20','bold'),command=self.debframe,fg="#003b8b")
        self.m_b1.grid(row=1,column=0,padx=60,pady=10)

        self.m_b2 = tk.Button(self.menu,text='CREDIT',width=10,bg="#777777",font=('Times','20','bold'),command=self.credit_Balance,fg="#003b8b")
        self.m_b2.grid(row=2,column=0,padx=76,pady=20)

        self.m_b3 = tk.Button(self.menu,text='Profile',bd=0,bg="#777777",font=('Times','20','bold'),command=self.show_profile,fg="#aadcba")
        self.m_b3.grid(row=0,column=1,padx=76,pady=25)


        self.m_b4 = tk.Button(self.menu,text='LOGOUT',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_f,fg="#ff0000")

        self.m_b4.grid(row=3,column=1,padx=76,pady=15)
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)


    def show_f(self):
        self.menu.grid_forget()
        self.menu_forget = True
        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)



    def main_frame(self):

        self.f = Frame(self.master,bg='#777777')
        Bank.username = StringVar()
        Bank.password = StringVar()

        self.l0 = Label(self.f,text="Welcome To PYTHON Banking Services",bg='#777777',font=('Times','20','bold'),fg='#abcdef')
        self.l0.grid(row=0,column=0,columnspan=3)

        self.l1 = Label(self.f,text='UserName : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
        self.l1.grid(row=1,column=0,ipadx=40,pady=30)

        self.e1 = Entry(self.f,textvariable=Bank.username,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e1.grid(row=1,column=1)

        self.l2 = Label(self.f,text='Password : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
        self.l2.grid(row=2,column=0)



        self.e2 = Entry(self.f,textvariable=Bank.password,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e2.grid(row=2,column=1,padx=20)

        self.b3 = Button(self.f,bg='#777777',text='forget password ?',font=('Times','12','bold'),command=self.fpass,fg='red',width=30,bd=0)
        self.b3.grid(row=3,column=1)

        self.b1 = Button(self.f,bg='#777777',text='LOGIN',font=('Times','20','bold'),command=self.login,fg='#123456')
        self.b1.grid(row=4,column=0,columnspan=4,padx=19,pady=31)

        self.b2 = Button(self.f,bg='#777777',text='SIGNUP',font=('Times','20','bold'),command=self.signup,fg='#123456')
        self.b2.grid(row=4,column=1,columnspan=4)
        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)

    def fpass(self):
        messagebox.showinfo("PRIVACY","Due to your privacy reason you have to meet in person to nearest branch with all documents to update your password.")

    def show_sf(self):
            self.sp.grid_forget()
            self.menu_forget = True
            self.f.grid(padx=self.ws*.3,pady=self.hs*.2)




root = Bank(Tk)
root.run()

mainloop()
