#RANGE CONCEPT

for x in range(0,10):
	print(x)

##FOR LOOP

#EVEN NUMBERS FROM 1 TO 10

for x in range(0,11):
	if(x%2==0):print(x)

#FOR LOOP TO GET VALUE FROM LIST

li = ['ONE','TWO','THREE','FOUR']
for x in li:
	print(x)

#INTRODUCE len() FUNCTION

li = ['ONE','TWO','THREE','FOUR']
print(len(li))

#TO FIND NO. OF ITERATION

#NORMAL (USING A AVARIABLE)
n = 0
li = ['ONE','TWO','THREE','FOUR']
for x in li:
	print(n,x)
	n+=1 #Equivalant To n = n+1

#USING LEN() AND RANGE() FUNCTION
li = ['ONE','TWO','THREE','FOUR']
for x in range(len(li)):
	print(x,li[x])

#USING enumerate()
li = ['ONE','TWO','THREE','FOUR']
for x,y in enumerate(li):
	print(x,y)

##WHILE LOOP

#PRINT CHARACTERS FROM THEIR ASCII VALUES
c = 97
while c<=122:
	print(chr(c))
	c+=1