print(" ASSIGNMENT-3 ")
print()

"-------------------------------------------------------------------------------"
print("Exercise 1:---------------------------------------------------")

print("Prime numbers from 1 to 100 are:")
for n in range(1,101):  
   if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
               break
       else:
           print(n)  
print()

"-------------------------------------------------------------------------------"
print("Exercise 2:-----------------------------------------------------------")

palindrome = str(input("Enter some string:"))
rev_str = palindrome[::-1]
print("reverse of a string:", rev_str)
if palindrome == rev_str:
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
print()

"-------------------------------------------------------------------------------"
print("Exercise 3:-----------------------------------------------------------")

s= "@Ekta_Shrestha21!!"
print("String:",s)
print()

upper_u = 0
lower_l = 0
digit_d = 0
special_s = 0

for i in s:
 if (i.isupper()): upper_u += 1
 elif (i.islower()): lower_l +=1
 elif (i.isdigit()): digit_d +=1
 else: special_s +=1
 
print("number of upper case:", upper_u)
print("number of lower case:", lower_l)
print("number of digits:", digit_d)
print("number of special symbols:", special_s)
print()

"-------------------------------------------------------------------------------"
print("Exercise 4:-----------------------------------------------------------")

n=int(input("Enter the number of terms: "))
sum=0
for i in range(1,n+1):
    sum=sum+(1/i)
print("The sum of series is",round(sum,2))
print()

"-------------------------------------------------------------------------------"
print("Exercise 5:-----------------------------------------------------------")

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print('*',end='')
    print()
print()

"-------------------------------------------------------------------------------"
print("Exercise 6:-----------------------------------------------------------")

String = str(input("Enter some string:"))
dic={}
for i in String:
   if i in dic.keys():
      dic[i]+=1
   else:
      dic[i]=1
print(dic)





























