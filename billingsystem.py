from tkinter import *
import math
import random,os
from tkinter import messagebox
class bill_app:
     def __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("billing software")
            self.root.resizable(False,False)
            bg_color="#074463"
            title=Label(self.root,text="billing software",bd=7,relief=GROOVE,bg=bg_color,fg="gold",font=("time new roman",25,"bold"),pady=1).pack(fill="x")
#===========varables===============================================================================================================================================

#==========cosmetics================================================================================================================================================
            self.soap=IntVar()
            self.face_wash=IntVar()
            self.face_cream=IntVar()
            self.hairoil=IntVar()
            self.loshan=IntVar()

#==========grocery===================================================================================================================================================
            self.rice=IntVar()
            self.wheat=IntVar()
            self.dal=IntVar()
            self.sweet_oil=IntVar()
            self.sugar=IntVar()


#===========cold drink====================================================================================================================================
            self.thumbup=IntVar()
            self.mazza=IntVar()
            self.fruit=IntVar()
            self.jira=IntVar()
            self.rescna=IntVar()

#==============price============================================================================================================
            self.cosmetics_price=StringVar()
            self.Grocery_price=StringVar()
            self.cold_drink_Tax=StringVar()


#============Tax=======================================================================================================
            self.cosmetics_Tax=StringVar()
            self.Grocery_Tax=StringVar()
            self.cold_drink=StringVar()


#=============CUSTOMER======================================================================================
            
            self.c_name=StringVar()
            self.c_phone=StringVar()
            
            self.c_billno=StringVar()
            x=random.randint(1000,9999)
            self.c_billno.set(str(x))
            self.c_searchbill=StringVar()
#==============================customer=================================================================================================================================
            F1=LabelFrame(self.root,text="Customer Details",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
            F1.place(x=0,y=48,relwidth=1)


            cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("time new roman",15,"bold")).grid(row=0,column=0,pady=2)
            cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=3,padx=7)

            cphone_lbl=Label(F1,text="phone No:",bg=bg_color,fg="white",font=("time new roman",15,"bold")).grid(row=0,column=2,pady=2)
            cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=7)

            cbill_lbl=Label(F1,text="bill No:",bg=bg_color,fg="white",font=("time new roman",15,"bold")).grid(row=0,column=4,pady=2)
            cbill_txt=Entry(F1,width=15,font="arial",textvariable=self.c_billno,bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=7)

            bill_btn=Button(F1,text="Search",command=self.find_bill,width=7,bd=3,font="arial 12 bold").grid(row=0,column=6)
#======================cosmatics Frame===============================================================================================================================
            F2=LabelFrame(self.root,fg="gold",bd=8,relief=GROOVE,text="Cosmetics",font=("time new roman",15,"bold"),bg=bg_color)
            F2.place(x=2,y=126,width=300,height=300)

            Bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            facewash_lbl=Label(F2,text="facewash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            facewash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=7)

            Cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            Cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=7)

            hairoil_lbl=Label(F2,text="hair oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            hairoil_txt=Entry(F2,textvariable=self.hairoil,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=7)

            bodyloshan_lbl=Label(F2,text="bodyloshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            bodyloshan_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=7)
#============================grocery======================================================================================================================================
            F3=LabelFrame(self.root,bd=8,fg="gold",relief=GROOVE,text="Grocery",font=("time new roman",15,"bold"),bg=bg_color)
            F3.place(x=290,y=126,width=270,height=300)

            Rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            Rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=7)

            daal_lbl=Label(F3,text="Dal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            daal_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=7)

            oil_lbl=Label(F3,text="sweet Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            oil_txt=Entry(F3,width=10,textvariable=self.sweet_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=7)

            sugar_lbl=Label(F3,text="sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=7)

#=========================cold drink=================================================================================================================================

            F4=LabelFrame(self.root,bd=8,fg="gold",relief=GROOVE,text="Cold Drink",font=("time new roman",15,"bold"),bg=bg_color)
            F4.place(x=560,y=126,width=280,height=300)

            Thumbup_lbl=Label(F4,text="Thumb up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            Thumbup_txt=Entry(F4,width=10,textvariable=self.thumbup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            Mazza_lbl=Label(F4,text="Mazza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            Mazza_txt=Entry(F4,width=10,textvariable=self.mazza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=7)

            fruitbeer_lbl=Label(F4,text="Fruit Beer",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            fruitbeer_txt=Entry(F4,width=10,textvariable=self.fruit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=7)

            Jira_lbl=Label(F4,text="Jira Masala",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            Jira_txt=Entry(F4,width=10,textvariable=self.jira,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=7)

            Rescna_lbl=Label(F4,text="Rescna",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            Rescna_txt=Entry(F4,width=10,textvariable=self.rescna,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=7)

#============bill Area===================================================================================================================================
            F5=Frame(self.root,bd=10,relief=GROOVE)
            F5.place(x=840,y=126,width=250,height=300)
            bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
            scrol_y=Scrollbar(F5,orient=VERTICAL)
            self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack()
#=================Button Frame========================================================================================================================
            F6=LabelFrame(self.root,bd=5,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
            F6.place(x=0,y=420,relwidth=1,height=134)

            m1=Label(F6,text="total cosmetics Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,pady=1,padx=8,sticky="w")
            m1_txt=Entry(F6,width=14,textvariable=self.cosmetics_price,font="arial 12 bold",bd=6,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=1)

            m2=Label(F6,text="total grocery Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,pady=1,padx=8,sticky="w")
            m2_txt=Entry(F6,width=14,textvariable=self.Grocery_price,font="arial 12 bold",bd=6,relief=SUNKEN).grid(row=1,column=1,padx=1,pady=1)

            m3=Label(F6,text="total cold drink Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,pady=1,padx=8,sticky="w")
            m3_txt=Entry(F6,width=14,textvariable=self.cold_drink,font="arial 12 bold",bd=6,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=1)

            m4=Label(F6,text="cosmetics Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=2,pady=1,padx=8,sticky="w")
            m4_txt=Entry(F6,width=14,textvariable=self.cosmetics_Tax,font="arial 12 bold",bd=6,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=1)

            m5=Label(F6,text="grocery Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=2,pady=1,padx=8,sticky="w")
            m5_txt=Entry(F6,width=14,textvariable=self.Grocery_Tax,font="arial 12 bold",bd=6,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=1)

            m5=Label(F6,text="cold drink Tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=2,pady=1,padx=8,sticky="w")
            m5_txt=Entry(F6,width=14,textvariable=self.cold_drink_Tax,font="arial 12 bold",bd=6,relief=SUNKEN).grid(row=2,column=3,padx=5,pady=1)
#======button=========================================================================================================================================            
            btn_F=Frame(F6,bd=6,relief=GROOVE)
            btn_F.place(x=635,width=448,height=105)

            Total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=12,bd=2,width=10,font="arial 11 bold").grid(row=0,column=0,padx=5,pady=5)
            Genaratebill_btn=Button(btn_F,text="GenarateBill",command=self.bill_area,bg="cadetblue",bd=2,fg="white",pady=12,width=10,font="arial 11 bold").grid(row=0,column=1,padx=5,pady=5)
            clear_btn=Button(btn_F,text="clear",bg="cadetblue",command=self.clear_data,fg="white",pady=12,bd=2,width=10,font="arial 11 bold").grid(row=0,column=2,padx=5,pady=5)
            exit_btn=Button(btn_F,text="exit",bg="cadetblue",fg="white",command=self.exit_system,pady=12,bd=2,width=10,font="arial 11 bold").grid(row=0,column=3,padx=5,pady=5)
            self.Welcome_bill()


           # self.soap=IntVar()
            #self.face_wash=IntVar()
            #self.face_cream=IntVar()
            #self.oil=IntVar()
            #self.loshan=IntVar()

     def  total(self):
           self.c_s=self.soap.get()*40
           self.c_fw=self.face_wash.get()*42
           self.c_fc=self.face_cream.get()*60
           self.c_h=self.hairoil.get()*70
           self.c_l=self.loshan.get()*50
           self.total_cosmetic_price=float(
                                                           self.c_s+
                                                           self.c_fw+
                                                           self.c_fc+
                                                           self.c_h+
                                                           self.c_l
                                                             )
           self.cosmetics_price.set("Rs. "+str(self.total_cosmetic_price))
           self.c_Tax=round((self.total_cosmetic_price*0.05),2)
           self.cosmetics_Tax.set("Rs. "+str(self.c_Tax))

#========================grocery====================================
           self.r=self.rice.get()*40
           self.w=self.wheat.get()*17
           self.d=self.dal.get()*17
           self.sw=self.sweet_oil.get()*47
           self.su=self.sugar.get()*49
           
           self.total_grocery_price=float(
                                                            self.r+
                                                           self.w+
                                                           self.d+
                                                           self.sw+
                                                           self.su
                                                           )
           self.Grocery_price.set("Rs. "+str(self.total_grocery_price))
           self.G_Tax=round((self.total_grocery_price*0.07),2)
           self.Grocery_Tax.set("Rs. "+str(self.G_Tax))
#=============cold drink======================
           self.T=self.thumbup.get()*25
           self.MZ=self.mazza.get()*42
           self.FR=self.fruit.get()*15
           self.JI=self.jira.get()*10
           self.RE=self.rescna.get()*15
           self.drink_cold=float(
                                           self.T+
                                           self.MZ+
                                           self.FR+
                                           self.JI+
                                           self.RE
                                           )
           self.cold_drink.set("Rs. "+str(self.drink_cold))
           self.D_Tax=D_Tax=round((self.drink_cold*0.03),2)
           self.cold_drink_Tax.set("Rs. "+str(self.D_Tax))


           self.Total_bill=float(
                                                    self.total_cosmetic_price+
                                                    self.total_grocery_price+
                                                    self.drink_cold+
                                                    self.c_Tax+
                                                    self.G_Tax+
                                                    self.D_Tax
                                           )
#==========billarea============================================

     def  Welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\nWelcome Webcode Retail")
            self.txtarea.insert(END,f"\nBill Number   :{self.c_billno.get()}")
            self.txtarea.insert(END,f"\nCustomer Name :{self.c_name.get()}")
            self.txtarea.insert(END,f"\nPhone Number  :{self.c_phone.get()}")
            self.txtarea.insert(END,f"\n==========================")
            self.txtarea.insert(END,f"\nProducts\t    QTY\t    Price")
            self.txtarea.insert(END,f"\n==========================")
     def  bill_area(self):
             if self.c_name.get()=="" or self.c_phone.get()=="":
                  messagebox.showerror("Error","Customer detail are important")
             elif   self.cosmetics_price.get()=="Rs. 0.0" and self.Grocery_price.get()=="Rs. 0.0" and self.cold_drink.get()=="Rs. 0.0":
                       messagebox.showerror("Error","No Product puchased")

                  
             else:
                  self.Welcome_bill()
             #===cosmatics=====
                  if self.soap.get()!=0:
                       self.txtarea.insert(END,f"\nBath Soap\t    {self.soap.get()}\t     {self.c_s}")
                  if self.face_wash.get()!=0:
                       self.txtarea.insert(END,f"\nFace Wash\t    {self.face_wash.get()}\t     {self.c_fw}")
                  if self.face_cream.get()!=0:
                       self.txtarea.insert(END,f"\nFace Cream\t   {self.face_cream.get()}\t     {self.c_fc}")
                  if self.hairoil.get()!=0:
                       self.txtarea.insert(END,f"\nHair oil\t     {self.hairoil.get()}\t     {self.c_h}")
                  if self.loshan.get()!=0:
                       self.txtarea.insert(END,f"\nBody loshan\t  {self.loshan.get()}\t     {self.c_l}")
                       
                 #====grocery=======================================================

                  if self.rice.get()!=0:
                       self.txtarea.insert(END,f"\nRice\t      {self.rice.get()}\t     {self.r}")
                  if self.wheat.get()!=0:
                       self.txtarea.insert(END,f"\nWheat\t      {self.wheat.get()}\t     {self.w}")
                  if self.dal.get()!=0:
                       self.txtarea.insert(END,f"\ndaal\t      {self.dal.get()}\t     {self.d}")
                  if self.sweet_oil.get()!=0:
                       self.txtarea.insert(END,f"\nSweet oil\t    {self.sweet_oil.get()}\t     {self.sw}")
                  if self.sugar.get()!=0:
                       self.txtarea.insert(END,f"\nSugar\t      {self.sugar.get()}\t     {self.su}")

                    #===cold drink========================================
                  if self.thumbup.get()!=0:
                       self.txtarea.insert(END,f"\nThumbup\t      {self.thumbup.get()}\t     {self.T}")
                  if self.mazza.get()!=0:
                       self.txtarea.insert(END,f"\nMazza\t      {self.mazza.get()}\t     {self.MZ}")
                  if self.fruit.get()!=0:
                       self.txtarea.insert(END,f"\nfruiti\t      {self.fruit.get()}\t     {self.FR}")
                  if self.jira.get()!=0:
                       self.txtarea.insert(END,f"\nJira masala\t  {self.jira.get()}\t     {self.JI}")
                  if self.rescna.get()!=0:
                       self.txtarea.insert(END,f"\nRescna\t      {self.rescna.get()}\t     {self.RE}")

                   
                  self.txtarea.insert(END,f"\n==========================")
                  if self.cosmetics_Tax.get()!="Rs. 0.0":
                            self.txtarea.insert(END,f"\nCosmetic Tax\t\t{self.cosmetics_Tax.get()}")

                  if self.Grocery_Tax.get()!="Rs. 0.0":
                            self.txtarea.insert(END,f"\nGrocery Tax\t\t{self.Grocery_Tax.get()}")

                  if self.cold_drink.get()!="Rs. 0.0":
                            self.txtarea.insert(END,f"\nCold drink Tax\t\t{self.cold_drink.get()}")


                  self.txtarea.insert(END,f"\n\n==========================")
                  self.txtarea.insert(END,f"\nTotal Bill :\t   Rs. {self.Total_bill}")
                  self.txtarea.insert(END,f"\n==========================")
                  self.save_bill()
     def save_bill(self):
              op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
              if op>0:
                   self.bill_data=self.txtarea.get("1.0",END)
                   F1=open("bills/"+str(self.c_billno.get())+".txt","w")
                   F1.write(self.bill_data)
                   F1.close()
                   messagebox.showinfo("saved",f"bill no. : {self.c_billno.get()} saved successfully")
              else:
                   return
     def find_bill(self):
            present="no"
            for i in os.listdir("bills/"):
                  if  i.split('.')[0]==self.c_billno.get():
                       F1=open(f"bills/{i}","r")
                       
                       self.txtarea.delete('1.0',END)
                       for d in F1:
                             self.txtarea.insert(END,d)
                       present="yes"
                       F1.close()
            if present=="no":   
                  messagebox.showerror("Error","invalid bill No.")

     def  clear_data(self):
             self.soap.set(0)
             self.face_wash.set(0)
             self.face_cream.set(0)
             self.hairoil.set(0)
             self.loshan.set(0)

     #==========grocery===================================================================================================================================================
             self.rice.set(0)
             self.wheat.set(0)
             self.dal.set(0)
             self.sweet_oil.set(0)
             self.sugar.set(0)


     #===========cold drink====================================================================================================================================
             self.thumbup.set(0)
             self.mazza.set(0)
             self.fruit.set(0)
             self.jira.set(0)
             self.rescna.set(0)

     #==============price============================================================================================================
             self.cosmetics_price.set(" ")
             self.Grocery_price.set(" ")
             self.cold_drink_Tax.set(" ")


     #============Tax=======================================================================================================
             self.cosmetics_Tax.set(" ")
             self.Grocery_Tax.set(" ")
             self.cold_drink.set(" ")


     #=============CUSTOMER======================================================================================
                 
             self.c_name.set(" ")
             self.c_phone.set(" ")
                 
             self.c_billno.set(" ")
             x=random.randint(1000,9999)
             self.c_billno.set(str(x))
             self.c_searchbill.set(" ")
             self.Welcome_bill()

     def exit_system(self):
            op=messagebox.askyesno("Exit","Do you really want exit")
            if op>0:
                   self.root.destroy()
      
                  
                    

#i.split(' . ')[0]==self.c_searchbill.get():
root=Tk()
obj=bill_app(root)
root.mainloop()     
