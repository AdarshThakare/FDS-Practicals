def accept(A):
    n = int(input("enter the number of people : "))
    for i in range(n):
        name = input("Enter the name")
        phone = int(input("Enter the phone number"))
        ele = [name,phone]
        A.append(ele)
    print("Elements entered successfully.")

def display(A):
    print("PHONE RECORDS:\n")

    print("|Sr.No\t|Name\t|Mobile number")
    for i in range(len(A)):
        print(f"|{i+1}\t|{A[i][0]}\t|{A[i][1]}")

def fibonacci_search(A,key):
    f2 = 0
    f1 = 1
    f0 = f1 + f2
    n = len(A)

    while(f0 < n):
        f2 = f1
        f1 = f0
        f0 = f1 + f2
    offset = -1

    while(f0 > 0):
        i = min(offset+f2,n-1)
        if(key == A[i][0]):
            return i
        if(key > A[i][0]):
            f0 = f1
            f1 = f2
            f2 = f0 - f1
            offset = i
        if(key < A[i][0]):
            f0 = f2
            f1 = f1 - f2
            f2 = f0 - f1
    return -1

def main():
    arr=[]
    while True:
        print("\n1.Accept data.")
        print("\n2.Display data.")
        print("\n5.Fibonacci search.")
        print("\n6.Exit.")
        
        ch = int(input("\nEnter your choice : "))
        if(ch==1):
            accept(arr)
        elif(ch==2):
            display(arr)
        elif(ch==5):
            e=input("\nEnter the name to be search : ")
            index = fibonacci_search(arr,e)
            if(index==-1):
                print("\nName to be searched not found.")
            else:
                print("\nName found at ",index)
                print("\nName : ",arr[index][0])
                print("\nMobile : ",arr[index][1])
			
        elif(ch==6):
            print("\nEnd of program.")
            break
        else:
            print("\nYou entered wrong choice.")

main()
                