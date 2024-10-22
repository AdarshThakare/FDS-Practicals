'''Write a Python program to store first year percentage of students in array.
Write function for sorting array of floating-point numbers in ascending order using quick sort and
display top five scores.'''

print(__doc__,"\n")

def accept_array(A): 
   n = int(input("Enter the total no. of student : "))
   for i in range(n):
      x = float(input("Enter the  first year percentage of student %d : "%(i+1)))
      A.append(x)
   print("Array accepted successfully\n\n");

def display_array(A): 
   n = len(A)
   if(n == 0) :
      print("\nNo records in the database")
   else :
      print("Array of FE Marks : ",end=' ')
      for i in range(n) :
         print(f"{A[i]}",end='  ')
      print("\n")

def partition(A,s,l) : #s is pivot and l  in length of the array
   lo=s+1
   high=l
   while(high>=lo) :
      while(lo<=l and A[s] >= A[lo]) :
         lo = lo + 1
      while(A[s] <A[high]) :
         high = high - 1
      if(high>lo) :
         A[high],A[lo] = A[lo],A[high]
   A[s], A[high] = A[high],A[s]
   return high

def Quicksort(A,s,l) :
   if(s<l) :
      mid = partition(A,s,l)
      Quicksort(A,s,mid-1)
      Quicksort(A,mid+1,l)


     
def Main() :   
   A = []
   while True :
      print ("\t1 : Accept & Display the FE Marks")      
      print ("\t2 : Quick sort ascending order and display top five scores")
      print ("\t3 : Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 3):
         print ("End of Program")
         quit()
      elif (ch==1):
         A = []
         accept_array(A)
         display_array(A)
      elif (ch==2):
         print("Marks before sorting")
         display_array(A)
         n =len(A)
         Quicksort(A,0,n-1)
         print("Marks after sorting")
         display_array(A)         
         if(n >= 5) :
            print("Top Five Scores : ")
            for i in range(n-1,n-6,-1) :
               print("\t%.1f"%A[i])
         else :
            print("Top Scorers : ")
            for i in range(n-1,-1,-1) :
               print("\t%.1f"%A[i])                               
      else :
           print ("Wrong choice entered !! Try again")


Main()