print(" ASSIGNMENT-2 ")
print()

"-------------------------------------------------------------------------------"
print("Exercise 1:---------------------------------------------------")

l = [10,20,30,40,50]
print("List of elements are:", l)
sum = 0
for s in l:
    sum=sum+s
print("Sum of", l, "is:", sum)
print()

"-------------------------------------------------------------------------------"
print("Exercise 2:-----------------------------------------------------------")

list1 = [10,10,20,30,40,50,80]
list2 = [10,40,40,60,70,80]
print("List1 contains:", list1)
print("List2 contains:", list2)

L1=set(list1)
L2=set(list2)
common= L1.intersection(L2)
print("Common elements from list1 and list2 are:",list(common))
print()

"-------------------------------------------------------------------------------"
print("Exercise 3:-----------------------------------------------------------")

list=[1, 5, 7, 12 ,15]
print("List contains:",list)
print("Each number in the list are:")
for n in list:
    print(n)
for s in list:   
    print("Square of",s,":",s**2)
print()

"-------------------------------------------------------------------------------"
print("Exercise 4:-----------------------------------------------------------")
ask = str(input("Enter some string:"))
print(type(ask))
print("The string which user have input is:",ask)

len=0
for l in ask:
    len=len+1
    
print("Length of the string:",len)
print()

"-------------------------------------------------------------------------------"
print("Exercise 5:-----------------------------------------------------------")

ask=str(input("Enter some string:"))
print(type(ask))
print("The string which user have input is:",ask)
print("Uppercase of a string:", ask.upper())
print("Lowercase of a string:", ask.lower())












