from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        # ========Variable===========
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        labeltitle=Label(self.root,bd=20,text="HOSPITAL MANAGEMENT SYSTEM",relief=RIDGE,fg="black",bg="white",font=("time new roman",50,"bold"))
        labeltitle.pack(side=TOP,fill=X)

        # ==============================Dataframe===================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

                            # =============Left Dataframe=============
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("time new roman",12,"bold"),text="Patient Informantion")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
                            # ============Right Dataframe=============
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("time new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        # ==============================Buttons Frame===================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=80)

        # ==============================Details Frame===================================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # ==============================DataframeLeft===================================
        labelNameTablet=Label(DataframeLeft,text="Names Of Tablets",font=("arial",12,"bold"),padx=2,pady=6)
        labelNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("arial",13,"bold"),width=33)
        comNametablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1,sticky=W)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refrence No:",padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,textvariable=self.ref,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=4)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,textvariable=self.NumberofTablets,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,textvariable=self.Issuedate,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,textvariable=self.sideEfect,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("arial",13,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,textvariable=self.DrivingUsingMachine,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,textvariable=self.StorageAdvice,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,textvariable=self.HowToUseMedication,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,textvariable=self.PatientId,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,textvariable=self.nhsNumber,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,textvariable=self.PatientName,font=("arial",13,"bold"),width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,textvariable=self.DateOfBirth,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,textvariable=self.PatientAddress,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)


        # =======================================Dataframe Right===================================================
        self.txtprescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

        # =========================================Buttons============================================================
        


        btnPrescription =Button(Buttonframe,command=self.iPrescription,text="Prescription", bg="green", fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData =Button(Buttonframe,text="Prescription Data", bg="green", fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6,command=self.prescriptionDate)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate =Button(Buttonframe,command=self.update_data,text="Update", bg="green", fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete =Button(Buttonframe,command=self.delete_fun,text="Delete", bg="green", fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear =Button(Buttonframe,command=self.clear,text="Clear", bg="green", fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit =Button(Buttonframe,command=self.Exit,text="Exit", bg="green", fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        # ==========================================Table====================================================
        # ========================================Scrollbar=============================================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftablet","ref","does","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address")
                                         ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference NO.")
        self.hospital_table.heading("does",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("does",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

 # ====================== Database Function ======================
    def prescriptionDate(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="mydata")
            my_cursor = conn.cursor()

            # Corrected SQL query
            sql_insert = "INSERT INTO hospital (name_of_tablets, reference_no, dose, numbers_of_tablets, lot, issue_date, exp_date, daily_dose, storage, nhs_number, patient_name, dob, patient_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            values = (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
            )

            my_cursor.execute(sql_insert, values)
            conn.commit()
            self.fatch_data()
            conn.close()

            messagebox.showinfo("Success", "Data inserted successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # ====================Update================================
    def update_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="mydata")
            my_cursor = conn.cursor()

            update_query = "UPDATE hospital SET name_of_tablets=%s, reference_no=%s, dose=%s, numbers_of_tablets=%s, lot=%s, issue_date=%s, exp_date=%s, daily_dose=%s, storage=%s, nhs_number=%s, patient_name=%s, dob=%s, patient_address=%s WHERE reference_no=%s"

            my_cursor.execute(update_query, (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()  # This should be at the end for the WHERE condition
                ))

            conn.commit()  # Save changes
            messagebox.showinfo("Success", "Data updated successfully!")
            self.fatch_data()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error updating data: {err}")

        finally:
            my_cursor.close()
            conn.close()  # Close connection
        




        #  ===============Fatch Data====================
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # ================select entry data values show data at frame left section======================    

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    #===========================Prescription======================
    def iPrescription(self):
        self.txtprescription.insert(END, "Name of Tablets:\t\t" + self.Nameoftablets.get() + "\n")
        self.txtprescription.insert(END, "Reference No:\t\t" + self.ref.get() + "\n")
        self.txtprescription.insert(END, "Dose:\t\t" + self.Dose.get() + "\n")
        self.txtprescription.insert(END, "Number Of Tablets:\t\t" + self.NumberofTablets.get() + "\n")
        self.txtprescription.insert(END, "Lot:\t\t" + self.Lot.get() + "\n")
        self.txtprescription.insert(END, "Issue Date:\t\t" + self.Issuedate.get() + "\n")
        self.txtprescription.insert(END, "Exp Date:\t\t" + self.ExpDate.get() + "\n")
        self.txtprescription.insert(END, "Daily Dose:\t\t" + self.DailyDose.get() + "\n")
        self.txtprescription.insert(END, "Side Effect:\t\t" + self.sideEfect.get() + "\n")
        self.txtprescription.insert(END, "Further Information:\t\t" + self.FurtherInformation.get() + "\n")
        self.txtprescription.insert(END, "Storage Advice:\t\t" + self.StorageAdvice.get() + "\n")
        self.txtprescription.insert(END, "Driving Using Machine:\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtprescription.insert(END, "Patient ID:\t\t" + self.PatientId.get() + "\n")
        self.txtprescription.insert(END, "NHS Number:\t\t" + self.nhsNumber.get() + "\n")
        self.txtprescription.insert(END, "Patient Name:\t\t" + self.PatientName.get() + "\n")
        self.txtprescription.insert(END, "Date of Birth:\t\t" + self.DateOfBirth.get() + "\n")
        self.txtprescription.insert(END, "Patient Address:\t\t" + self.PatientAddress.get() + "\n")



        # ====Delete function=================
    def delete_fun(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="mydata")
        my_cursor=conn.cursor()
        del_query="delete from hospital where reference_no=%s"
        value=(self.ref.get(),)
        my_cursor.execute(del_query,value)
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully!")
           

    #   ===============Clear Function=============
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtprescription.delete("1.0",END)

    # ============Exit Function=============
    def Exit(self):
        iexit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iexit:  # No need to check for `> 0`, since `askyesno` returns `True` or `False`
            self.root.destroy()  # Use `self.root`, not `root`
       
  
       
       
     
       


root = Tk()
ob = Hospital(root)
root.mainloop()