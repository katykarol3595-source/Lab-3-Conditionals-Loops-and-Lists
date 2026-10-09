# Asks the user to input a numeric grade (0-100).
grade = float(input("Enter your numeric grade (0-100):"))
#Uses an if-elif-else structure to convert the numeric grade to a letter grade
if 90 <= grade <= 100:
    letter_grade = "A"
elif 80 <= grade <= 90:
    letter_grade = "B"
elif 70 <= grade <= 80:
    letter_grade = "C"
elif 60 <= grade <= 70:
    letter_grade = "D"
elif 0 <= grade <= 60:
    letter_grade = "F"
else:
    letter_grade = "Invalid"
#Prints the letter grade if valid
if letter_grade != "Invalid":
        print(f"Your grade is {letter_grade}")
#Includes a final message using a conditional expression
else:
        print(" Error: Please enter a grade between 0 and 100.")
