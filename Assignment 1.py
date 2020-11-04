print(" ASSIGNMENT-1 ")

"-------------------------------------------------------------------------------"
print("Exercise 1:---------------------------------------------------")

width = 17
height = 12.0
delimiter = '.'

##1. width/2:
print("answer number 1 (width/2) is:", width/2)
print( type(width/2) )
    
##2. width/2.0
print("answer number 2 (width/2.0) is:",width/2.0)
print( type(width/2.0) )

##3. height/3
print("answer number 3 (height/3) is:",height/3)
print( type(height/3) )

##4. 1 + 2 * 5
print("answer number 4 (1 + 2 * 5) is:",1 + 2 * 5)
print( type(1 + 2 * 5) )

##5. delimiter * 5
print("answer number 5 (delimiter * 5) is:",delimiter * 5)
print( type(delimiter * 5) )


"-------------------------------------------------------------------------------"
print("Exercise 2:-----------------------------------------------------------")

Temperature = float(input("Enter temperature in Fahrenheit:"))
Celsius = (Temperature - 32)* 5/9
print("Temperature in Celsius: ",Celsius)


"-------------------------------------------------------------------------------"
print("Exercise 3:-----------------------------------------------------------")

SECONDS_PER_MINUTE= 60
seconds= int(input("Enter number of seconds:"))

minutes= seconds / SECONDS_PER_MINUTE
seconds= seconds % SECONDS_PER_MINUTE

print("the duration is:", "%02d minutes and %02d seconds "% (minutes,seconds))


"-------------------------------------------------------------------------------"
print("Exercise 4:-----------------------------------------------------------")

list= [10,20,30,40,50,60,70,80]
print("List of elements are:", list)
print("length of list:", len(list))
print("first element of the list:", list[0])
print("fourth element of the list:", list[3])


"-------------------------------------------------------------------------------"
print("Exercise 5:-----------------------------------------------------------")

list= [10,20,30,40,50,60,70,80]
print("List of elements are:", list)
print("poping last element:", list.pop())
print(list)
print("inserting '90' in 5th position:", list.insert(5,90))
print(list)
print("removing '20' element from the list:", list.remove(20))
print(list)











