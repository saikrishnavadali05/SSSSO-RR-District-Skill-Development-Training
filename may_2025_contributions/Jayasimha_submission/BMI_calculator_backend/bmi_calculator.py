"""
BMI Calculator Project
Calculates Body Mass Index and classifies health status
Author: Jayasimha Valam
Date: July 15, 2025
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / height (m)²
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

def classify_bmi(bmi):
    """
    Classify BMI into health categories
    
    Args:
        bmi (float): BMI value
    
    Returns:
        str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_positive_input(prompt):
    """
    Get positive numeric input from user with validation
    
    Args:
        prompt (str): Input prompt message
    
    Returns:
        float: Valid positive number
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("ERROR: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("ERROR: Please enter a valid number.")

def main():
    """
    Main function to run the BMI calculator
    """
    print("=" * 40)
    print("        BMI CALCULATOR")
    print("=" * 40)
    print()
    
    # Get user input with validation
    weight = get_positive_input("Enter your weight (in kg): ")
    height = get_positive_input("Enter your height (in meters): ")
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI
    category = classify_bmi(bmi)
    
    # Display results
    print("\n" + "=" * 40)
    print("           RESULTS")
    print("=" * 40)
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("=" * 40)
    
    # Additional health information
    print("\nBMI Categories:")
    print("- Underweight: BMI < 18.5")
    print("- Normal weight: BMI 18.5-24.9")
    print("- Overweight: BMI 25-29.9")
    print("- Obese: BMI >= 30")
    
    # Health recommendations
    print(f"\nHealth Recommendation:")
    if category == "Underweight":
        print("Consider consulting a healthcare provider about healthy weight gain.")
    elif category == "Normal weight":
        print("Great! Maintain your current healthy lifestyle.")
    elif category == "Overweight":
        print("Consider a balanced diet and regular exercise.")
    else:
        print("Consult a healthcare provider for personalized advice.")

if __name__ == "__main__":
    main()
