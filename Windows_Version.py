 #!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = "0.1.1 for Windows 10"
__author__  = "Goutham Dhondi,Deepika Amruth,Sreeja Ayyawari, Mani Dhondi"
__license__ = 'MIT'

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbToCSV import toCSV
from csvToPdf import CsvtoPDF
from dialog import OptionDialog
import pymysql
import sqlite3

def create_database():
    """Function to create a Database"""
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dmce_inventory (product_id text PRIMARY KEY , product_type text , model_no text , manufacturer text , department text , location text ,incharge text, comment text)")
    conn.commit()
    conn.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Stock():
    """Creating a main window on Inventory"""

    def __init__(self, root):
        """Default __INIT__ Function"""

        self.root=root
        self.root.title("I.T.S - For Datta Meghe College Of Engineering")
        self.root.geometry("1200x660+160+80")
        self.root.resizable(0, 0)

        self.product_id_var = StringVar()
        self.product_type_var = StringVar()
        self.model_no_var = StringVar()
        self.manufacturer_var = StringVar()
        self.department_var = StringVar()
        self.location_var = StringVar()
        self.incharge_var = StringVar()

        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()




        head_title = Label(self.root,text="Inventory Tracking System",bd=10, relief=GROOVE, font=("ariel", 20 , "bold"), bg="RED", fg="white")
        head_title.pack(side="top", pady=20, padx=10, fill=X)

        #===================================================================================================================================
        #===============================MANAGE_FRAME========================================================================================
        #===================================================================================================================================

        Manage_Frame=Frame(self.root, bd=5, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=10, y=80, width=350, height=570)

        m_title=Label(Manage_Frame,text="Manage Inventory", font=("", 20 , "bold"), bg="crimson", fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        #------------------------------------------------------------------------------------------------------------------------------------

        def caps(event):
            """Function to Convert Text To UPPERCAP"""
            self.product_id_var.set(self.product_id_var.get().upper())
            self.product_type_var.set(self.product_type_var.get().upper())
            self.model_no_var.set(self.model_no_var.get().upper())
            self.manufacturer_var.set(self.manufacturer_var.get().upper())
            self.location_var.set(self.location_var.get().upper())
            self.incharge_var.set(self.incharge_var.get().upper())
            self.search_txt_var.set(self.search_txt_var.get().upper())

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_product_id=Label(Manage_Frame,text="Product ID : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_product_id.grid(row=1, column=0, padx=10, pady=10,sticky ="w")

        txt_product_id=Entry(Manage_Frame, font=("times new roman", 13 , "bold") ,bd=2, relief=GROOVE, textvariable=self.product_id_var)
        txt_product_id.bind("<KeyRelease>", caps)
        txt_product_id.grid(row=1, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_type=Label(Manage_Frame,text="Product Type : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_type.grid(row=2, column=0, padx=10, pady=10,sticky ="w")

        txt_type=Entry(Manage_Frame, font=("times new roman", 13 , "bold") ,bd=2, relief=GROOVE, textvariable=self.product_type_var)
        txt_type.bind("<KeyRelease>", caps)
        txt_type.grid(row=2, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_model_no=Label(Manage_Frame,text="Model No : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_model_no.grid(row=3, column=0, padx=10, pady=10,sticky ="w")

        txt_model_id=Entry(Manage_Frame, font=("times new roman", 13 , "bold") ,bd=2, relief=GROOVE, textvariable=self.model_no_var)
        txt_model_id.bind("<KeyRelease>", caps)
        txt_model_id.grid(row=3, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_manufacturer=Label(Manage_Frame,text="Manufacturer : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_manufacturer.grid(row=4, column=0, padx=10, pady=10,sticky ="w")

        txt_manufacturer=Entry(Manage_Frame, font=("times new roman", 13 , "bold") ,bd=2, relief=GROOVE, textvariable=self.manufacturer_var)
        txt_manufacturer.bind("<KeyRelease>", caps)
        txt_manufacturer.grid(row=4, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_department=Label(Manage_Frame,text="Department : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_department.grid(row=5, column=0, padx=10, pady=10,sticky ="w")

        combo_department=ttk.Combobox(Manage_Frame, width=18, font=("", 13, "bold" ), state="readonly" , textvariable=self.department_var)
        combo_department["values"]=("COMPUTER","ELECTRICAL","CIVIL","MECHANICAL","CHEMICAL","I.T.")
        combo_department.current(0)
        combo_department.grid(row=5, column=1, padx=10, pady=10,sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_location=Label(Manage_Frame,text="Location : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_location.grid(row=6, column=0, padx=10, pady=10,sticky ="w")

        txt_location=Entry(Manage_Frame, font=("times new roman", 13 , "bold") ,bd=2, relief=GROOVE, textvariable=self.location_var)
        txt_location.bind("<KeyRelease>", caps)
        txt_location.grid(row=6, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_incharge=Label(Manage_Frame,text="Incharge : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_incharge.grid(row=7, column=0, padx=10, pady=10,sticky ="w")

        txt_incharge=Entry(Manage_Frame, font=("times new roman", 13 , "bold") ,bd=2, relief=GROOVE, textvariable=self.incharge_var)
        txt_incharge.bind("<KeyRelease>", caps)
        txt_incharge.grid(row=7, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------

        lbl_comment=Label(Manage_Frame,text="Comment : ", font=("", 10 , "bold"), bg="crimson", fg="white")
        lbl_comment.grid(row=8, column=0, padx=10, pady=10,sticky ="w")

        self.txt_comment=Text(Manage_Frame, width=20, height=3, bd=2, relief=GROOVE, font=("times new roman", 13 , ""))
        self.txt_comment.grid(row=8, column=1, padx=10, pady=10, sticky ="w")

        #------------------------------------------------------------------------------------------------------------------------------------




        #===================================================================================================================================
        #==========================BUTTON_FRAME=============================================================================================
        #===================================================================================================================================

        Button_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE, bg="yellow")
        Button_Frame.place(x=5, y=500, width=330, height=50)

        #------------------------------------------------------------------------------------------------------------------------------------
        add_button=Button(Button_Frame, text="Add", width=8, highlightbackground="yellow", command=self.add_items)
        add_button.grid(row=0, column=0, padx=5, pady=7)

        #------------------------------------------------------------------------------------------------------------------------------------
        update_button=Button(Button_Frame, text="Update", width=8, highlightbackground="yellow", command=self.update_data)
        update_button.grid(row=0, column=1, padx=5, pady=7)

        #------------------------------------------------------------------------------------------------------------------------------------
        delete_button=Button(Button_Frame, text="Delete", width=8, highlightbackground="yellow", command=self.delete_data)
        delete_button.grid(row=0, column=2, padx=5, pady=7)

        #------------------------------------------------------------------------------------------------------------------------------------
        clear_button=Button(Button_Frame, text="Clear", width=10, highlightbackground="yellow", command=self.clear)
        clear_button.grid(row=0, column=3, padx=5, pady=7)



        #===================================================================================================================================
        #==========================DETAIL_FRAME=============================================================================================
        #===================================================================================================================================

        Detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=370, y=80, width=820, height=570)


        #===================================================================================================================================
        #==========================SEARCH_FRAME=============================================================================================
        #===================================================================================================================================

        Search_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="yellow")
        Search_Frame.place(x=10, y=10, width=792, height=60)

        lbl_search=Label(Search_Frame,text="Search By : ", font=("", 13 , "bold"), bg="yellow", fg="red")
        lbl_search.grid(row=0, column=0, padx=10, pady=10,sticky ="w")

        combo_search_by=ttk.Combobox(Search_Frame, width=13, font=("", 13, "" ), state="readonly", textvariable=self.search_by_var)
        combo_search_by["values"]=("All","Product ID.","Product Type","Model No","Manufacturer","Department","Location","Incharge")
        combo_search_by.current(0)
        combo_search_by.grid(row=0, column=1, padx=2, pady=10,sticky ="w")



        txt_search=Entry(Search_Frame, width=22,font=("times new roman", 15 ) ,bd=2, relief=GROOVE, textvariable=self.search_txt_var)
        txt_search.bind("<KeyRelease>", caps)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky ="w")

        search_button=Button(Search_Frame, text="Search", width=8, highlightbackground="yellow", command=self.search_data)
        search_button.grid(row=0, column=3, padx=4, pady=5)

        view_button=Button(Search_Frame, text="View All", width=8, highlightbackground="yellow", command=self.view_data)
        view_button.grid(row=0, column=4, padx=9, pady=5)

        tocsv_button=Button(Search_Frame, text="Export", width=8, highlightbackground="yellow", command=self.export_data)
        tocsv_button.grid(row=0, column=5, padx=9, pady=5)

        #===================================================================================================================================
        #==========================TABLE_FRAME=============================================================================================
        #===================================================================================================================================

        Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="yellow")
        Table_Frame.place(x=10, y=80, width=792, height=472)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.View_Table=ttk.Treeview(Table_Frame, columns=("pid","ptype","mno","manufacturer","department","location","incharge","comment"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.View_Table.xview)
        scroll_y.config(command=self.View_Table.yview)

        self.View_Table.heading("pid", text="Product ID.")
        self.View_Table.heading("ptype", text="Product Type")
        self.View_Table.heading("mno", text="Model No")
        self.View_Table.heading("manufacturer", text="Manufacturer")
        self.View_Table.heading("department", text="Department")
        self.View_Table.heading("location", text="Location")
        self.View_Table.heading("incharge", text="Incharge")
        self.View_Table.heading("comment", text="Comment")

        self.View_Table.column("pid", width=90)
        self.View_Table.column("ptype", width=100)
        self.View_Table.column("mno", width=120)
        self.View_Table.column("manufacturer", width=90)
        self.View_Table.column("department", width=120)
        self.View_Table.column("location", width=90)
        self.View_Table.column("incharge", width=130)
        self.View_Table.column("comment", width=250)


        self.View_Table["show"]="headings"
        self.View_Table.pack(fill=BOTH, expand=1)
        self.View_Table.bind("<ButtonRelease-1>", self.get_cursor)


        self.view_data()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def add_items(self):
        """Function to ADD item to Database"""
       
        if self.product_id_var.get()=="":
            messagebox.showerror("Error","Product ID. cannot be blank!!!")
        
        elif self.unique_id()==TRUE:
            messagebox.showerror("Error","Product ID. Already Exists!!!")
            
        elif self.product_type_var.get()=="":
            messagebox.showerror("Error","Enter Product Type..!")
            
        elif self.model_no_var.get()=="":
            messagebox.showerror("Error","Enter Model Number..!")
            
        elif self.manufacturer_var.get()=="":
            messagebox.showerror("Error","Enter Manufacture Company..!")
                      
        elif self.location_var.get()=="":
            messagebox.showerror("Error","Enter Location !!!!")
            
        elif self.incharge_var.get()=="":
            messagebox.showerror("Error","Enter InCharge !!!")
                                    
        else:
            try:
                con=sqlite3.connect('inventory.db')
                cur=con.cursor()
                cur.execute(" insert into dmce_inventory values (?,?,?,?,?,?,?,?)",(
                                                                                            self.product_id_var.get(),
                                                                                            self.product_type_var.get(),
                                                                                            self.model_no_var.get(),
                                                                                            self.manufacturer_var.get(),
                                                                                            self.department_var.get(),
                                                                                            self.location_var.get(),
                                                                                            self.incharge_var.get(),
                                                                                            self.txt_comment.get('1.0',END),
                                                                                          ))
                con.commit()
                self.view_data()
                con.close()

            except:
                pass

            else:
                self.clear()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_data(self):
        """Function to UPDATE an item of Database"""

        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute("update dmce_inventory set  product_type=? , model_no=? , manufacturer=? , department=? , location=? ,incharge=?, comment=? where product_id=?",(
                                                                                                                                                                        self.product_type_var.get(),
                                                                                                                                                                        self.model_no_var.get(),
                                                                                                                                                                        self.manufacturer_var.get(),
                                                                                                                                                                        self.department_var.get(),
                                                                                                                                                                        self.location_var.get(),
                                                                                                                                                                        self.incharge_var.get(),
                                                                                                                                                                        self.txt_comment.get('1.0',END),
                                                                                                                                                                        self.product_id_var.get()
                                                                                                                                                                     ))
        con.commit()
        self.view_data()
        self.clear()
        con.close()        
     
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def delete_data(self):
        """Function to DELETE an item from the Database"""

        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute("delete from dmce_inventory where product_id=?",(self.product_id_var.get(),))
        con.commit()
        self.view_data()
        self.clear()
        con.close()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def clear(self):
        """Function to CLEAR all Input Fields"""

        self.product_id_var.set("")
        self.product_type_var.set("")
        self.model_no_var.set("")
        self.manufacturer_var.set("")
        self.location_var.set("")
        self.incharge_var.set("")
        self.txt_comment.delete("1.0", END)
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
   
    def unique_id(self):
        """Function to Show Error if user enter Existing Product ID."""

        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute('SELECT COUNT(*) FROM dmce_inventory where product_id=?',(self.product_id_var.get(),)) 
        id_exist = cur.fetchone()
        con.close()
        # print(id_exist)
        return id_exist[0] > 0
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
    
    def anonymus_input(self):  
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute("select COUNT(*) from dmce_inventory where product_id=? OR product_type=? OR model_no=? OR manufacturer=? OR department=? OR location=? OR incharge=?", (
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                         ))
                          
        data_exists=cur.fetchone()  
        con.close()
        print(data_exists)
        if data_exists[0] != 0 :
            return FALSE
        else :
            return TRUE
            
    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def search_data(self):
        """Function to Search for items in Database"""

        con=sqlite3.connect('inventory.db')
        cur=con.cursor()

        if self.search_by_var.get()=="Product ID.":
            cur.execute("select * from dmce_inventory where product_id=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()

        elif self.search_by_var.get()=="Product Type":
            cur.execute("select * from dmce_inventory where product_type=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()

        elif self.search_by_var.get()=="Model No":
            cur.execute("select * from dmce_inventory where model_no=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()

        elif self.search_by_var.get()=="Manufacturer":
            cur.execute("select * from dmce_inventory where manufacturer=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()

        elif self.search_by_var.get()=="Department":
            cur.execute("select * from dmce_inventory where department=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()

        elif self.search_by_var.get()=="Location":
            cur.execute("select * from dmce_inventory where location=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()

        elif self.search_by_var.get()=="Incharge":
            cur.execute("select * from dmce_inventory where incharge=?", ( self.search_txt_var.get(),))
            rows=cur.fetchall()
 #------------------------------------------------------------------------------------------------
        elif self.search_txt_var.get()=="":
            
            messagebox.showerror("Error","Please Enter ''Input text'' to search")
            self.search_txt_var.set("")
                
            con=sqlite3.connect('inventory.db')
            cur=con.cursor()
            cur.execute("select * from dmce_inventory")
            rows=cur.fetchall()
            self.View_Table.delete(*self.View_Table.get_children())
                
            if len(rows)!=0:
                for row_value in rows:
                     self.View_Table.insert("", END, values=row_value)
                con.commit()
            con.close()
  #----------------------------------------------------------------------------------------------  
        elif self.anonymus_input()==TRUE:
            messagebox.showerror("Error","No Such data Exist")
            self.search_txt_var.set("")
                
            con=sqlite3.connect('inventory.db')
            cur=con.cursor()
            cur.execute("select * from dmce_inventory")
            rows=cur.fetchall()
            self.View_Table.delete(*self.View_Table.get_children())
                
            if len(rows)!=0:
                for row_value in rows:
                     self.View_Table.insert("", END, values=row_value)
                con.commit()
            con.close() 
            
        else:
            cur.execute("select * from dmce_inventory where product_id=? OR product_type=? OR model_no=? OR manufacturer=? OR department=? OR location=? OR incharge=?", (
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                            self.search_txt_var.get(),
                                                                                                                                                                         ))
        rows=cur.fetchall()


        self.View_Table.delete(*self.View_Table.get_children())
        if len(rows)!=0:
            for row_values in rows:
                self.View_Table.insert("", END, values=row_values)
            con.commit()
        con.close()
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               
    def view_data(self):
        """Function to VIEW data into Table"""

        self.search_txt_var.set("")
        con=sqlite3.connect('inventory.db')
        # print(con)
        cur=con.cursor()
        # print(cur)
        cur.execute("select * from dmce_inventory")
        rows=cur.fetchall()
        # print(rows)
        self.View_Table.delete(*self.View_Table.get_children())
        if len(rows)!=0:
            for row_value in rows:
                self.View_Table.insert("", END, values=row_value)
                # print(row_value)
            con.commit()
        else:
            messagebox.showerror("Error","Databases is Empty please insert some data ")
        con.close() 
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def export_data(self):
        """Function to Expoet data into various Formats"""
        
        que1 = messagebox.askquestion( "Export",
                                "Do you want to export to CSV?",
                                icon ='info')
        if que1 == 'yes':
            toCSV()

        que2 = messagebox.askquestion( "Export",
                                        "Do you want to export to PDF?",
                                        icon ='info')

        if que2 == 'yes':
            CsvtoPDF()
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        

    def get_cursor(self,event):
        """Function to SELECT a particular item"""

        try:
            cursor_row_num=self.View_Table.focus()
            # print(cursor_row_num)
            row_content=self.View_Table.item(cursor_row_num)
            # print(row_content)
            row_values=row_content["values"]
            # print(row)

            self.product_id_var.set(row_values[0])
            self.product_type_var.set(row_values[1])
            self.model_no_var.set(row_values[2])
            self.manufacturer_var.set(row_values[3])
            self.department_var.set(row_values[4])
            self.location_var.set(row_values[5])
            self.incharge_var.set(row_values[6])
            self.txt_comment.delete("1.0", END)
            self.txt_comment.insert(END, row_values[7])

        except:
            pass

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_- 

if __name__ == '__main__':
    """START THE PROGRAM"""

    create_database()
    root = Tk()
    root.title("Stock Management System")
    root.iconbitmap("its_icon.ico")
    ob = Stock(root)
    root.mainloop()
