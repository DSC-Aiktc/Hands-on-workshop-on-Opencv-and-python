##FUNCTION EXPLANATION

#NORMAL

#EXAMPEL 1
def hello():
    print("WELCOME TO DSCAIKTC WORKSHOP!!")

hello()

#EXAMPLE 2
def sum(a, b):
    return a + b

print(sum(10,20))

#EXAMPLE 3
def welcome(*args): 
    for arg in args: 
        print (arg)
   
welcome('DSCAIKTC', 'LEARN', 'LIKE', 'SHARE', 'SUBSCRIBE') 

#LAMBDA

#anonamous function cuz name not difined

#normal function
def square():
	x = int(input("Enter a number: "))
	return x*x
print(square())

#lambda version
a = int(input("Enter a number: "))
b = lambda a:a*a
print(b(a))