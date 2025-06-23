#Python program of "BMI Calculator"
#Date : 21 June 2025
#Description : Calculates Body Mass Index (BMI) from user’s weight and height to classify underweight, normal, overweight, or obese status. 
#The program prompts for weight and height, computes BMI = weight/(height²), and displays the result and category.


print("\n******************Welcome to the BMI : \"Body Mass Index\" Calculator page*******************\n")

#User input person name
Prsn_Name = input("Please enter your Name : ").capitalize()

#User input person age
def Get_Prsn_Age():
    while True:
        try:
            Prsn_Age = int(input("Please enter your age : "))
            if Prsn_Age in range(2,121):
                return Prsn_Age
            else:
                print("Invalid Age. Please enter a valid age between 2 and 120.")
        #Age should always be numeric
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
#User input person gender
def Get_Valid_Gender():
    while True:
        try:
            Gender = input("Please enter the gender (Male / Female) : ").strip().capitalize()
            if Gender.isnumeric():
                raise ValueError("Numeric input is not allowed for gender.")
            
            if Gender in ["Male","Female"]:
                return Gender
            else:
                raise ValueError("Invalid gender entered.")
            
        except ValueError as ve:
            print(f"{ve} Please enter Male / Female.")
 
#Selection of units.
#Us Units: Height in Feet and Inches and Weight in Pounds.
#Metric Units : Height in CM and Weight in KG.

def Get_unit_system():
    while True:
        try:
            unit = input("Please select unit system : US or Metric (Type US or Metric): ").strip().lower()
            if unit in ['us','metric']:
                return unit
            else:
                raise ValueError("invalid unit system.")
        except ValueError as ve:
            print(f"{ve} Please enter 'US' or 'Metric'.")

#Based on the unit system (US/Metric) selected, 
#User will be asked to enter weight(Pounds/Kilograms) and Height(Inches/Meters) accordingly.
def Get_Weight_Height(unit):
    try:
        if unit == 'us':
            Prsn_Weight = float(input("Please enter your weight in pounds : "))
            Prsn_Height = float(input("Please enter your height in inches : "))
        else:
            Prsn_Weight = float(input("Please enter your weight in Kilograms : "))
            Prsn_Height = float(input("Please enter your height in meters : "))
        return Prsn_Weight, Prsn_Height
    except ValueError:
        print("Invalid input. Please enter numeric value for weight and height.")
        return Get_Weight_Height(unit)

#BMI Calculation based on the unit (US/Metric) selected.
def BMI_Calculator(Prsn_Weight,Prsn_Height,unit):

    if unit == 'metric':
        BMI = round(Prsn_Weight / Prsn_Height**2 , 1)
    elif unit == 'us':
        BMI = round(Prsn_Weight * 703 / Prsn_Height**2 , 1)
    else:
        BMI = None
    return BMI

#Displays the BMI value and the category they fall based on the BMI value.
#Also provides suggestion (which is optional) based on the BMI category, Age and Gender.
def Prediction_BMI(BMI,Prsn_Age,Prsn_Gender):
    if Prsn_Age < 18:
        print(f"\nDear {Prsn_Name}, your BMI is {BMI}. For children and teens, BMI needs to be interpreted using age- and gender-specific percentiles.")

 # For adults (age 18 and above)
    if BMI < 18.5:
        category = "Underweight"
    elif 18.5 <= BMI < 25:
        category = "Normal weight"
    elif 25 <= BMI < 30:
        category = "Overweight"
    else:
        category = "Obese"

        print(f"\nDear {Prsn_Name}, your BMI is {BMI} and you fall under the category: {category}.")

    # Optional: gender-based suggestion
    if Prsn_Gender.lower() == 'female':
        if category in ["Overweight", "Obese"]:
            print("\nNote: Women may naturally have a higher body fat percentage. Consider getting a body composition check.\n")
        elif category == "Underweight":
            print("\nNote: Being underweight may affect hormonal health in women. Consider consulting a doctor.\n")

    elif Prsn_Gender.lower() == 'male':
        if category in ["Overweight", "Obese"]:
            print("\nNote: Higher BMI in men can be linked to cardiovascular risk. Consider lifestyle adjustments and a heart health check.\n")
        elif category == "Underweight":
            print("\nNote: Low BMI may indicate low muscle mass or nutrition deficiency. Consider a nutritional evaluation.\n")


#Main Program:
Prsn_Age = Get_Prsn_Age()
Prsn_Gender = Get_Valid_Gender()
unit = Get_unit_system()
Prsn_Weight,Prsn_Height = Get_Weight_Height(unit)
BMI = BMI_Calculator(Prsn_Weight,Prsn_Height,unit)
Prediction_BMI(BMI,Prsn_Age,Prsn_Gender)