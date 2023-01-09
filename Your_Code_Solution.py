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

    
def factorial(n):                   #5X4X3X2X1=120
    fact = 1
 
    for i in range(1, n+1):
        fact = fact * i
 
    print("The factorial of number is : ", end="")
    print(fact)

    
def traversing(list):             #printing the elements of array & traversing
    print ("\n Array is :-")
    length = len(list)
    i = 0
    while i < length:
        print(list[i])
        i += 1


def insertMatrix():
    
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
  
    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")
  
    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)


    for i in range(R):           #printing the matrix
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()
            
def transposeMatrix():
    print("-------first enter a matric-------")

    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
  
    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")
  
    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    print("original matrix:-")
    for i in range(R):           #printing the matrix
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()
    print("Transpose matrix:-")
    for i in range(R):           #printing the transpose matrix
        for j in range(C):
            print(matrix[j][i], end = " ")
        print()

        
def linearSearch(arr,x):
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1


def binarySearch(arr, low, high,x):
    if high >= low:
 
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binarySearch(arr, mid + 1, high, x)
 
    else:
        return -1

    
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key




############# security function ##############

def security():
    userid=input("enter your userid:")
    passwd=int(input("enter password"))
    if (userid=="student" and passwd==123):
        main()                  # main function callilng
    else:
        print("Oops! incorrect password or UserID")
        






def main():
    print("----------------------"+ 
        "Welcome to Your Code Solutions"+ 
        "----------------------")
    while True:
        print("\n------------------------------------"+
          "Menu:"+
          "--------------------------------- \n ")
        print("Press 1 to find fibonacci number using recursion  \n")
        print("Press 2 to find armstrong number  \n")
        print("Press 3 to find greatest amongst the three  \n")
        print("Press 4 to find factorial of numbers using recursion \n")
        print("Press 5 to traversing the array  \n")
        print("Press 6 to inserting elements in matrix \n")
        print("Press 7 to find transpose of matrics  \n")
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
            insertMatrix()


        
        elif choice == 7:
            transposeMatrix()


        
        elif choice == 8:
            arr=[]
            n=int(input("enter the length of array"))
            for i in range (0,n):
                a=int(input("enter the value to array"))
                arr.append(a)
            print(arr)
            x=int(input("enter the number to find"))

            b=linearSearch(arr,x)      #func calling
        
            print("index of",x,"in the array is",b)


        
        elif choice == 9:
            arr=[]                      #initializing array
            n=int(input("enter the length of array"))      #taking input from user in an array
            for i in range (0,n):
                a=int(input("enter the value to array"))
                arr.append(a)
            print(arr)              #printing array
        
            x=int(input("enter the number to find"))
            result=binarySearch(arr,0,len(arr)-1,x)

            if result != -1:
                print("Element is present at index", str(result))
            else:
                print("Element is not present in array")

            
        elif choice == 10:
            arr=[]                     #initializing array
            n=int(input("enter the length of array"))      #taking input from user in an array
            for i in range (0,n):
                a=int(input("enter the value to array"))
                arr.append(a)
            print(arr)                 #printing array

            bubbleSort(arr)            #func calling


            print("Sorted array is:")
            for i in range(len(arr)):
                print("% d" % arr[i], end=" ")



        elif choice == 11:
            arr=[]                     #initializing array
            n=int(input("enter the length of array"))      #taking input from user in an array
            for i in range (0,n):
                a=int(input("enter the value to array"))
                arr.append(a)
            print(arr)                 #printing array

        
            insertionSort(arr)
            print('Sorted Array in Ascending Order:')
            print(arr)
        elif choice == 0:
            break
        else:
            print("Invalid choice, please choose again\n")

            
# main
security()       #userid=student password=123
    
