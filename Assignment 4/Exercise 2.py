"""
    Implement question number 1, 2 and 4 from Session 2 Exercise as different functions in a single
    
    Exercise 1: Choose a list of your choice and find the sum of all elements of that list.
    Exercise 2: Write a program that returns a list which contains common elements from two lists. Avoid
    the duplicate elements from lists.
    Exercise 4: Write a code to ask an input from the user which is a string and display the string along
    with its length.
"""

#Exercise 1
def list_sum(l):
    sum=0
    for i in l:
        sum+=i
    return  sum

#Exercise 2
def common(list1, list2):
    L1=set(list1)
    L2=set(list2)
    return L1.intersection(L2)

#Exercise 4
def len_string(ask):
    count=0
    for i in ask:
        count+=1
    return count


def main():
    list1=[10,20,30,40,50]
    print("The sum of the list {} is {}".format(list1,list_sum(list1)))
    print("-----------------------------------")
    list2=[10,40,40,60,70,80]
    print("The common elements from the list of {} and {}".format(list1,list2))
    print("Common: ",list(common(list1,list2)))
    print("-----------------------------------")
    string=input("Enter some string: ")
    print(" Length of the string {} is {}".format(string,len_string(string)))


if __name__ == '__main__':
    main()
