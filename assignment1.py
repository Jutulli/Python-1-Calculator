AmountOfLabs = int(input("Enter the number of labs completed: "))
AmountOfQuizzes = int(input("Enter the number of quizzes completed: "))

Assignment1 = int(input("Enter grade for Assignment 1: "))
Assignment2 = int(input("Enter grade for Assignment 2: "))
Assignment3 = int(input("Enter grade for Assignment 3: "))
Assignment4 = int(input("Enter grade for Assignment 4: "))

Midterm1 = int(input("Enter grade for Midterm 1: "))
Midterm2 = int(input("Enter grade for Midterm 2: "))

Final = int(input("Enter grade for Final Exam: "))
MidtermAndPreperation = int(input("Enter grade of Midterms and Final Preperation: "))

if AmountOfLabs > 5: AmountOfLabs = 5

if AmountOfQuizzes > 5: AmountOfQuizzes = 5

FinalGrade = (AmountOfLabs * 20/5) + (AmountOfQuizzes * 15/5) + (Assignment1 * 0.04) + (Assignment2 * 0.04) + (Assignment3 * 0.04) + (Assignment4 * 0.04) + (Midterm1 * 0.125) + (Midterm2 * 0.125) + (Final * 0.18) + (MidtermAndPreperation * 0.06)

print(round(FinalGrade, 2))
