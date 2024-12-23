# 47.00 to start

from tkinter import *
import time
from  tkinter.ttk import Combobox
from tkinter import messagebox
import re 
import pymysql
#,charset='utf8mb4'
#Connection Python to MySQL Server Database
'''
try:
    cont=pymysql.connect(host="localhost",port=3306,user="root",password="root",charset='utf8mb4',database="pydatabase")
    curs=cont.cursor()
    curs.execute("""create table Bankdata
                    (acn_no int primary key auto_increment,
                     acn_name text,
                     acn_email text,
                     acn_pass text,
                     acn_mob text,
                     acn_bal float,
                     acn_opendate text,
                     acn_gender text,
                     acn_type text)
                     """)
    
#    curs.execute("create database pydatabase;")
    cont.close()
    print("created")
except pymysql.MySQLError as e:
    print(f"Error creating database:{e}")
'''    

#window 
win=Tk()
win.state('zoomed')
win.configure(bg='pink')
win.resizable(width=False,height=False)

#Tital Name 
tital=Label(win,text='Banking Automation',font=('italic',30,'bold','underline'),)
tital.pack()

# Date time 
dt=time.strftime("%d/%b/%Y")
date=Label(win,text=f"{dt}",font=('italic',19,'bold'),bg='pink',fg='blue')
date.place(relx=.80,rely=.1)


# Input Feild
def main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.14, relwidth=1,relheight=.90)
    def for_pass():
        frm.destroy()
        forgetpass_screen()

    def log_in():
        global acn
        acn=e_acn.get()
        pwd=e_pass.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showwarning("Validation","Please fill befor details")
        else:
            acn=e_acn.get()
            pwd=e_pass.get()
            cont=pymysql.connect(host='localhost',password='root',user='root',port=3306,database='pydatabase',charset='utf8mb4')
            curs=cont.cursor()
            curs.execute('select * from bankdata  where acn_no= %s and acn_pass= %s',(acn,pwd))
            tup=curs.fetchone()
            cont.commit()
            cont.close()
            if tup ==None:
                messagebox.showerror('Error','record not found')
            else:
                frm.destroy()
                quelify_user()
    def clear():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        e_acn.focus()
         
    lbl_acn=Label(frm,text="ACN",font=("arial",19,"bold"),bg="powder blue")
    lbl_acn.place(relx=.2,rely=.1)
    
    e_acn=Entry(frm,font=('italic',20,'bold'),bd=4)
    e_acn.place(relx=.3,rely=.1)
    e_acn.focus()
    #Password input
    lbl_pass=Label(frm,text="Pass",font=("arial",19,"bold"),bg="powder blue")
    lbl_pass.place(relx=.2,rely=.2)
    
    e_pass=Entry(frm,font=("italic",20,"bold"),bd=3,show="#")
    e_pass.place(relx=.3,rely=.2)
    
    # Button Login
    btn_login=Button(frm,command=log_in,text="login",font=("italic",16,"bold"),bd=3,bg="powder blue")
    btn_login.place(relx=.3,rely=.3)
    #clear Button
    btn_clear=Button(frm,command=clear,text="clear",font=("italic",16,"bold"),bd=3,bg="powder blue")
    btn_clear.place(relx=.486,rely=.3)

    # Forget Password Buton
    btn_fgp=Button(frm,command=for_pass,text="Forget password",font=("italic",16,"bold"),bd=3,bg="powder blue")
    btn_fgp.place(relx=.348,rely=.42)
    # Opne new Account Button
    btn_opneAccount=Button(frm,command=New_User,text="Open Account",font=("italic",15,"bold"),bd=3,bg="powder blue")
    btn_opneAccount.place(relx=.359,rely=.3)


#________________________Forget Password Button_________________________________

    
def forgetpass_screen():
    frm=Frame(win)
    frm.configure(bg="powder blue")
    frm.place(relx=.0,rely=.15,relwidth=1,relheight=.85)

    def Btn_backe():
        frm.destroy()
        main_screen()
    def clear():
        e_acn.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        e_acn.focus()
    def submit_db():
        global acn
        acn=e_acn.get()
        email=e_email.get()
        mob=e_mob.get()
            
        import pymysql
        cont=pymysql.connect(host="localhost",port=3306,user="root",password="root",charset='utf8mb4',database="pydatabase")
        curs=cont.cursor()
        curs.execute('''select acn_pass from bankdata where acn_no=%s and acn_email=%s and acn_mob=%s ''',(acn,email,mob))
        tup=curs.fetchone()
        if len (acn) == 0 or len(email)==0 or len(mob)==0:
            messagebox.showerror("Empty error field","Empty not allowed")
            return
        elif tup is None:
            messagebox.showerror("404","record not found")
        else:
            messagebox.showinfo("Pass key",f"your password: {tup[0]}")
        cont.commit()
        cont.close()
        e_acn.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
    btn_back=Button(frm,command=Btn_backe,text="<",font=("italic",20,"bold"),bd=5,bg="powder blue")
    btn_back.place(relx=0,rely=0)
    
    #ACN input
    lbl_acn=Label(frm,text="ACN",font=("italic",16,"bold"),bg="powder blue")
    lbl_acn.place(relx=.3,rely=.1)
    e_acn=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()

    #Email input
    lbl_email=Label(frm,text="Email",font=("italic",16,"bold"),bg="powder blue")
    lbl_email.place(relx=.3,rely=.2)
    e_email=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_email.place(relx=.4,rely=.2)

    #Mobile No input
    lbl_mob=Label(frm,text="Mob No",font=("arial",15,"bold"),bd=5,bg="powder blue")
    lbl_mob.place(relx=.3,rely=.3)
    e_mob=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_mob.place(relx=.4,rely=.3)
    #Button Login
    btn_get=Button(frm,command=submit_db,text="submit",font=("italic",15,"bold"),bd=4,bg="powder blue")
    btn_get.place(relx=.42,rely=.4)

    #Clear Input Button
    btn_clear=Button(frm,command=clear,text="clear",font=("arial",15,'bold'),bd=4,bg="powder blue")
    btn_clear.place(relx=.51,rely=.4)

#Open New Account_____________________________________________
def New_User():
    frm=Frame(win)
    frm.configure(bg="powder blue")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.86)

    def back_btn():
        frm.destroy()
        main_screen()
    def clear():
        e_name.delete(0,"end")
        e_email.delete(0,"end")
        e_pass.delete(0,"end")
        e_mob.delete(0,"end")
        cd_gender.delete(0,"end")
        e_type.delete(0,"end")
        e_name.focus()
    def newuser_db():
        name=e_name.get()
        email=e_email.get()
        pwd=e_pass.get()
        mob=e_mob.get()
        gender=cd_gender.get()
        etype=e_type.get()
        bal=0
        opendate=time.strftime("%d/%b/%Y")

        
#New User To Data Get For Server & Connection To Server___________________________________________________
        if len(name)==0 or len(email)==0 or len(pwd)==0 or len(gender)==0 or len(etype)==0 :
            messagebox.showerror("Empty error field","Empty field not allowed")
            return
        pattern = "[A-Za-z]{4,24}"
        match=re.fullmatch(pattern,name)
        if match is None:
            messagebox.showerror("not valid name !","try 4 to 24 char !")
            return
# vikas621196@gmail.com
        pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

        match=re.fullmatch(pattern,email)
        if match is None:
            messagebox.showerror("not valid name !","try 4 to 24 char !")
            return



        
        match=re.fullmatch("[6-9][0-9]{9}",mob)
        if match==None:
            messagebox.showerror("Error !","invalid mob number !")
        else:
            True

        
#        if len(bal)>=8:
#            messagebox.showerror("Error","out of range  ammount")
#            return
            
# Create the main window
        
        import pymysql
        try:
            cont=pymysql.connect(host="localhost",port=3306,user="root",password="root",charset='utf8mb4',database="pydatabase")
            curs=cont.cursor()
            curs.execute('insert into bankdata(acn_name,acn_email, acn_pass,  acn_mob, acn_bal, acn_opendate, acn_gender, acn_type ) values(%s,%s,%s,%s,%s,%s,%s,%s)',(name,email,pwd,mob,bal,opendate,gender,etype))
#Get Account Number
            curs.execute("select max(acn_no) from bankdata")
            tup=curs.fetchone()
            data=curs.fetchall()
            cont.commit()
            cont.close()
            print("Succesfully insert data:")
            print(data)
        except pymysql.MySQLError as e:
            print(f"Error creating database: {e}")
       
        messagebox.showinfo("New User",f"created Account no={tup[0]}")
        e_name.delete(0,"end")
        e_email.delete(0,"end")
        e_pass.delete(0,"end")
        e_mob.delete(0,"end")
        cd_gender.delete(0,"end")
        e_type.delete(0,"end")

#______________________________________________________________________________________________________


    btn_back=Button(frm,command=back_btn,text="<",font=("italic",15,"bold"),bg="powder blue",bd=4)
    btn_back.place(relx=.0,rely=.0)
    #Name        
    lbl_name=Label(frm,text="Name",font=("italic",16,"bold"),bg="powder blue")
    lbl_name.place(relx=.3,rely=.1)
    e_name=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_name.place(relx=.4,rely=.1)
    e_name.focus()
    #Gmail
    lbl_email=Label(frm,text="Email",font=("italic",16,"bold"),bg="powder blue")
    lbl_email.place(relx=.3,rely=.2)
    e_email=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_email.place(relx=.4,rely=.2)
    #Password
    lbl_pass=Label(frm,text="Pass",font=("arial",15,"bold"),bd=5,bg="powder blue")
    lbl_pass.place(relx=.3,rely=.3)
    e_pass=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_pass.place(relx=.4,rely=.3)
    #Mobile
    lbl_mob=Label(frm,text="Mob No",font=("arial",15,"bold"),bd=5,bg="powder blue")
    lbl_mob.place(relx=.3,rely=.4)
    e_mob=Entry(frm,font=("italic",15,"bold"),bd=4)
    e_mob.place(relx=.4,rely=.4)
    #Gender
    lbl_gender=Label(frm,text="Gender",font=("arial",12,"bold"),bd=5,bg="powder blue")
    lbl_gender.place(relx=.3,rely=.48)
    #e_gender=Entry(frm,font=("italic",15,"bold"),bd=4)
    #e_gender.place(relx=.4,rely=.4)
    cd_gender=Combobox(frm,value=['--select--','Male','Female','Other'],font=("italic",13,"bold"))
    cd_gender.place(relx=.41,rely=.48)
    #
    lbl_type=Label(frm,text="ACNtype",font=("arial",12,"bold"),bd=5,bg="powder blue")
    lbl_type.place(relx=.3,rely=.56)
    e_type=Combobox(frm,value=['--select--','Saving','Buisness','Other'],font=("italic",13,"bold"))
    e_type.place(relx=.41,rely=.56)
                       
    #
    btn_get=Button(frm,command=newuser_db,text="login",font=("italic",15,"bold"),bd=4,bg="powder blue")
    btn_get.place(relx=.42,rely=.7)

    #Clear Input Button
    btn_clear=Button(frm,width=5,command=clear,text="clear",font=("arial",15,'bold'),bd=4,bg="powder blue")
    btn_clear.place(relx=.51,rely=.7)
              
#______________________________________________________________
def quelify_user():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    def log_Out():
        frm.destroy()
        main_screen()
    #----------------------
    def Info_Details():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)

        lbl_banner=Label(ifrm,text="This is Details Screen",font=("italic",16,"bold"),fg='blue')
        lbl_banner.place(relx=.3,rely=.0)
        
        
        cont=pymysql.connect(host="localhost",port=3306,user="root",password="root",charset='utf8mb4',database="pydatabase")
        curs=cont.cursor()
        curs.execute('select acn_opendate, acn_bal, acn_gender, acn_email, acn_mob, acn_type from  bankdata where acn_no=%s',(acn))
        tup=curs.fetchone()
        cont.close()
               
        lbl_opendate=Label(ifrm,text=f"Open Date :    {tup[0]}",font=("italic",16,"bold"),bg='white',fg='blue')
        lbl_opendate.place(relx=.2,rely=.12)
        lbl_opendate.config(padx=.1, pady=.5)
        
        lbl_bal=Label(ifrm,text=f"Balance :         {tup[1]}",font=("italic",16,"bold"),bg='white',fg='blue')
        lbl_bal.place(relx=.2,rely=.22)
        
        lbl_bal=Label(ifrm,text=f"Phone no :      {tup[4]}",font=("italic",16,"bold"),bg='white',fg='blue')
        lbl_bal.place(relx=.2,rely=.31)
        
        lbl_bal=Label(ifrm,text=f"Email :             {tup[3]}",font=("italic",16,"bold"),bg='white',fg='blue')
        lbl_bal.place(relx=.2,rely=.41)
        
        lbl_bal=Label(ifrm,text=f"Account :        {tup[5]}",font=("italic",16,"bold"),bg='white',fg='blue')
        lbl_bal.place(relx=.2,rely=.51)
        
        lbl_bal=Label(ifrm,text=f"Gender :          {tup[2]}",font=("italic",16,"bold"),bg='white',fg='blue')
        lbl_bal.place(relx=.2,rely=.61)
        
        

#___________________________________________________________________________________________________________

    def Info_update():

            ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
            ifrm.configure(bg='white')
            ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)

            lbl_banner=Label(ifrm,text="This is Update Screen",font=("italic",16,"bold"),fg='blue')
            lbl_banner.place(relx=.3,rely=.0)

            cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
            curs=cont.cursor()
            curs.execute("select  acn_name, acn_email, acn_pass, acn_mob from bankdata where acn_no=%s",(acn,))
            tup=curs.fetchone()
            cont.commit()
            cont.close()
            
#            lbl_wel=Label(ifrm,text="This is Update Screen",font=('arial',20,'bold'),bg='white',fg='blue')
#            lbl_wel.pack()

            #Name        
            lbl_name=Label(ifrm,text="Name",font=("italic",16,"bold"),bg="white")
            lbl_name.place(relx=.1,rely=.1)
            e_name=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_name.place(relx=.1,rely=.2)
            e_name.insert(0,tup[0])
            e_name.focus()
            #Gmail
            lbl_email=Label(ifrm,text="Email",font=("italic",16,"bold"),bg="white")
            lbl_email.place(relx=.1,rely=.4)
            e_email=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_email.place(relx=.1,rely=.5)
            e_email.insert(0,tup[1])

            #Password
            lbl_pass=Label(ifrm,text="Pass",font=("arial",15,"bold"),bd=5,bg="white")
            lbl_pass.place(relx=.5,rely=.1)
            e_pass=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_pass.place(relx=.5,rely=.2)
            e_pass.insert(0,tup[2])
            
            #Mobile
            lbl_mob=Label(ifrm,text="Mob No",font=("arial",15,"bold"),bd=5,bg="white")
            lbl_mob.place(relx=.5,rely=.4)
            e_mob=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_mob.place(relx=.5,rely=.5)
            e_mob.insert(0,tup[3])
            
            
            def Update():
                name=e_name.get()
                gmail=e_email.get()
                pwd=e_pass.get()
                mob=e_mob.get()

                cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                curs=cont.cursor()
                curs.execute("update  bankdata set acn_name=%s, acn_email=%s, acn_pass=%s, acn_mob=%s where acn_no=%s",(name,gmail,pwd,mob,acn))
                cont.commit()
                cont.close()
                messagebox.showinfo("update","record updated")
                                     
                Info_Details()
            btn=Button(ifrm,text="Update",command=Update,font=("italic",16,"bold"),fg='blue')    
            btn.place(relx=.6,rely=.7)
#_________________________________________________________________________________________________________

    def Info_deposit():
            ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
            ifrm.configure(bg='white')
            ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)

            lbl_banner=Label(ifrm,text="This is Deposit Screen",font=("italic",16,"bold"),fg='blue')
            lbl_banner.place(relx=.3,rely=.0)

            lbl_amt=Label(ifrm,text="Ammount",font=("italic",16,"bold"),bg="white")
            lbl_amt.place(relx=.1,rely=.3)
            e_amt=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_amt.place(relx=.25,rely=.3)
           
            def deposit():
                bal=e_amt.get()
                
                if not bal.isdigit() or float(bal)==0:
                    messagebox.showerror("Error","Not valid number")
                    return
                if len(bal)>=8:
                    messagebox.showerror("Error","out of range  ammount")
                    return

                bal=float(bal)                  
                cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                curs=cont.cursor()
                curs.execute("update  bankdata set acn_bal= acn_bal+%s where acn_no=%s ;",(bal,acn))
                tup=curs.fetchone()
                cont.commit()
                cont.close()
                messagebox.showinfo("update",f"{bal} Ammount updated")
                Info_Details()

            btn_amt=Button(ifrm,command=deposit,text="Deposit",font=("italic",16,"bold"),fg='blue')    
            btn_amt.place(relx=.3,rely=.5)
#__________________________________________________________________________________________________________           
    def Info_withdraw():
            ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
            ifrm.configure(bg='white')
            ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)

            lbl_banner=Label(ifrm,text="This is Withdraw Screen",font=("italic",16,"bold"),fg='blue')
            lbl_banner.place(relx=.3,rely=.0)

            lbl_amt=Label(ifrm,text="Ammount",font=("italic",16,"bold"),bg="white")
            lbl_amt.place(relx=.1,rely=.3)
            e_amt=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_amt.place(relx=.25,rely=.3)
           
            def withdraw():
                bal=e_amt.get()
                    
                if not bal.isdigit():
                    messagebox.showerror("Error","Not valid ammount")
                    return

                if len(bal)>=8:
                    messagebox.showerror("Error","out of range  ammount")
                    return
                
                bal=float(bal)

                cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                curs=cont.cursor()
                curs.execute("select  acn_bal from bankdata where acn_no=%s",(acn))
                tup=curs.fetchone()
                currentBal=tup[0]
                cont.commit()
                cont.close()
#       if currentBal>=100:
                if currentBal>=bal:
                    cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                    curs=cont.cursor()
                    curs.execute("update  bankdata set acn_bal= acn_bal-%s where acn_no=%s ;",(bal,acn))
                    tup=curs.fetchone()
                    cont.commit()
                    cont.close()
                    messagebox.showinfo("Withdraw",f"{bal} Ammount withdraw")
                    Info_Details()
                else:
                    messagebox.showerror("Error !","Insufficient balance!")
                    

            btn_with=Button(ifrm,command=withdraw,text="Withdraw",font=("italic",16,"bold"),fg='blue')    
            btn_with.place(relx=.3,rely=.5)
#__________________________________________________________________________________________________________           
            
    def Info_transfer():
            ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
            ifrm.configure(bg='white')
            ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)

            lbl_banner=Label(ifrm,text="This is Transfer Screen",font=("italic",16,"bold"),fg='blue')
            lbl_banner.place(relx=.3,rely=.0)



            lbl_amt=Label(ifrm,text="Ammount pay ",font=("italic",16,"bold"),bg="white")
            lbl_amt.place(relx=.1,rely=.1)
            e_amt=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_amt.place(relx=.1,rely=.2)
            e_amt.focus()
            # To Pay
            lbl_to=Label(ifrm,text="To send Acn No ?",font=("italic",16,"bold"),bg="white")
            lbl_to.place(relx=.1,rely=.4)
            e_to=Entry(ifrm,font=("italic",15,"bold"),bd=4)
            e_to.place(relx=.1,rely=.5)
            e_to.focus()

            def transfer():
                global pay_to
                pay_to=e_to.get()
                bal=e_amt.get()

                symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`','!']
#______________________________________________________________________________________
                
                for char in bal:
                    if char.isalpha():
                        messagebox.showwarning("404!!"," Not char Account!")
                        return
                for symbol in symbols:
                    if symbol in bal:
                        messagebox.showwarning("404!!"," Not valid symbol Account!")
                        return

                
                for char in pay_to:
                    if char.isalpha():
                        messagebox.showwarning("404!!"," Not char bal!")
                        return
                for symbol in symbols:
                    if symbol in pay_to:
                        messagebox.showwarning("404!!"," Not valid symbol bal!")
                        return


                if not bal:
                    messagebox.showwarning("Ammount pay ?", "Ammount field can't be empty!")
                    return
                    
                if not pay_to:
                    messagebox.showwarning("To send Acn No ?", "Account number can't be empty!")
                    return
                if len(bal)>=8:
                    messagebox.showerror("Error","out of range  ammount")
                    return

                if bal==0 or float(bal)==0:
                    messagebox.showerror("Error","Not valid ammount")
                    return 
                bal=float(bal)


                if float(bal)==0:
                    messagebox.showerror("Error","Not valid ammount")
                    return 
                bal=float(bal)
                

                cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                curs=cont.cursor()
                curs.execute("select acn_bal acn_no from bankdata where  acn_no=%s ;",(acn))
#          current_bal=curs.execute("select  acn_bal from bankdata where  acn_no=%s ;",(acn))
                tup=curs.fetchone()
                current_bal=tup[0]
                cont.commit()
                cont.close()
                current_bal= float(current_bal)


                cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                curs=cont.cursor()
                curs.execute("select acn_no from bankdata where  acn_no=%s ;",(pay_to))
                tup=curs.fetchone()
                cont.commit()
                cont.close()

                if tup is None :
                    messagebox.showwarning("404!!"," Not found this Account!")
                    return 

                if pay_to == acn:
                    messagebox.showwarning("404!!"," Not send || becouse this account!")
                    return
                
                if current_bal>=bal:
                    cont=pymysql.connect(host="localhost",password="root",user="root",port=3306,database="pydatabase")
                    curs=cont.cursor()
                    curs.execute("update  bankdata set acn_bal=acn_bal+%s where acn_no=%s;",(bal,pay_to))
                    curs.execute("update  bankdata set acn_bal=acn_bal-%s where acn_no=%s;",(bal,acn))
                    cont.commit()
                    cont.close()
                    messagebox.showwarning("Update"," Succesfull transjuction!")
                else:
                    messagebox.showwarning("Warning"," not sufficient balnce!")


            btn_with=Button(ifrm,command=transfer,text="Transfer",font=("italic",16,"bold"),fg='blue')    
            btn_with.place(relx=.15,rely=.67)

            
    def Info_setting():
            ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
            ifrm.configure(bg='white')
            ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.5)

            lbl_banner=Label(ifrm,text="This is Setting Screen",font=("italic",16,"bold"),fg='blue')
            lbl_banner.place(relx=.3,rely=.0)


    cont=pymysql.connect(host="localhost",port=3306,user="root",password="root",charset='utf8mb4',database="pydatabase")
    curs=cont.cursor()
    curs.execute("select acn_name from bankdata where acn_no=%s ",(acn,))
    tup=curs.fetchone()
    cont.commit()
    cont.close()


    lbl_out=Label(frm,text='Wellcome'f': {tup[0]}',font=('italic',20,'bold'),bg='powder blue',bd=4)
    lbl_out.place(relx=.0,rely=0)
    btn_out=Button(frm,command=log_Out,text="logOut",font=("arial",15,'bold'),bd=4,bg="powder blue")
    btn_out.place(relx=.9,rely=0)

    #Wellcome Screen Button List
    btn_details=Button(frm,command= Info_Details,text="Details",font=('italic',18,'bold'),width=11,bd=5)
    btn_details.place(relx=0,rely=.1)

    btn_update=Button(frm,command=Info_update,text="Update",font=('italic',18,'bold'),width=11,bd=5)
    btn_update.place(relx=0,rely=.21)

    btn_deposit=Button(frm,command=Info_deposit,text="Depost",font=('italic',18,'bold'),width=11,bd=5)
    btn_deposit.place(relx=0,rely=.32)

    btn_withdraw=Button(frm,command=Info_withdraw,text="Withdraw",font=('italic',18,'bold'),width=11,bd=5)
    btn_withdraw.place(relx=0,rely=.43)
    
    btn_transfer=Button(frm,command=Info_transfer,text="Transfer",font=('italic',18,'bold'),width=11,bd=5)
    btn_transfer.place(relx=0,rely=.54)

    btn_setting=Button(frm,command=Info_setting,text="Setting",font=('italic',18,'bold'),width=11,bd=5)
    btn_setting.place(relx=0,rely=.65)


main_screen()
win.mainloop()
