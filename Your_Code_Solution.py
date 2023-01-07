def fibonacci(n):     #0 1 1 2 3 5 8 13 21 34 ........
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def armstrong(num):      # 1^n+5^n+3^n = 153
                         # 1^n+6^n+3^n+4^n =1634
    n = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** n
       temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

        
def greatestamongst(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print("The largest number is", largest)

    
def factorial(n):
    fact = 1
 
    for i in range(1, n+1):
        fact = fact * i
 
    print("The factorial of number is : ", end="")
    print(fact)

    
def traversing(list):
    print ("\n Array is :-")
    length = len(list)
    i = 0
    while i < length:
        print(list[i])
        i += 1
def addMatrix():
    print ("hello5")
def transposeMatrix():
    print ("hello6")
def linearSearch():
    print ("hello7")
def binarySearch():
    print ("hello8")
def bubbleSort():
    print ("hello9")
def insertionSort():
    print ("hello10")










print("----------------------"+ 
        "Welcome to Your Code Solutions"+ 
        "----------------------")
while True:
    print("\n-----------------Menu:----------------- \n ")
    print("Press 1 to find fibonacci number using recursion  \n")
    print("Press 2 to find armstrong number  \n")
    print("Press 3 to find greatest amongst the three  \n")
    print("Press 4 to find factorial of numbers using recursion \n")
    print("Press 5 to traversing the array  \n")
    print("Press 6 to add two matrices \n")
    print("Press 7 to  find transpose of matrics  \n")
    print("Press 8 to search elements using linear seacrh  \n")
    print("Press 9 to search elements using binary seacrh  \n")
    print("Press 10 to Bubble Sort \n")
    print("Press 11 to Insertion Sort \n")
    print("Press 0 to exit the menu. \n")
    
    choice =int(input("Enter the task you want to do: \n"))
    
    if choice == 1:
        n=int(input("enter the number"))
        a=fibonacci(n)
        print(a)
    elif choice == 2:
        num=int(input("enter the number"))
        armstrong(num)
        
    elif choice == 3:
        num1=int(input("enter number1"))
        num2=int(input("enter number2"))
        num3=int(input("enter number3"))
        greatestamongst(num1,num2,num3)

        
    elif choice == 4:                         #factorial
        n=int(input("enter the number"))
        factorial(n)

        
    elif choice == 5:
        lst = []                                      #adding elements in array
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = int(input("Element-"))
            lst.append(ele)
            
        traversing(lst)                               #calling func

        
    elif choice == 6:
        addMatrix()
    elif choice == 7:
        transposeMatrix()
    elif choice == 8:
        linearSearch()
    elif choice == 9:
        binarySearch()
    elif choice == 10:
        bubbleSort()
    elif choice == 11:
        insertionSort()
    elif choice == 0:
        break
    else:
        print("Invalid choice, please choose again\n")
