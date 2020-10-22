from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
class quiz:
    def __init__(self,root):
        self.root=root
        self.root.title("Quiz App")
        self.root.geometry("1350x690+0+0")
        root.resizable(0,0)
        self.root.config(bg="light blue") 
        root.iconbitmap('favicon.ico')       
       #============Variable defined=================
        self.sql_port_no=StringVar()
        self.sql_password_no=StringVar()
        self.admin_password=StringVar()
        self.n_quiz_nm_var=StringVar()
        self.n_class_nm_var=StringVar()
        self.no_of_qn_quiz_var=StringVar()
        self.add_qn_class_var=StringVar()
        self.add_qn_quiz_var=StringVar()
        self.ans_typ=StringVar()
        self.question_var=StringVar()
        self.mcq_correct_entry_var=StringVar()
        self.participant_name_var=StringVar()
        self.mcq_option2_txt=StringVar()
        self.mcq_option3_txt=StringVar()
        self.mcq_option4_txt=StringVar()
        global mcq_option1_txt
        mcq_option1_txt=StringVar()
        self.Short_Answer_Status_var=StringVar()
        self.participant_id_var=StringVar()
        self.add_participant_class_var=StringVar()
        self.mcq_correct_entry=StringVar()
        self.answer_type=StringVar()
        self.n_quiz_name_var=StringVar()
        self.participant_play_id_var=IntVar()
        self.participant_play_id_var_int=IntVar()
        self.participant_play_class_var=StringVar()
        self.participant_quiz_name_select_var=StringVar()
        self.option1_ans=StringVar()
        self.option1_ans.set("")
        self.chk_quiz_name_select_var=StringVar()
        self.correct_ans_count=0
        self.no_of_qn_count=0
        self.yet_to_be_calculated=0
        self.chk_id_var=StringVar()
        self.chk_quiz_var=StringVar()
        self.by_quiz_class_var=StringVar()
        self.by_quiz_quiz_var=StringVar()
        self.by_part_id_var=StringVar()
        
        #===========================================================================================================
        for widget in self.root.winfo_children():
            widget.destroy()
        self.start_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.start_frame.pack()        
        self.sql_port=Label(self.start_frame,text=" Port No. ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.sql_port.grid(row=0,column=0,pady=50,padx=20,sticky="w")
        self.txt_sql_port=Entry(self.start_frame,width=30,textvariable=self.sql_port_no, font=("times new roman",30,"bold"),bd=5)
        self.txt_sql_port.grid(row=0,column=1,pady=50,padx=20)
        self.sql_password=Label(self.start_frame,text=" Password ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.sql_password.grid(row=1,column=0,pady=50,padx=20,sticky="w")
        self.txt_sql_password=Entry(self.start_frame,width=30,textvariable=self.sql_password_no,show="*", font=("times new roman",30,"bold"),bd=5)
        self.txt_sql_password.grid(row=1,column=1,pady=50,padx=20)
        self.admin_btn=Button(self.start_frame,text="Submit",width=10,bd=5,cursor="hand2",command=self.m_frame,font=("times new roman",30,"bold"),bg="orange").grid(row=2,column=1,padx=275,pady=10)                      
    
    def m_frame(self):
        if self.sql_password_no.get() != "" and self.sql_port_no.get() != "":
            try: 
                try:
                    con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),charset="utf8")
                    cur=con.cursor()
                    cur.execute("")
                    con.commit()
                    con.close()
                    self.ok()
                    try:
                        con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),charset="utf8")
                        cur=con.cursor()
                        cur.execute("create database quiz")
                        con.commit()
                        con.close()
                        self.ok()
                    except:
                        pass
                except Exception as es:
                        messagebox.showerror("Error",es)                
            except Exception as es: 
                messagebox.showerror("Error",es)
        else:
            messagebox.showerror("!ERROR!","All details ar must.")
    def ok(self):
        if self.sql_password_no.get() != "" and self.sql_port_no.get() != "":
            try:
                con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                cur=con.cursor()
                cur.execute("create table quiz_name(Class varchar (100),Name_of_quiz varchar (100))")
                cur.execute("create table participant_name (ID int NOT NULL AUTO_INCREMENT,Name varchar(200),Class varchar(200), PRIMARY KEY (ID))")
                con.commit()
                con.close()
                self.m_frame_def()
            except:
                self.m_frame_def()

    def m_frame_def(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        #=======Main Frame======================================================+       
        self.m_frame=Frame(self.root,relief=RIDGE,bd=4,bg="light blue")
        self.m_frame.pack()
        self.m_title=Label(self.m_frame,text="          Login As            ",fg="Black",bg="yellow", font=("times new roman","50","bold","underline"))
        self.m_title.pack()   
        #=======user admin selection frame========================
        self.user_admin_frame=Frame(self.m_frame,relief=RIDGE,bd=4,bg="dark blue")
        self.user_admin_frame.pack()#place(x=350,y=100,height=450,width=800
        self.admin_btn=Button(self.user_admin_frame,text="Admin",width=10,font=("times new roman",30,"bold"),bd=5,cursor="hand2",bg="orange",command=self.admin_home).grid(row=0,column=0,padx=275,pady=10)
        self.participant_btn=Button(self.user_admin_frame,text="Participant",width=10,bd=5,cursor="hand2",font=("times new roman",30,"bold"),command=self.participant_home_def,bg="orange").grid(row=1,column=0,padx=10,pady=100)
        self.start_frame.destroy()    
        
    def admin_home(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.m_frame.destroy()
        self.user_admin_frame.destroy()
        self.user_admin_frame.destroy()
        self.start_frame.destroy()
        self.m_title.destroy()               
        self.admin_btn_frame=Frame(self.root,relief=RIDGE,bd=6,bg="brown")
        self.admin_btn_frame.pack(fill=Y,side='right')
        self.admin_add_quiz_btn=Button(self.admin_btn_frame,text="Add Quiz",width=10,height=3,padx=22,cursor="hand2",command=self.add_quiz,font=("times new roman",15,"bold"),bg="orange",bd=5).pack()
        self.admin_add_qs_btn=Button(self.admin_btn_frame,text="Add Question",width=10,height=3,command=self.add_qn,padx=22,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",bd=5).pack()
        self.admin_add_p_btn=Button(self.admin_btn_frame,text="Add Participant",width=10,height=3,padx=22,cursor="hand2",command=self.add_participant,font=("times new roman",15,"bold"),bg="orange",bd=5).pack()
        self.admin_chk_ans_btn=Button(self.admin_btn_frame,text="Check Answers",width=10,height=3,padx=22,command=self.chk_ans,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",bd=5).pack()
        self.admin_chk_his_btn=Button(self.admin_btn_frame,text="Check History",width=10,height=3,padx=22,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",bd=5,command=self.chk_his_def).pack()
        self.admin_new_pass_btn=Button(self.admin_btn_frame,text="New Password",width=10,height=3,padx=22,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",bd=5).pack()
        self.admin_about_btn=Button(self.admin_btn_frame,text="About",width=10,height=2,padx=22,command=self.about_def,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",bd=5).pack()
        self.admin_logout_btn=Button(self.admin_btn_frame,text="Logout",width=10,height=2,padx=22,command=self.m_frame_def,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",bd=5).pack()      
        self.image_intro()
    
    def image_intro(self):    
        self.img = PhotoImage(file="admin_home.png")
        self.panel = Label(self.root, image =self.img,bd=5,highlightbackground="yellow")
        self.panel.pack()
        
    def add_quiz(self):        
        for widget in self.root.winfo_children():
            widget.destroy()            
        self.admin_home()
        self.panel.destroy()
        self.add_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.add_quiz_frame.pack()       
        self.n_quiz_nm=Label(self.add_quiz_frame,text=" Quiz Name ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.n_quiz_nm.grid(row=0,column=0,pady=50,padx=20,sticky="w")
        self.txt_n_quiz_nm=Entry(self.add_quiz_frame,width=30,textvariable=self.n_quiz_nm_var, font=("times new roman",30,"bold"),bd=5)
        self.txt_n_quiz_nm.grid(row=0,column=1,pady=50,padx=20)
        self.class_of_quiz=Label(self.add_quiz_frame,text=" Class           ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.class_of_quiz.grid(row=1,column=0,pady=50,padx=20,sticky="w") 
        self.Class=ttk.Combobox(self.add_quiz_frame,width=30,height=19, textvariable=self.n_class_nm_var,font=("times new roman",30,"bold"),state="readonly")
        self.Class['values']=("6","7","8","9","10","11","12","Python","Java","HtmlandCSS","QBasic","C","C_plus_plus","C_plus","C_sharp","Oracle","MySql","FoxPro","Other")
        self.Class.grid(row=1,column=1,padx=20,pady=10)
        self.Class.set("Select")
        self.admin_add_quiz_finall_btn=Button(self.add_quiz_frame,text="Add Quiz",width=30,command=self.add_quiz_final,height=2,padx=22,font=("times new roman",20),bg="yellow",bd=5).grid(row=4,column=1)

    def add_quiz_final(self):
        if self.n_class_nm_var.get() != "Select" and self.n_quiz_nm_var.get().lstrip()!="" :
            try:
                con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                cur=con.cursor()
                cur.execute("create table "+self.n_quiz_nm_var.get()+"_"+self.n_class_nm_var.get()+"(participant_id varchar(50), Name_of_participant  varchar (80), Marks_got varchar(20), Maximium_marks varchar(100))")
                cur.execute("insert into quiz_name values(%s,%s)",(self.n_class_nm_var.get(),
                                                                    self.n_quiz_nm_var.get()))
                cur.execute("create table "+self.n_quiz_nm_var.get()+"_"+self.n_class_nm_var.get()+"qn (Question varchar(800),answer_status varchar(50),option1 varchar(200),option2 varchar(200),option3 varchar(200),option4 varchar(200), correct_option varchar (80),Short_Answer varchar (50))")
                cur.execute("create table "+self.n_quiz_nm_var.get()+"_"+self.n_class_nm_var.get()+"answer_chk (participant_ID varchar(50),question varchar(500),answer_given varchar(800),correction_status varchar(100))")                
                con.commit()
                con.close()
                messagebox.showinfo("Added!","Quiz " +self.n_quiz_nm_var.get()+" added successfully.")
                self.n_quiz_name_var.set("")
                self.n_class_nm_var.set("Select")
                self.no_of_qn_quiz_var.set("Select")
            except Exception as es:
                messagebox.showerror("Error!",es)
        else:
            messagebox.showinfo("Required!","All details are must.")
            
    def add_qn(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.admin_home()
        self.panel.destroy()
        self.add_qn_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.add_qn_frame.pack()
        self.qn_class_nm=Label(self.add_qn_frame,text=" Class ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.qn_class_nm.grid(row=0,column=0,pady=10,padx=20,sticky="W")        
        self.add_qn_Class=ttk.Combobox(self.add_qn_frame,width=30,height=10, textvariable=self.add_qn_class_var,font=("times new roman",24,"bold"),state="readonly")
        self.add_qn_Class['values']=("6","7","8","9","10","11","12","Python","Java","HtmlandCSS","QBasic","C","C_plus_plus","C_plus","C_sharp","Oracle","MySql","FoxPro","Other")
        self.add_qn_Class.grid(row=0,column=1,pady=5,padx=20,sticky="W")
        self.add_qn_Class.set("Select")
        self.add_qn_Class.bind("<<ComboboxSelected>>",self.add_qn2)
 
    def add_qn2(self,ev):
        if self.add_qn_class_var.get()!= "Select":
            self.qn_quiz_nm=Label(self.add_qn_frame,text=" Quiz Name ",bg="crimson",fg="White", font=("times new roman",24,"bold"))
            self.qn_quiz_nm.grid(row=1,column=0,pady=5,padx=20,sticky="w")
            con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
            cur=con.cursor()
            cur.execute("select name_of_quiz from quiz_name where Class= '"+self.add_qn_class_var.get()+"'")           
            rows=cur.fetchall()
            self.add_qn_quiz_nm=ttk.Combobox(self.add_qn_frame,width=30,height=19, textvariable=self.add_qn_quiz_var,font=("times new roman",24,"bold"),state="readonly")
            self.add_qn_quiz_nm.grid(row=1,column=1,padx=20,pady=10,sticky="W")
            self.add_qn_quiz_nm.set("Select")
            values=[]
            rows1=list(rows)           
            for i in range (0,len(rows1)):
                var=rows1[i]
                var1=str(var)
                b=(var1.replace("('",''))
                self.final=b.replace("',)","")               
                values.append(self.final)
            self.add_qn_quiz_nm['values']=values
            self.qn_lbl=Label(self.add_qn_frame,text=" Question ",bg="crimson",fg="White",anchor="w", font=("times new roman",30,"bold")).grid(row=2,column=0,padx=20,sticky="W")
            self.txt_qn=Text(self.add_qn_frame,width=70,height=4,font=("",14))
            self.txt_qn.grid(row=2,column=1,padx=20,pady=10,sticky="W")
            self.ans_typ=Label(self.add_qn_frame,text=" Answer Type ",bg="crimson",fg="White", font=("times new roman",30,"bold")).grid(row=3,column=0,padx=20,sticky="W")
            self.ans_typ_frame=Frame(self.add_qn_frame,height=100,bg="Grey",width=500,relief=RIDGE,bd=4)
            self.ans_typ_frame.grid(row=3,column=1,padx=20,pady=10,sticky="W")
            global ans_typ
            ans_typ=StringVar()
            mcq=Radiobutton(self.ans_typ_frame,value="mcq",text="MCQ",bg="grey",anchor="w",width=20,fg="White",command=self.ans_typ_func, variable=ans_typ,font=("times new roman",16,"bold")).grid(row=0,column=0,sticky="W")
            a_ans=Radiobutton(self.ans_typ_frame,value="s_ans",text="Short Answer",width=20,anchor="w",bg="grey",command=self.ans_typ_func, variable=ans_typ,fg="White", font=("times new roman",16,"bold")).grid(row=1,column=0,sticky="W")
            chk=Radiobutton(self.ans_typ_frame,value="chkbox",text="CheckBox",width=20,anchor="w",bg="grey",fg="White",command=self.ans_typ_func, variable=ans_typ, font=("times new roman",16,"bold")).grid(row=2,column=0,sticky="W")    
        else:
            messagebox.showerror("Select!","No Class Selected.")
   
    def ans_typ_func(self):
        global admin_add_qn_finall_btn
        if ans_typ.get() == "mcq":
            self.Short_Answer_Status_var="no"
            self.answer_type="mcq"
            self.mcq_status="yes"
            try:
                self.S_ans_lbl.destroy()
                mcq_option1_txt.set('Option 1')
                self.mcq_option2_txt.set('Option 2')
                self.mcq_option3_txt.set('Option 3')
                self.mcq_option4_txt.set('Option 4')
                self.mcq_lbl1=Label(self.add_qn_frame,text=" Options: ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
                self.mcq_lbl1.grid(row=4,column=0,sticky="W",padx=20)
                self.mcq_option_entry1=Entry(self.add_qn_frame,width=20,textvariable=mcq_option1_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry1.grid(row=4,padx=20,column=1,sticky="W")                
                self.mcq_option_entry2=Entry(self.add_qn_frame,width=20,textvariable=self.mcq_option2_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry2.grid(row=5,column=1,padx=20,sticky="W")                
                self.mcq_option_entry3=Entry(self.add_qn_frame,width=20,textvariable=self.mcq_option3_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry3.grid(row=6,column=1,padx=20,sticky="W")               
                self.mcq_option_entry4=Entry(self.add_qn_frame,width=20,textvariable=self.mcq_option4_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry4.grid(row=7,column=1,padx=20,sticky="W")
                self.mcq_lbl2=Label(self.add_qn_frame,text=" Correct Option ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
                self.mcq_lbl2.grid(row=8,column=0,sticky="W",padx=20)                
                self.mcq_correct_entry=ttk.Combobox(self.add_qn_frame,width=20,height=19, textvariable=self.mcq_correct_entry_var,font=("times new roman",22,"bold"),state="readonly")
                self.mcq_correct_entry['values']=("Option1","Option2","Option3","Option4")
                self.mcq_correct_entry.grid(row=8,column=1,padx=20,pady=10,sticky="W")                
                self.mcq_correct_entry.set("Select")
                admin_add_qn_finall_btn=Button(self.add_qn_frame,text="Add Question",width=10,command=self.Questions_added,height=1,padx=2,pady=1,font=("times new roman",20),bg="yellow",bd=5)
                admin_add_qn_finall_btn.grid(row=9,column=1,pady=5)
            except Exception as es:
                mcq_option1_txt.set('Option 1')
                self.mcq_option2_txt.set('Option 2')
                self.mcq_option3_txt.set('Option 3')
                self.mcq_option4_txt.set('Option 4')
                self.mcq_lbl1=Label(self.add_qn_frame,text=" Options: ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
                self.mcq_lbl1.grid(row=4,column=0,sticky="W",padx=20)
                self.mcq_option_entry1=Entry(self.add_qn_frame,width=20,textvariable=mcq_option1_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry1.grid(row=4,padx=20,column=1,sticky="W")                
                self.mcq_option_entry2=Entry(self.add_qn_frame,width=20,textvariable=self.mcq_option2_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry2.grid(row=5,column=1,padx=20,sticky="W")                
                self.mcq_option_entry3=Entry(self.add_qn_frame,width=20,textvariable=self.mcq_option3_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry3.grid(row=6,column=1,padx=20,sticky="W")                
                self.mcq_option_entry4=Entry(self.add_qn_frame,width=20,textvariable=self.mcq_option4_txt, font=("times new roman",20,"bold"),bd=5)
                self.mcq_option_entry4.grid(row=7,column=1,padx=20,sticky="W")
                self.mcq_lbl2=Label(self.add_qn_frame,text=" Correct Option ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
                self.mcq_lbl2.grid(row=8,column=0,sticky="W",padx=20)                
                self.mcq_correct_entry=ttk.Combobox(self.add_qn_frame,width=20,height=19, textvariable=self.mcq_correct_entry_var,font=("times new roman",22,"bold"),state="readonly")
                self.mcq_correct_entry['values']=("Option1","Option2","Option3","Option4")
                self.mcq_correct_entry.grid(row=8,column=1,padx=20,pady=10,sticky="W")
                self.mcq_correct_entry.set("Select")
                admin_add_qn_finall_btn=Button(self.add_qn_frame,text="Add Question",width=10,command=self.Questions_added,height=1,padx=2,pady=1,font=("times new roman",20),bg="yellow",bd=5)
                admin_add_qn_finall_btn.grid(row=9,column=1,pady=5)        
        elif ans_typ.get()=="s_ans":
            self.answer_type="s_ans"
            self.Short_Answer_Status_var="yes"
            self.mcq_status="yes"
            try:
                self.mcq_lbl1.destroy()
                self.mcq_option_entry1.destroy()
                self.mcq_option_entry2.destroy()
                self.mcq_option_entry3.destroy()
                self.mcq_option_entry4.destroy()
                self.mcq_lbl2.destroy()
                self.mcq_correct_entry.destroy()
                self.S_ans_lbl=Label(self.add_qn_frame,text=" Short answer selected. ",bg="light blue",fg="black", font=("times new roman",32,"underline"))
                self.S_ans_lbl.grid(row=4,column=1,padx=7)
                admin_add_qn_finall_btn=Button(self.add_qn_frame,text="Add Question",width=10,command=self.Questions_added,height=1,padx=2,pady=1,font=("times new roman",20),bg="yellow",bd=5)
                admin_add_qn_finall_btn.grid(row=9,column=1,pady=5)
            except Exception as es:
                self.S_ans_lbl=Label(self.add_qn_frame,text=" Short answer selected. ",bg="light blue",fg="black", font=("times new roman",32,"bold","underline"))
                self.S_ans_lbl.grid(row=4,column=1,padx=7)
                admin_add_qn_finall_btn=Button(self.add_qn_frame,text="Add Question",width=10,command=self.Questions_added,height=1,padx=2,pady=1,font=("times new roman",20),bg="yellow",bd=5)
                admin_add_qn_finall_btn.grid(row=9,column=1,pady=5)
        elif ans_typ.get()=="chkbox":
            messagebox.showinfo("Sorry!","Our this feature is currently not available.\nWe will try to bring it in future updates.")     

    def Questions_added(self):
        if self.answer_type=="mcq":
            if self.add_qn_quiz_var.get()=="Select" or self.txt_qn.get('1.0',END).lstrip()=="" or self.mcq_correct_entry_var.get()=="Select" or mcq_option1_txt.get().lstrip()==""  or self.mcq_option2_txt.get().lstrip()=="" or self.mcq_option3_txt.get().lstrip()=="" or self.mcq_option4_txt.get().lstrip()=="":
                messagebox.showinfo("Must!","All details are must.")
            else:
                try:
                    con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                    cur1=con.cursor()
                    cur1.execute("insert into "+ self.add_qn_quiz_var.get()+"_"+self.add_qn_class_var.get()+"qn (Question,answer_status,option1,option2,option3,option4,correct_option) values(%s,%s,%s,%s,%s,%s,%s)",(self.txt_qn.get('1.0',END),
                                                                    self.answer_type,
                                                                    mcq_option1_txt.get(),
                                                                    self.mcq_option2_txt.get(),
                                                                    self.mcq_option3_txt.get(),
                                                                    self.mcq_option4_txt.get(),
                                                                    self.mcq_correct_entry_var.get(),
                                                                     ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Added!","Question added successfully to quiz "+self.add_qn_quiz_var.get())
                    mcq_option1_txt.set('Option 1')
                    self.mcq_option2_txt.set('Option 2')
                    self.mcq_option3_txt.set('Option 3')
                    self.mcq_option4_txt.set('Option 4')
                    self.add_qn_quiz_var.set("Select")
                    self.txt_qn.delete("1.0",END)
                    self.mcq_correct_entry_var.set("Select")                    
                except Exception as es:
                    messagebox.showerror("Error!",es)       
        elif self.answer_type=="s_ans":
            if self.add_qn_quiz_var.get()!="Select" and self.txt_qn.get('1.0',END).lstrip()!="":
                try:
                    con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                    cur1=con.cursor()
                    cur1.execute("insert into "+ self.add_qn_quiz_var.get()+"_"+self.add_qn_class_var.get()+"qn (Question,answer_status) values(%s,%s)",(self.txt_qn.get('1.0',END),
                                                                    self.answer_type ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Added!","Question added successfully to quiz "+self.add_qn_quiz_var.get())
                    mcq_option1_txt.set('Option 1')
                    self.mcq_option2_txt.set('Option 2')
                    self.mcq_option3_txt.set('Option 3')
                    self.mcq_option4_txt.set('Option 4')
                    self.add_qn_quiz_var.set("Select")
                    self.txt_qn.delete("1.0",END)
                    self.mcq_correct_entry_var.set("Select")
                except Exception as es:
                    messagebox.showerror("Error!",es)
            else:
                messagebox.showinfo("Must!","All details are must.")       
#======================================================Add Question===========================================================================
    def add_participant(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.admin_home()
        self.panel.destroy()
        self.add_participant_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.add_participant_frame.pack()
        self.participnat_id_lbl=Label(self.add_participant_frame,text=" ID ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.participnat_id_lbl.grid(row=0,column=0,pady=10,padx=20,sticky="W")
        self.id_txt=Entry(self.add_participant_frame,width=30,textvariable=self.participant_id_var,state="readonly", font=("times new roman",30,"bold"),bd=5)
        self.id_txt.grid(row=0,column=1,pady=50,padx=20)
        self.participnat_name_lbl=Label(self.add_participant_frame,text=" Name ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.participnat_name_lbl.grid(row=1,column=0,pady=10,padx=20,sticky="W")
        self.name_txt=Entry(self.add_participant_frame,width=30,textvariable=self.participant_name_var, font=("times new roman",30,"bold"),bd=5)
        self.name_txt.grid(row=1,column=1,pady=50,padx=20)
        self.participnat_class_lbl=Label(self.add_participant_frame,text=" Class ",bg="crimson",fg="White", font=("times new roman",30,"bold"))
        self.participnat_class_lbl.grid(row=2,column=0,pady=10,padx=20,sticky="W")       
        self.add_part_Class=ttk.Combobox(self.add_participant_frame,width=30,height=10, textvariable=self.add_participant_class_var,font=("times new roman",24,"bold"),state="readonly")
        self.add_part_Class['values']=("6","7","8","9","10","11","12","Python","Java","HtmlandCSS","QBasic","C","C_plus_plus","C_plus","C_sharp","Oracle","MySql","FoxPro","Other")
        self.add_part_Class.grid(row=2,column=1,pady=5,padx=20,sticky="W")
        self.add_part_Class.set("Select")
        admin_part_finall_btn=Button(self.add_participant_frame,text="Add Participant",width=16,command=self.participant_added,height=1,padx=2,pady=1,font=("times new roman",20),bg="yellow",bd=5)
        admin_part_finall_btn.grid(row=9,column=1,pady=5)            
           
    def participant_added(self):
        if self.participant_name_var.get().lstrip()!="" and self.add_participant_class_var.get()!="Select":
            try:
                con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                cur1=con.cursor()
                cur1.execute("insert into participant_name (Name,Class) values(%s,%s)",(self.participant_name_var.get(),self.add_participant_class_var.get()))
                cur2=con.cursor()
                id = cur1.lastrowid
                self.participant_id_var.set(id)
                cur2.execute("create table "+self.participant_name_var.get()+"_"+self.add_participant_class_var.get()+"_"+str(id)+"participant (Quiz_played varchar(500),Marks_secured varchar (250), Maximum_Marks varchar(200),PRIMARY KEY (Quiz_played))")
                con.commit()
                con.close()
                x=str(id)
                messagebox.showinfo("Added!","Participant added successfully\n Participant Id is "+ x)
            except Exception as es:
                messagebox.showerror("Error!",es)
        else:
            messagebox.showinfo("Must","All details are must.") 
    
    def about_def(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.admin_home()
        self.panel.destroy()
        self.about_frame=Frame(self.root,relief=RIDGE,bd=6,bg="white")
        self.about_frame.pack()
        lbl1=Label(self.about_frame,text=" Developed By:                Aakarsh Kumar ",bg="purple",fg="White", font=("times new roman",24,"bold"))
        lbl1.grid(row=0,column=0,pady=2,padx=20,sticky="W")
        lbl2=Label(self.about_frame,text=" Launch Date:             05/09/2020               ",bg="purple",fg="White", font=("times new roman",24,"bold"))
        lbl2.grid(row=1,column=0,pady=2,padx=20,sticky="W")
        lbl3=Label(self.about_frame,text=" Version:                 1.0                                 ",bg="purple",fg="White", font=("times new roman",24,"bold"))
        lbl3.grid(row=2,column=0,pady=2,padx=20,sticky="W")
        lbl4=Label(self.about_frame,text=" MAIL ID:      aakarsh2504@gmail.com   ",bg="purple",fg="White", font=("times new roman",24,"bold"))
        lbl4.grid(row=3,column=0,pady=2,padx=20,sticky="W")
        lbl5=Label(self.about_frame,text=" Note:\n    1.Admin is  requested to make sure the smooth handle of the Application.\n    2.Admin should not click the selectd option of Answer Type, during the process of Add Question. \n    3.You cannot Add the quiz with the name that already exists in a particular class.\n    4.In Add Participant column the ID feild is ReadOnly feild.\n    5.A participant could not play a quiz more than once.\n    6.After the completion of the quiz the participant gets the number of correct MCQ's\n       and number of short answers that were there in the quiz, whose marks are not declared there.\n    7.The Admin could check the short answers afterwards and\n       the participant could see the final result in History option. ",bg="pink",fg="black", justify="left",font=("console",16))
        lbl5.grid(row=4,column=0,pady=10,padx=20,sticky="W")
        self.img1 = PhotoImage(file="capture.png")
        self.panel1 = Label(self.about_frame, image =self.img1,bd=0,highlightbackground="yellow")
        self.panel1.grid(row=5,column=0,pady=10)
    
    def participant_home_def(self):
        for widget in self.root.winfo_children():
            widget.destroy()         
        self.participant_home_frame=Frame(self.root,relief=RIDGE,bd=4,bg="Dark green")
        self.participant_home_frame.pack()
        self.participant_play_id=Label(self.participant_home_frame,text=" ID ",bg="purple",fg="light green", font=("times new roman",24,"bold"))
        self.participant_play_id.grid(row=0,column=0,padx=20,pady=20)
        self.participant_play_id_txt=Entry(self.participant_home_frame,width=20,textvariable=self.participant_play_id_var, font=("times new roman",30,"bold"),bd=5)
        self.participant_play_id_txt.grid(row=0,column=1,pady=50,padx=20)
        self.participant_play_select_quiz_btn=Button(self.participant_home_frame,text=" Select Quiz ",width=16,command=self.participant_play_select_quiz_def,height=1,padx=2,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
        self.participant_play_select_quiz_btn.grid(row=1,column=1,pady=5)
        self.participant_play_logout_btn=Button(self.root,text=" Logout ",width=10,command=self.m_frame_def,height=1,padx=2,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
        self.participant_play_logout_btn.pack(side="bottom")        
    
    def participant_play_select_quiz_def(self):
        if str(self.participant_play_id_var.get()).lstrip() != "" and self.participant_play_id_var.get() != 0:
            self.participant_play_id_var_int=str(self.participant_play_id_var.get())
            self.participant_play_quiz_lbl=Label(self.participant_home_frame,text=" Quiz ",bg="purple",fg="light green", font=("times new roman",24,"bold"))
            self.participant_play_quiz_lbl.grid(row=2,column=0,padx=20,pady=20)
            try:
                con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                cur=con.cursor()
                cur.execute("select Class from participant_name where ID="+self.participant_play_id_var_int) 
                self.participant_play_class_var=(cur.fetchall())
                self.participant_play_class_var_str=str(self.participant_play_class_var)
                self.replace1=self.participant_play_class_var_str.replace("[('","")
                self.replace2=self.replace1.replace("',)]","")                
                cur1=con.cursor()
                cur1.execute("select Name_of_quiz from quiz_name where Class='"+self.replace2+"'")
                self.participant_play_quiz_name=(cur1.fetchall())                
                if self.participant_play_quiz_name==[]:
                    messagebox.showerror("No Data!","No participant or Quiz found for ID "+self.participant_play_id_var_int)
                    self.participant_quiz_select_combo=ttk.Combobox(self.participant_home_frame,width=30,height=19, textvariable=self.participant_quiz_name_select_var,font=("times new roman",24,"bold"),state="readonly")
                    self.participant_quiz_select_combo.grid(row=2,column=1,padx=20,pady=10,sticky="W")
                    self.participant_quiz_select_combo.set("Select")                  
                    values=[]
                    rows1=list(self.participant_play_quiz_name)               
                    for i in range (0,len(rows1)):
                        var=rows1[i]
                        var1=str(var)                        
                        b=(var1.replace("('",""))
                        self.final=b.replace("',)","")                        
                        values.append(self.final)
                    self.participant_quiz_select_combo['values']=values
                else:
                    self.participant_quiz_select_combo=ttk.Combobox(self.participant_home_frame,width=30,height=19, textvariable=self.participant_quiz_name_select_var,font=("times new roman",24,"bold"),state="readonly")                   
                    self.participant_quiz_select_combo.grid(row=2,column=1,padx=20,pady=10,sticky="W")
                    self.participant_quiz_select_combo.set("Select")                    
                    values=[]
                    rows1=list(self.participant_play_quiz_name)                
                    for i in range (0,len(rows1)):
                        var=rows1[i]
                        var1=str(var)
                        b=(var1.replace("('",''))
                        self.final=b.replace("',)","")                       
                        values.append(self.final)
                    self.participant_quiz_select_combo['values']=values
                    self.participant_play_quiz_info_btn=Button(self.participant_home_frame,text=" Next ",width=16,height=1,padx=2,command=self.next_def,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                    self.participant_play_quiz_info_btn.grid(row=3,column=1,pady=5) 
                con.close()
            except Exception as es:
                messagebox.showerror("Error!",es)       
        else:
            messagebox.showinfo("Select!","Select the ID.")
    
    def next_def(self):
        if self.participant_quiz_name_select_var.get()!="Select":
            con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
            cur=con.cursor()
            cur.execute("select Name from participant_name where ID="+str(self.participant_play_id_var_int))           
            self.name_playing=str(cur.fetchall())
            self.name_playing=self.name_playing.replace("[('","")
            self.name_playing=self.name_playing.replace("',)]","")
            cur1=con.cursor()
            cur1.execute("select Quiz_played from "+self.name_playing+"_"+self.replace2+"_"+str(self.participant_play_id_var.get())+"participant")
            
            if self.participant_quiz_name_select_var.get() in  str(cur1.fetchall()):
                messagebox.showwarning("Played!","You have already played this quiz\nand cannot be replayed.")
            else:                
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.participant_home_frame1=Frame(self.root,relief=RIDGE,bd=4,bg="Dark green")
                self.participant_home_frame1.pack()  
                self.participant_lbl1=Label(self.participant_home_frame1,text="Read The Rules And\nClick Start Once You Are ready...\n\n\n1.Please don't use unnecessary signs and symbols in breif answers.\n2.Think before clicking the next button,\n  because you could not go back and your answer will be submited.\n3.M.C.Q results are instant after the test.\n4.Short answer result are not instant after the test,\n  you could check it in history once the admin  has checked it.\n5.If you face any problem or difficulty you could contact your host,\nand the host could contact the developer for the same.",bg="purple",fg="light green", font=("consolas",20,"bold"),justify="left")
                self.participant_lbl1.grid(row=0,column=0,padx=20,pady=20) 
                self.participant_play_logout_btn1=Button(self.root,text=" Logout ",width=10,command=self.m_frame_def,height=1,padx=2,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                self.participant_play_logout_btn1.pack(side="bottom")   
                self.next_def2()
            con.close()
        else:
            messagebox.showinfo("Must!","All details are must.")
        
    def next_def2(self):
        self.participant_play_quiz_start_btn=Button(self.participant_home_frame1,text=" Start ",width=16,height=1,padx=2,command=self.start_quiz,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5,cursor="hand2")
        self.participant_play_quiz_start_btn.grid(row=1,column=0,pady=10)
    
    def start_quiz(self):
        con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
        cur1=con.cursor()
        cur1.execute("select * from "+self.participant_quiz_name_select_var.get()+"_"+self.replace2+"qn")
        global mcq_status_fetch
        mcq_status_fetch=cur1.fetchall()
        self.participant_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="grey")
        self.participant_quiz_frame.pack()
        self.b=0
        self.running_loop1()       
        con.close()

    def running_def(self):
        self.participant_play_quiz_ans()
        running="yes"
        self.running_loop1()
     
    def running_loop(self):        
        a=""
        i=len(mcq_status_fetch)-1           
        global running
        running="yes"        
        while a != "none":
            while running=="yes":               
                self.fetch_per_question_details=mcq_status_fetch[self.b]
                if self.answer_type_of_qn=="mcq":
                    self.qs1_lbl1.config(text=self.fetch_per_question_details[0])
                    self.option1_radio.config(text=self.fetch_per_question_details[2])
                    self.option2_radio.config(text=self.fetch_per_question_details[3])
                    self.option3_radio.config(text=self.fetch_per_question_details[4])
                    self.option4_radio.config(text=self.fetch_per_question_details[5])                
                elif self.answer_type_of_qn=="s_ans":
                    self.qs1_lbl1.config(text=self.fetch_per_question_details[0])            
                running="no"
            a="none"
                    
    def running_loop1(self):
        a=""
        i=len(mcq_status_fetch)-1
        try:
            test=mcq_status_fetch[self.b]
            for widget in self.root.winfo_children():
                widget.destroy()
            global running
            running="yes"
            while a != "none":
                while running=="yes":                
                    self.fetch_per_question_details=mcq_status_fetch[self.b]
                    self.answer_type_of_qn=self.fetch_per_question_details[1]
                    if self.answer_type_of_qn == "mcq":
                        try:
                            self.participant_quiz_frame.destroy()
                            self.participant_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="grey")
                            self.participant_quiz_frame.pack()                 
                            self.qs1_lbl1=Label(self.participant_quiz_frame,text="",fg="dark blue", font=("arial",20),justify="left")
                            self.qs1_lbl1.grid(row=0,column=0,padx=20,pady=20)
                            self.option1_radio=Radiobutton(self.participant_quiz_frame,value="Option1",text="MCQ",anchor="w",width=20,fg="Black", variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option1_radio.grid(row=1,column=0,sticky="W")
                            self.option2_radio=Radiobutton(self.participant_quiz_frame,value="Option2",text="MCQ",anchor="w",width=20,fg="Black", variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option2_radio.grid(row=2,column=0,sticky="W")
                            self.option3_radio=Radiobutton(self.participant_quiz_frame,value="Option3",text="MCQ",anchor="w",width=20,fg="Black", variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option3_radio.grid(row=3,column=0,sticky="W")
                            self.option4_radio=Radiobutton(self.participant_quiz_frame,value="Option4",text="MCQ",anchor="w",width=20,fg="Black", variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option4_radio.grid(row=4,column=0,sticky="W")
                            self.participant_play_quiz_next_qn_btn=Button(self.participant_quiz_frame,text=" Next ",width=16,height=1,padx=2,command=self.running_def,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                            self.participant_play_quiz_next_qn_btn.grid(row=5,column=0,pady=5)
                            self.running_loop()                       
                        except:
                            self.participant_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="grey")
                            self.participant_quiz_frame.pack() 
                            self.qs1_lbl1=Label(self.participant_quiz_frame,text="",fg="dark blue", font=("arial",20),justify="left")
                            self.qs1_lbl1.grid(row=0,column=0,padx=20,pady=20)
                            self.option1_radio=Radiobutton(self.participant_quiz_frame,value="Option1",text="MCQ",anchor="w",width=20,fg="Black",command=self.participant_play_quiz_ans, variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option1_radio.grid(row=1,column=0,sticky="W")
                            self.option2_radio=Radiobutton(self.participant_quiz_frame,value="Option2",text="MCQ",anchor="w",width=20,fg="Black",command=self.participant_play_quiz_ans, variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option2_radio.grid(row=2,column=0,sticky="W")
                            self.option3_radio=Radiobutton(self.participant_quiz_frame,value="Option3",text="MCQ",anchor="w",width=20,fg="Black",command=self.participant_play_quiz_ans, variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option3_radio.grid(row=3,column=0,sticky="W")
                            self.option4_radio=Radiobutton(self.participant_quiz_frame,value="OPtion4",text="MCQ",anchor="w",width=20,fg="Black",command=self.participant_play_quiz_ans, variable=self.option1_ans,font=("times new roman",16,"bold"))
                            self.option4_radio.grid(row=4,column=0,sticky="W")
                            self.participant_play_quiz_next_qn_btn=Button(self.participant_quiz_frame,text=" Next ",width=16,height=1,padx=2,command=self.running_def,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                            self.participant_play_quiz_next_qn_btn.grid(row=5,column=0,pady=5)        
                            self.running_loop()
                    elif self.answer_type_of_qn=="s_ans":
                        try:
                            self.participant_quiz_frame.destroy()
                            self.participant_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="grey")
                            self.participant_quiz_frame.pack()
                            self.qs1_lbl1=Label(self.participant_quiz_frame,text="",fg="dark blue", font=("arial",20),justify="left")
                            self.qs1_lbl1.grid(row=0,column=0,padx=20,pady=20)                           
                            self.participant_play_quiz_s_ans=Text(self.participant_quiz_frame,width=50,height=15,font=("",16))
                            self.participant_play_quiz_s_ans.grid(row=1,column=0,padx=20,pady=10,sticky="W")
                            self.participant_play_quiz_next_qn_btn=Button(self.participant_quiz_frame,text=" Next ",width=16,height=1,padx=2,command=self.running_def,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                            self.participant_play_quiz_next_qn_btn.grid(row=5,column=0,pady=5)
                            self.running_loop()
                        except:
                            self.qs1_lbl1=Label(self.participant_quiz_frame,text="",fg="dark blue", font=("arial",20),justify="left")
                            self.qs1_lbl1.grid(row=0,column=0,padx=20,pady=20)
                            self.participant_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="grey")
                            self.participant_quiz_frame.pack()
                            self.participant_play_quiz_s_ans=Text(self.participant_quiz_frame,width=50,height=8,font=("",14))
                            self.participant_play_quiz_s_ans.grid(row=1,column=0,padx=20,pady=10,sticky="W")
                            self.participant_play_quiz_next_qn_btn=Button(self.participant_quiz_frame,text=" Next ",width=16,height=1,padx=2,command=self.running_def,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                            self.participant_play_quiz_next_qn_btn.grid(row=5,column=0,pady=5)
                            self.running_loop()
                    if self.b!=i:
                        self.b=self.b+1
                    else:
                        a="none"
                        if self.b==i:
                            self.participant_play_quiz_next_qn_btn.destroy()
                            self.participant_play_quiz_submit_qn_btn=Button(self.participant_quiz_frame,text=" Submit ",command=self.submit_def,width=16,height=1,padx=2,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
                            self.participant_play_quiz_submit_qn_btn.grid(row=5,column=0,pady=5)
                    running="no"               
                a="none"        
        except:
            messagebox.showerror("No Question","Admin has added no question to this quiz.")      
    def participant_play_quiz_ans(self):
        self.no_of_qn_count+=1
        if self.answer_type_of_qn=="mcq":       
            if self.option1_ans.get()!="":
                con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                cur1=con.cursor()
                cur1.execute("select correct_option from "+self.participant_quiz_name_select_var.get()+"_"+self.replace2+"qn where question='"+str(self.fetch_per_question_details[0])+"'") 
                x_str=str(cur1.fetchall())
                x=x_str.replace("[('","")
                y=x.replace("',)]","")
                con.close()               
                if self.option1_ans.get()==y:
                    messagebox.showinfo("Hurray!","You got it correct. ")
                    self.correct_ans_count=self.correct_ans_count+1                    
                else:
                   messagebox.showinfo("Wrong!","You got wrong.")
            else:
                pass
        elif self.answer_type_of_qn=="s_ans":  
            try:
                cona=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                cura=cona.cursor()
                cura.execute("insert into "+self.participant_quiz_name_select_var.get()+"_"+self.replace2+"answer_chk (participant_ID,question,answer_given,correction_status) values(%s,%s,%s,%s)",(self.participant_play_id_var_int,
                                                                                                                                                        self.fetch_per_question_details[0],
                                                                                                                                                        self.participant_play_quiz_s_ans.get("1.0",END),
                                                                                                                                                        "no"))
                cona.commit()
                cona.close()
                self.yet_to_be_calculated+=1
            except Exception as es:
                messagebox.showerror("Error!",es)
                
    def submit_def(self):
        self.participant_play_quiz_ans()
        for widget in self.root.winfo_children():
            widget.destroy()        
        self.participant_result_frame=Frame(self.root,relief=RIDGE,bd=4,bg="pink")
        self.participant_result_frame.pack()
        percent=(self.correct_ans_count/self.no_of_qn_count)*100
        if self.yet_to_be_calculated==0:
            if percent>=90:
                self.img1= PhotoImage(file="transparentGradHat.png")
                self.panel1 = Label(self.participant_result_frame, image =self.img1,bd=5,highlightbackground="yellow")
                self.panel1.grid(row=0,column=1)               
                participant_count_qn_lbl1=Label(self.participant_result_frame,text="You desereve it.",font=("calibri",24,"bold"),fg="black")
                participant_count_qn_lbl1.grid(row=1,column=1)
            elif percent>=70:
                self.img2= PhotoImage(file="great.png")
                self.panel2 = Label(self.participant_result_frame, image =self.img2,bd=5,highlightbackground="yellow")
                self.panel2.grid(row=0,column=1)
            elif percent>=40: 
                self.img3= PhotoImage(file="ok.png")
                self.panel3 = Label(self.participant_result_frame, image =self.img3,bd=5,highlightbackground="yellow")
                self.panel3.grid(row=0,column=1)
            else:   
                self.img4= PhotoImage(file="bad.png")
                self.panel4 = Label(self.participant_result_frame, image =self.img4,bd=5,highlightbackground="yellow")
                self.panel4.grid(row=0,column=1)
        else:
            self.img5= PhotoImage(file="doubt.png")
            self.panel5 = Label(self.participant_result_frame, image =self.img5,bd=2,highlightbackground="yellow")
            self.panel5.grid(row=0,column=1)
                  
        participant_count_qn_lbl=Label(self.participant_result_frame,text="No. of questions= "+str(self.no_of_qn_count),font=("calibri",30,"bold"),fg="black")
        participant_count_qn_lbl.grid(row=2,column=0,pady=3,padx=7)
        participant_correct_ans_lbl=Label(self.participant_result_frame,text="No. of correct answers= "+str(self.correct_ans_count),font=("calibri",30,"bold"),fg="black",bg="orange")
        participant_correct_ans_lbl.grid(row=2,column=1,pady=3,padx=7)
        participant_correct_ans_lbl=Label(self.participant_result_frame,text="No. of Short answers= "+str(self.yet_to_be_calculated),font=("calibri",30,"bold"),fg="black")
        participant_correct_ans_lbl.grid(row=2,column=2,pady=3,padx=7)
        self.participant_play_again_btn=Button(self.participant_result_frame,text=" Play Again ",width=10,command=self.participant_home_def,padx=2,pady=1,font=("times new roman",22,"bold"),bg="red",bd=5)
        self.participant_play_again_btn.grid(row=3,column=1,pady=2)
        self.participant_play_logout_btn=Button(self.participant_result_frame,text=" Logout ",width=10,command=self.m_frame_def,height=1,padx=2,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
        self.participant_play_logout_btn.grid(row=4,column=1,pady=2)               
        con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
        cur=con.cursor()
        cur.execute("select  Name from participant_name where ID="+self.participant_play_id_var_int) 
        name_fetch1=str(cur.fetchall()).replace("[('","")
        name_fetch2=name_fetch1.replace("',)]","")
        cur1=con.cursor()
        cur1.execute("insert into "+name_fetch2+"_"+self.replace2+"_"+str(self.participant_play_id_var.get())+"participant values(%s,%s,%s)",(self.participant_quiz_name_select_var.get(),
                                                                                                                                            self.correct_ans_count,
                                                                                                                                            self.no_of_qn_count))
        cur2=con.cursor()
        cur2.execute("insert into "+self.participant_quiz_name_select_var.get()+"_"+self.replace2+" values(%s,%s,%s,%s)",(str(self.participant_play_id_var.get()),name_fetch2,self.correct_ans_count,self.no_of_qn_count ))
        con.commit()
        con.close()
        self.correct_ans_count=0
        self.no_of_qn_count=0
        self.yet_to_be_calculated=0
        
    def chk_ans(self):
        for widget in self.root.winfo_children():
            widget.destroy()           
        self.admin_home()
        self.panel.destroy()
        self.chk_ans_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.chk_ans_frame.pack()
        self.chk_ans_id=Label(self.chk_ans_frame,text=" ID ",fg="White", bg="dark blue",font=("times new roman",20,"bold"))
        self.chk_ans_id.grid(row=0,column=0,pady=5,padx=20,sticky="w")
        self.txt_chk_id=Entry(self.chk_ans_frame,width=30,textvariable=self.chk_id_var, font=("times new roman",20,"bold"),bd=3)
        self.txt_chk_id.grid(row=0,column=1,pady=5,padx=20,sticky="w")
        self.chk_ans_select_quiz_btn=Button(self.chk_ans_frame,text=" Select Quiz ",width=16,command=self.chk_ans_select_quiz_def,height=1,padx=2,pady=1,font=("times new roman",20,"bold"),bg="yellow",bd=5)
        self.chk_ans_select_quiz_btn.grid(row=1,column=1,pady=5)       

    def chk_ans_select_quiz_def(self):    
            if str(self.chk_id_var.get()).lstrip() != "" and self.chk_id_var.get() != 0:
                self.chk_id_var_str=str(self.chk_id_var.get())
                try:
                    self.chk_ans_quiz_lbl.pack_forget()
                    con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                    cur=con.cursor()
                    cur.execute("select Class from participant_name where ID="+self.chk_id_var_str) 
                    self.chk_ans_class_var=(cur.fetchall())
                    self.chk_ans_class_var_str=str(self.chk_ans_class_var)
                    self.replace10=self.chk_ans_class_var_str.replace("[('","")
                    self.replace11=self.replace10.replace("',)]","")                   
                    cur1=con.cursor()
                    cur1.execute("select Name_of_quiz from quiz_name where Class='"+self.replace11+"'")
                    self.chk_quiz_name=(cur1.fetchall())                   
                    if self.chk_quiz_name==[]:
                        messagebox.showerror("No Data!","No participant or Quiz or Question found for ID "+self.chk_id_var_str)
                    else:
                        self.chk_ans_quiz_lbl=Label(self.chk_ans_frame,text=" Quiz ",fg="White",bg="dark blue", font=("times new roman",20,"bold"))
                        self.chk_ans_quiz_lbl.grid(row=2,column=0,pady=5,padx=20,sticky="w")
                        self.chk_quiz_select_combo=ttk.Combobox(self.chk_ans_frame,width=30,height=19, textvariable=self.chk_quiz_name_select_var,font=("times new roman",20,"bold"),state="readonly")                       
                        self.chk_quiz_select_combo.grid(row=2,column=1,padx=20,pady=5,sticky="W")
                        self.chk_quiz_select_combo.set("Select")
                        self.chk_qn_lbl=Label(self.chk_ans_frame,fg="dark blue", font=("arial",20),justify="left")                     
                        self.chk_qn_lbl.grid(row=3,column=1,padx=20,pady=20,sticky="w")
                        self.chk_ans_s_ans=Text(self.chk_ans_frame,width=50,height=12,font=("",16))
                        self.chk_ans_s_ans.grid(row=4,column=1,padx=10,pady=10)
                        values=[]
                        rows1=list(self.chk_quiz_name)                   
                        for i in range (0,len(rows1)):
                            var=rows1[i]
                            var1=str(var)                           
                            b=(var1.replace("('",""))
                            self.final1=b.replace("',)","")                          
                            values.append(self.final1)
                        self.chk_quiz_select_combo['values']=values
                        self.chk_quiz_select_combo.bind("<<ComboboxSelected>>",self.chk_ans_select_quiz_def1) 
                    con.close()
                except:
                    con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
                    cur=con.cursor()
                    cur.execute("select Class from participant_name where ID="+self.chk_id_var_str) 
                    self.chk_ans_class_var=(cur.fetchall())
                    self.chk_ans_class_var_str=str(self.chk_ans_class_var)
                    self.replace10=self.chk_ans_class_var_str.replace("[('","")
                    self.replace11=self.replace10.replace("',)]","")                   
                    cur1=con.cursor()
                    cur1.execute("select Name_of_quiz from quiz_name where Class='"+self.replace11+"'")
                    self.chk_quiz_name=(cur1.fetchall())                  
                    if self.chk_quiz_name==[]:
                        messagebox.showerror("No Data!","No participant or Quiz or Question found for ID "+self.chk_id_var_str)
                    else:
                        self.chk_ans_quiz_lbl=Label(self.chk_ans_frame,text=" Quiz ",fg="White",bg="dark blue", font=("times new roman",20,"bold"))
                        self.chk_ans_quiz_lbl.grid(row=2,column=0,pady=5,padx=20,sticky="w")
                        self.chk_quiz_select_combo=ttk.Combobox(self.chk_ans_frame,width=30,height=19, textvariable=self.chk_quiz_name_select_var,font=("times new roman",20,"bold"),state="readonly")           
                        self.chk_quiz_select_combo.grid(row=2,column=1,padx=20,pady=5,sticky="W")
                        self.chk_quiz_select_combo.set("Select")
                        self.chk_qn_lbl=Label(self.chk_ans_frame,text="",fg="dark blue", font=("arial",20),justify="left")                    
                        self.chk_qn_lbl.grid(row=3,column=1,padx=20,pady=20,sticky="w")
                        self.chk_ans_s_ans=Text(self.chk_ans_frame,width=50,height=12,font=("",16))
                        self.chk_ans_s_ans.grid(row=4,column=1,padx=10,pady=10)
                        values=[]
                        rows1=list(self.chk_quiz_name)                    
                        for i in range (0,len(rows1)):
                            var=rows1[i]
                            var1=str(var)                          
                            b=(var1.replace("('",""))
                            self.final1=b.replace("',)","")                          
                            values.append(self.final1)
                        self.chk_quiz_select_combo['values']=values
                        self.chk_quiz_select_combo.bind("<<ComboboxSelected>>",self.chk_ans_select_quiz_def1) 
                    con.close()
                finally :
                    pass    
            else:
                messagebox.showinfo("Required!","All details are must.")
    def chk_ans_select_quiz_def1(self,ev):
        try:
            con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
            cur=con.cursor()
            cur.execute("select question from "+self.chk_quiz_name_select_var.get()+"_"+self.replace11+"answer_chk where participant_ID='"+self.chk_id_var_str+"'"+" and correction_status='no'")
            self.question_chk=cur.fetchall()
            self.chk_ans_qn_count=0
            cur1=con.cursor()
            cur1.execute("select answer_given from "+self.chk_quiz_name_select_var.get()+"_"+self.replace11+"answer_chk where participant_ID='"+self.chk_id_var_str+"'"+" and correction_status='no'")
            self.chk_ans_count=0
            self.ans_chk=cur1.fetchall()
            con.close()            
            b=""
            j=len(self.question_chk)-1
            global running1
            running1="yes"
            while b!="none":
                while running1=="yes":
                    self.chk_qn_lbl.config(text="")
                    self.chk_ans_s_ans.config(state="normal")
                    self.chk_ans_s_ans.delete("1.0",END)
                    self.answer_ck_question=self.question_chk[self.chk_ans_qn_count]
                    self.answer_ck_question=str(self.answer_ck_question).replace("('","")
                    self.answer_ck_question=str(self.answer_ck_question).replace("',)","")
                    self.answer_ck_question=str(self.answer_ck_question).replace("\\n","\n")
                    self.chk_qn_lbl.config(text=str(self.answer_ck_question))                    
                    self.answer_chk=str(self.ans_chk[self.chk_ans_qn_count]).replace("('","")
                    self.answer_chk=self.answer_chk.replace("\\n","\n")
                    self.answer_chk=self.answer_chk.replace("',)","")                   
                    self.chk_ans_s_ans.insert(END,self.answer_chk)
                    self.chk_ans_s_ans.config(state="disabled")                    
                    self.chk_ans_qn_count+=1
                    self.chk_correct_btn=Button(self.chk_ans_frame,text="Correct",command=self.chk_correct_def,padx=2,font=("times new roman",20,"bold"),bg="light green",bd=3)
                    self.chk_correct_btn.grid(row=3,column=0)
                    self.chk_wrong_btn=Button(self.chk_ans_frame,text="Wrong",command=self.chk_wrong_def,padx=2,font=("times new roman",20,"bold"),bg="red",bd=3)
                    self.chk_wrong_btn.grid(row=4,column=0)
                    running1="no"
                b="none"
        except :
            messagebox.showinfo("Great","You have corrected all the answers of this participant or\nno question for this quiz.")

    def chk_correct_def(self):
        con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
        cur=con.cursor()
        cur.execute("update "+self.chk_quiz_name_select_var.get()+"_"+self.replace11+"answer_chk  set correction_status='yes' where participant_ID="+self.chk_id_var.get()+" and question='"+self.answer_ck_question+"' and answer_given='"+self.answer_chk+"'")
        cur1=con.cursor()
        cur1.execute("select Name from participant_name where ID="+self.chk_id_var_str)
        self.Nm_of_chk_ans=str(cur1.fetchall()).replace("[('","")
        self.Nm_of_chk_ans=self.Nm_of_chk_ans.replace("',)]","")
        cur2=con.cursor()
        cur2.execute("select Marks_secured from "+self.Nm_of_chk_ans+"_"+self.replace11+"_"+self.chk_id_var_str+"participant where Quiz_played='"+self.chk_quiz_name_select_var.get()+"'")
        self.marks_secured=str(cur2.fetchall()).replace("[('","")
        self.marks_secured=int(self.marks_secured.replace("',)]",""))
        cur3=con.cursor()
        cur3.execute("update "+self.Nm_of_chk_ans+"_"+self.replace11+"_"+self.chk_id_var_str+"participant set Marks_secured="+str(self.marks_secured+1)+" where Quiz_played='"+self.chk_quiz_name_select_var.get()+"'")        
        cur4=con.cursor()
        cur4.execute("update "+self.chk_quiz_name_select_var.get()+"_"+self.replace11+" set Marks_got="+str(self.marks_secured+1)+" where participant_id='"+self.chk_id_var_str+"'")       
        con.commit()
        con.close()
        self.chk_ans_select_quiz_def1(ev=0)
    
    def chk_wrong_def(self):
        con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
        cur=con.cursor()
        cur.execute("update "+self.chk_quiz_name_select_var.get()+"_"+self.replace11+"answer_chk  set correction_status='yes' where participant_ID="+self.chk_id_var.get()+" and question='"+self.answer_ck_question+"' and answer_given='"+self.answer_chk+"'")
        con.commit()
        con.close()
        self.chk_ans_select_quiz_def1(ev=0)  

    def chk_his_def(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.admin_home()
        self.panel.destroy()
        self.chk_his_frame=Frame(self.root,relief=RIDGE,bd=4,bg="grey")
        self.chk_his_frame.pack()
        self.chk_his_lbl=Label(self.chk_his_frame,text=" Serach By ",fg="pink", bg="dark blue",font=("times new roman",20,"bold"))
        self.chk_his_lbl.grid(row=0,column=0,pady=5,padx=20,sticky="e")
        self.by_quiz_btn=Button(self.chk_his_frame,text="Participant",padx=2,command=self.search_by_part,font=("times new roman",20,"bold"),bg="yellow",bd=3)
        self.by_quiz_btn.grid(row=0,column=1,padx=10)
        self.by_quiz_btn=Button(self.chk_his_frame,text="Quiz",padx=2,font=("times new roman",20,"bold"),command=self.search_by_quiz,bg="yellow",bd=3)
        self.by_quiz_btn.grid(row=0,column=2,padx=10)
    
    def search_by_quiz(self):
        self.chk_his_def()
        self.by_quiz_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.by_quiz_frame.pack()
        self.by_quiz_class_nm=Label(self.by_quiz_frame,text=" Class ",bg="crimson",fg="White", font=("times new roman",16,"bold"))
        self.by_quiz_class_nm.grid(row=0,column=0,pady=10,padx=20,sticky="W")      
        self.by_quiz_Class=ttk.Combobox(self.by_quiz_frame,width=30,height=10, textvariable=self.by_quiz_class_var,font=("times new roman",16,"bold"),state="readonly")
        self.by_quiz_Class['values']=("6","7","8","9","10","11","12","Python","Java","HtmlandCSS","QBasic","C","C_plus_plus","C_plus","C_sharp","Oracle","MySql","FoxPro","Other")
        self.by_quiz_Class.grid(row=0,column=1,pady=5,padx=20,sticky="W")
        self.by_quiz_Class.set("Select")
        self.by_quiz_Class.bind("<<ComboboxSelected>>",self.seacrh_by_quiz2)
    
    def seacrh_by_quiz2(self,ev):       
        if self.add_qn_class_var.get()!= "Select":
            self.by_quiz_quiz_nm=Label(self.by_quiz_frame,text=" Quiz Name ",bg="crimson",fg="White", font=("times new roman",16,"bold"))
            self.by_quiz_quiz_nm.grid(row=1,column=0,pady=5,padx=20,sticky="w")
            con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
            cur=con.cursor()
            cur.execute("select name_of_quiz from quiz_name where Class= '"+self.by_quiz_class_var.get()+"'")           
            rows=cur.fetchall()        
            self.by_quiz_quiz=ttk.Combobox(self.by_quiz_frame,width=30,height=19, textvariable=self.by_quiz_quiz_var,font=("times new roman",16,"bold"),state="readonly")
            self.by_quiz_quiz.grid(row=1,column=1,padx=20,pady=10,sticky="W")
            self.by_quiz_quiz.set("Select")
            values=[]
            rows1=list(rows)          
            for i in range (0,len(rows1)):
                var=rows1[i]
                var1=str(var)
                b=(var1.replace("('",''))
                self.final5=b.replace("',)","")                
                values.append(self.final5)
            self.by_quiz_quiz['values']=values
            self.by_quiz_quiz.bind("<<ComboboxSelected>>",self.search_by_quiz3)
    def search_by_quiz3(self,ev):        
        con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
        cur=con.cursor()
        cur.execute("select * from "+self.by_quiz_quiz_var.get()+"_"+self.by_quiz_class_var.get())
        data=(cur.fetchall())
        if data==[]:
            messagebox.showinfo("No Data!","No participant played this quiz.")
            con.close()
        else:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.admin_home()
            self.panel.destroy()
            self.chk_his_def()
            self.search_by_quiz()
            self.seacrh_by_quiz2(ev=0)
            #self.search_by_quiz3(ev=0)
            self.Table_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
            self.Table_Frame1.pack()                
            scroll_x=Scrollbar(self.Table_Frame1,orient=HORIZONTAL)
            scroll_y=Scrollbar(self.Table_Frame1,orient=VERTICAL)
            self.Student_table1=ttk.Treeview(self.Table_Frame1,column=("Participant ID","Name Of Participants","Marks Secured","Maximum Marks"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Student_table1.xview)
            scroll_y.config(command=self.Student_table1.yview)              
            self.Student_table1.column("#0",width=0,stretch=NO)
            self.Student_table1.column("Participant ID",width=150,minwidth=150,anchor=W)
            self.Student_table1.column("Name Of Participants",width=250,minwidth=250,anchor=W)
            self.Student_table1.column("Marks Secured",width=150,minwidth=150,anchor=CENTER)
            self.Student_table1.column("Maximum Marks",width=150,minwidth=150,anchor=CENTER)
            self.Student_table1.heading("Participant ID",text="Participant ID")
            self.Student_table1.heading("Name Of Participants",text="Name Of Participants")
            self.Student_table1.heading("Marks Secured",text="Marks Secured")
            self.Student_table1.heading("Maximum Marks",text="Maximum Marks")
            self.Student_table1.pack()
            con.close()
            count=0              
            for data_i in data:
                data_i=list(data_i)            
                self.Student_table1.insert(parent='',index='end',iid=count,text="",values=(data_i[0],data_i[1],data_i[2],data_i[3]))
                count+=1
            self.Student_table1.pack()              
            
    def search_by_part(self):
        self.chk_his_def()
        self.by_part_frame=Frame(self.root,relief=RIDGE,bd=4,bg="dark blue")
        self.by_part_frame.pack()
        self.by_part_id_lbl=Label(self.by_part_frame,text=" ID ",bg="crimson",fg="White", font=("times new roman",18,"bold"))
        self.by_part_id_lbl.grid(row=0,column=0,pady=5,padx=5,sticky="w")
        self.txt_by_part_id=Entry(self.by_part_frame,width=30,textvariable=self.by_part_id_var, font=("times new roman",18,"bold"),bd=5)
        self.txt_by_part_id.grid(row=0,column=1,pady=5,padx=5)
        self.by_quiz_chk_btn=Button(self.by_part_frame,text="Check",padx=2,font=("times new roman",20,"bold"),command=self.chk_by_part_def,bg="light green",bd=3)
        self.by_quiz_chk_btn.grid(row=1,column=1,padx=0,pady=7)
    
    def chk_by_part_def(self):
        self.search_by_part()
        if self.by_part_id_var.get()!=0 and str(self.by_part_id_var.get()).lstrip()!="":
            con=mysql.connector.connect(host="localhost",user="root",port=self.sql_port_no.get(),password=self.sql_password_no.get(),database="quiz",charset="utf8")
            cur=con.cursor()
            cur.execute("select * from participant_name where ID="+self.by_part_id_var.get())
            self.by_part_dt=(cur.fetchall())
            if self.by_part_dt==[]:
                messagebox.showinfo("No Data!","No participant for this ID.")
                con.close()
            else:
                Table_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
                Table_Frame.pack()              
                scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
                scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
                self.Student_table=ttk.Treeview(Table_Frame,column=("Quiz Name","Marks Secured","Maximum Marks"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.Student_table.xview)
                scroll_y.config(command=self.Student_table.yview)              
                self.Student_table.column("#0",width=0,stretch=NO)
                self.Student_table.column("Quiz Name",width=250,minwidth=250,anchor=W)
                self.Student_table.column("Marks Secured",width=150,minwidth=150,anchor=W)
                self.Student_table.column("Maximum Marks",width=150,minwidth=150,anchor=CENTER)              
                self.Student_table.heading("Quiz Name",text="Quiz Name")
                self.Student_table.heading("Marks Secured",text="Marks Secured")
                self.Student_table.heading("Maximum Marks",text="Maximum Marks")          
                self.by_part_dt=list(self.by_part_dt[0]) 
                self.by_part_id=self.by_part_dt[0]  
                self.by_part_nm=self.by_part_dt[1]        
                self.by_part_class=self.by_part_dt[2]
                cur1=con.cursor()
                cur1.execute("select * from "+self.by_part_nm+"_"+self.by_part_class+"_"+str(self.by_part_id)+"participant")
                data=cur1.fetchall()                
                con.close()
                count=0               
                for data_i in data:
                    data_i=list(data_i)            
                    self.Student_table.insert(parent='',index='end',iid=count,text="",values=(data_i[0],data_i[1],data_i[2]))
                    count+=1
                self.Student_table.pack()
        else:
            messagebox.showinfo("Must","All details are must.")  
#==============Bottom_Main Area============
root=Tk()
ob=quiz(root)
root.mainloop()
