import tkinter
from tkinter import ttk,messagebox

#Main window
root = tkinter.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
#root.configure(bg = "#5c33ff" )

#Function for capturing the data submitted in Name, Age, Gender, Unit, Height and Weight fields 
#on clicking the Calculate_BMI button.
def OnClick_Calculate_BMI():
    Name = Name_Textbox.get
    Age = Age_Textbox.get()
    Gender = Gender_Dropdown.get()

    if Name and Age and Gender:
        messagebox.showinfo(f"Status","Data Submitted")
    else:
        messagebox.showwarning("Warning","Please fill all the information.")

#Name field
Name_Label = tkinter.Label(root , text = " Enter Name :" )
Name_Label.pack(anchor=tkinter.W,padx=10)
Name_Textbox = tkinter.Entry(root)
Name_Textbox.pack(anchor=tkinter.W,padx=10)

#Age field
Age_Label = tkinter.Label(root , text = " Enter Age :" )
Age_Label.pack(anchor=tkinter.W,padx=10)
Age_Textbox = tkinter.Entry(root)
Age_Textbox.pack(anchor=tkinter.W,padx=10)

#Gender field
Gender_Label = tkinter.Label(root,text = "Select Gender :")
Gender_Label.pack(anchor=tkinter.W,padx=10)
choices = ['Male','Female']
Gender_Dropdown = ttk.Combobox(root,values = choices,)
Gender_Dropdown.pack(anchor=tkinter.W,padx=10)

#Calculate BMI Button
Calculate_BMI_Button = tkinter.Button(root, text = "Calculate BMI",command=OnClick_Calculate_BMI)
Calculate_BMI_Button.pack(anchor=tkinter.W,padx=10)

root.mainloop()