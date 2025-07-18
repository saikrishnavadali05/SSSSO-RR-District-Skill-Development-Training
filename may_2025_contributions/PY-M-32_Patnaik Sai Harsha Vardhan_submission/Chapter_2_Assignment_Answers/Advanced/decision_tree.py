#24.Use indentation to structure a decision tree using if-elif-else blocks clearly.
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D or F")
#output: Enter your score: <score>
#output: Grade: A (if score >= 90)
#output: Grade: B (if score >= 75)
#output: Grade: C (if score >= 60)
#output: Grade: D or F (if score < 60)
#output: Enter your score: 85
#output: Grade: B