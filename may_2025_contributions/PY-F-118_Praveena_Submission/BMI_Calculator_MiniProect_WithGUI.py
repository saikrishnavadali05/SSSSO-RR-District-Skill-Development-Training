#Mini Project : BMI Calculator
#Date : 21 Jun 2025
#Author : Praveena Kumbum
#Description : Calculates Body Mass Index (BMI) from user’s weight and height to classify underweight, normal, overweight, or obese status. 
#The program prompts for weight and height, computes BMI = weight/(height²), and displays the result and category.

import tkinter
from tkinter import ttk,messagebox

#Main window
root = tkinter.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
#root.configure(bg = "#5c33ff" )
root.resizable(False, False)

#BMI Calculation based on the unit (US/Metric) selected.
def BMI_Calculator(Prsn_Weight,Prsn_Height,Unit):
    try:
        Prsn_Weight = float(Prsn_Weight)
        Prsn_Height = float(Prsn_Height)
        if Unit == 'Metric':
            BMI = round(Prsn_Weight / (Prsn_Height/100)**2 , 1)
        elif Unit == 'US':
            BMI = round(Prsn_Weight * 703 / Prsn_Height**2 , 1)
        else:
            BMI = None
        return BMI
    except:
        return None

#Displays the BMI value and the category they fall based on the BMI value.
#Also provides suggestion (which is optional) based on the BMI category, Age and Gender.
def Prediction_BMI(BMI,Prsn_Age,Prsn_Gender,Prsn_Name):
    Prsn_Age = int(Prsn_Age)

    if Prsn_Age < 18:
        return f"Dear {Prsn_Name}, your BMI is {BMI}. For children and teens, BMI needs to be interpreted using age- and gender-specific percentiles."

 # For adults (age 18 and above)
    if BMI < 18.5:
        category = "Underweight"
    elif 18.5 <= BMI < 25:
        category = "Normal weight"
    elif 25 <= BMI < 30:
        category = "Overweight"
    else:
        category = "Obese"

    message = f"Dear {Prsn_Name}, your BMI is {BMI} and you fall under the category: {category}."

# Optional: gender-based suggestion
    if Prsn_Gender.lower() == 'female':
        if category in ["Overweight", "Obese"]:
            message += "\nNote: Women may naturally have a higher body fat percentage. Consider getting a body composition check."
        elif category == "Underweight":
            message += "\nNote: Being underweight may affect hormonal health in women. Consider consulting a doctor."

    elif Prsn_Gender.lower() == 'male':
        if category in ["Overweight", "Obese"]:
            message += "\nNote: Higher BMI in men can be linked to cardiovascular risk. Consider lifestyle adjustments and a heart health check."
        elif category == "Underweight":
            message += "\nNote: Low BMI may indicate low muscle mass or nutrition deficiency. Consider a nutritional evaluation."
    return message

#Function for capturing the data submitted in Name, Age, Gender, Unit, Height and Weight fields 
#on clicking the Calculate_BMI button.
def OnClick_Calculate_BMI():
    Prsn_Name = Name_Textbox.get().strip().capitalize()
    Prsn_Age = Age_Textbox.get().strip()
    Prsn_Gender = Gender_Dropdown.get().strip()
    Unit = Unit_Dropdown.get().strip()
    Prsn_Height = Height_Textbox.get().strip()
    Prsn_Weight = Weight_Textbox.get().strip()

    if not (Prsn_Name and Prsn_Age and Prsn_Gender and Unit and Prsn_Height and Prsn_Weight):
        messagebox.showwarning("Missing Info","Please fill all the information.")
        return
    try:
        Prsn_Age = int(Prsn_Age)
        if not (2 <= Prsn_Age <= 120):
            raise ValueError("Age out of range.")
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid age between 2 and 120.")
        return

    BMI = BMI_Calculator(Prsn_Weight,Prsn_Height,Unit)
    if BMI is None:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for height and weight.")
        return
    result = Prediction_BMI(BMI,Prsn_Age,Prsn_Gender,Prsn_Name)
    messagebox.showinfo("BMI Result", result)



#Name field
Name_Label = tkinter.Label(root , text = "Enter Name :" )
Name_Label.pack(anchor=tkinter.W,padx=10)
Name_Textbox = tkinter.Entry(root)
Name_Textbox.pack(anchor=tkinter.W,padx=10)

#Age field
Age_Label = tkinter.Label(root , text = "Enter Age :" )
Age_Label.pack(anchor=tkinter.W,padx=10,pady=2)
Age_Textbox = tkinter.Entry(root)
Age_Textbox.pack(anchor=tkinter.W,padx=10,pady=2)

#Gender field
Gender_Label = tkinter.Label(root,text = "Select Gender :")
Gender_Label.pack(anchor=tkinter.W,padx=10,pady=2)
choices = ['Male','Female']
Gender_Dropdown = ttk.Combobox(root,values = choices,)
Gender_Dropdown.pack(anchor=tkinter.W,padx=10,pady=2)

#Unit System selection:
Unit_Label = tkinter.Label(root,text = "Select Unit :")
Unit_Label.pack(anchor=tkinter.W,padx=10,pady=2)
choices = ['Metric','US']
Unit_Dropdown = ttk.Combobox(root,values = choices,)
Unit_Dropdown.pack(anchor=tkinter.W,padx=10,pady=2)

#Weight field
Weight_Lable = tkinter.Label(root,text = "Enter Weight (in Kg or Pounds): ")
Weight_Lable.pack(anchor=tkinter.W,padx=10,pady=2)
Weight_Helptext = tkinter.Label(root,text = "Ex: Enter 70 kg if using Metric or 154 lbs if using US",fg='gray')
Weight_Helptext.pack(anchor=tkinter.W,padx=10,pady=2)
Weight_Textbox = tkinter.Entry(root)
Weight_Textbox.pack(anchor = tkinter.W,padx=10,pady=2)

#Height field
Height_Lable = tkinter.Label(root,text = "Enter Height (in Centimeters or Inches ): ")
Height_Lable.pack(anchor=tkinter.W,padx=10,pady=2)
Height_Helptext = tkinter.Label(root,text = "E.g., 175 centimeters if using Metric or 69 inches if using US",fg='gray')
Height_Helptext.pack(anchor=tkinter.W,padx=10,pady=2)
Height_Textbox = tkinter.Entry(root)
Height_Textbox.pack(anchor = tkinter.W,padx=10,pady=2)

#Calculate BMI Button
Calculate_BMI_Button = tkinter.Button(root, text = "Calculate BMI",command=OnClick_Calculate_BMI)
Calculate_BMI_Button.pack(anchor=tkinter.W,padx=10)

root.mainloop()