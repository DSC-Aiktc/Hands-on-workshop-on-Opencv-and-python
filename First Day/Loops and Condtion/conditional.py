#if-else
#DRIVIG TEST ELIGIBLITY

age =int(input("ENTER YOUR AGE: "))

if age < 18:
	print("NOT ELIGIBLE FOR DRIVING TEST")
else:
	print("ELIGIBLE FOR DRIVING TEST")

#elif
#MARKS GRADING

#NORMAL
marks = int(input("ENTER YOUR MARKS: "))

if marks >= 90:
	print("A GRADE")
elif marks >=80 and marks < 90:  #range and 80 < marks < 90
	print("B GRADE")
else:
	print("O GRADE")

#WITH IN-BETWEEN VALUES
marks = int(input("ENTER YOUR MARKS: "))

if marks >= 90:
	print("A GRADE")
elif 80 < marks < 90:
	print("B GRADE")
else:
	print("O GRADE")
