"""
    Implement question number 1, 2 and 6 from Session 3 Exercise as different functions

    Exercise 1: Write a program to display all prime numbers from 1 to 100.
    Exercise 2: Ask the user for a string and print out whether this string is a palindrome or not.
    Exercise 6: Create a dictionary that has a key value pair of letters and the number of occurrences of
    that letter in a string.
"""

#Exercise 1
def prime_numbers(n):
    if n==1 or n==2:
        return True
    else:
        for i in range(2,n//2+1):
            if(n%i ==0):
                return False
        else:
            return True

#Exercise 2
def check_palindrome(item):
    rev_str=""
    for i in range(len(item)-1,-1,-1):
        rev_str+=item[i]

    if(item==rev_str):
        return True
    else:
        return False

#Exercise 6
def d(item):
    dic={}
    for i in item:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1

    return dic



def main():
    for i in range(1,101):
        if(prime_numbers(i)):
            print(i, end=" ")
    print("\n----------------------------------------")

    string=str(input("Enter some string:"))
    if(check_palindrome(string)):
        print("The string is palindrome.")
    else:
        print("The string is not palindrome.")
    print("\n----------------------------------------")
    string=str(input("Enter some string:"))
    print(d(string))


if __name__ == '__main__':
    main()
