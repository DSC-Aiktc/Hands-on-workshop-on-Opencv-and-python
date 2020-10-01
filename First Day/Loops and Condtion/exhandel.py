#EXCEPTION VS ERROR EXPLANATION

#EXCEPTION EXAMPLE 1
a = 7
b = 0
print(a/b)

#EXCEPTION EXAMPLE 2
print(c)

##TRY-EXCEPT

#BY KNOWING THE EXCEPTION (PARTICULAR)

#EXAMPLE 1
a = 7
b = 0
try:
	print(a/b)
except ZeroDivisionError :
	print("CANNOT DIVIDE WITH ZERO!")

#EXAMPLE 2
try:
	print(c)
except NameError:
	print("VARIABLE NOT DEFINED!")

#BY KNOWING THE EXCEPTION (NOT PARTICULAR)
#WILL FIND FROM ALL THE EXCEPTION WHAT THIS EXCEPTION IS
a = 7
b = 0
try:
	print(a/b)
except:
	print("EXCEPTION OCCURED!")

#BY NOT KNOWING THE EXCEPTION

#TO WHAT THE EXCEPTION IS (INFO)
a = 7
b = 0
try:
	print(a/b)
except Exception as e:
	print(e)




