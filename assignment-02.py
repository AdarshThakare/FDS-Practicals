'''Write a Python program to store marks scored in subject “Fundamental of
Data Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency'''

print(__doc__)
print("--------------------\n")

marksheet = []

n = int(input("Enter the number of students in the class : "))
m = int(input("Enter the total marks that can be obtained for FDS : "))

def inputStudents(l1):
    print("NOTE - Give -1 marks if the student is absent")
    student = 0
    for student in range(n):
        marks = int(input(f"Enter the marks of student {student + 1} in FDS : "))
        if(marks > m):
            print(f"Error : Enter the marks less than {m}")
            break
        l1.append(marks)

inputStudents(marksheet)

# A = [23,30,-1,26,10,-1,14]
# n = 7
# m = 40

#a) The average score of class
  
def avg_score(l1):
    sum = 0
    num = 0
    count = 0
    for i in l1:
        if(i != -1):
            sum += i
            count += 1
        num += 1
    
    print(f"Aggregate is : {sum/count}")
    print(f"Average is : {sum/num}")

print("----------------------")
print("Answer for part (a) is -")
avg_score(marksheet)

print("----------------------")
#b) Highest score and lowest score of class

def minmax(li):
    min = m+1
    max = -1
    for i in range(n):
        if(li[i] != (-1)):
            if(li[i] <= min):
                min = li[i]
                mindx = i
            if(li[i] >= max):
                max = li[i]
                maxdx = i
    print(f"Highest score is {max} which is attained by student {maxdx+1}")
    print(f"Lowest score is {min} which is attained by student {mindx+1}")

print("Answer for part (b) is -")

minmax(marksheet)
print("----------------------")

# c) Count of students who were absent for the test
def absentee(li):
    count = 0
    for i in li:
        if(i == -1):
            count+=1
    print(f"The number of absent sudents are : {count}")

print("Answer for part (c) is -")

absentee(marksheet)
print("----------------------")

#d) Display mark with highest frequency
def highest_freq(li):
    freq = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if(li[i] == li[j]):
                count += 1
        freq = max(freq,count)
    print(f"The modal marks are {li[freq]} attained by {freq} students")    


print("Answer for part (d) is -")

highest_freq(marksheet)
print("----------------------")