#Problem definition:
'''In second year, computer engineering class, group A student's play cricket, group B students play
badminton and group C students play football. Write a Python program using functions to compute
following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note-While realizing the group, duplicate entries should be avoided, do not use SET built-in
functions)'''

#A = [1,2,3,4,5,8] #Cricket
#B = [1,9,4,8] #Badminton
#C = [0,2,4,6,8,9] #Football

#to input A,B and C
def inputTeam(l1):
    n = int(input(f"Enter the number of students for the current team: "))
    for i in range(n):
        student = int(input(f"Enter the jersey number of the team member {i+1} : "))
        l1.append(student)
    print(f"All the team members for the team are selected successfully now!")
    print("-----------------------")
    return l1;    

A = []
B = []
C = []

print("For Team A -")
inputTeam(A)
print("For Team B -")
inputTeam(B)
print("For Team C -")
inputTeam(C)

#a) List of students who play both cricket and badminton => A n B

def intersection(l1,l2):
    res = []
    for student in l1:
        if student in l2:
            res.append(student)
    return res

#b) List of students who play either cricket or badminton but not both => (A u B) - (A n B)

def union(l1,l2):
    res = l2.copy()
    for student in l1:
        if student not in l2:
            res.append(student)
    res.sort()
    return res

def symm_diff(l1,l2):
    res = []
    for student in union(A,B):
        if student not in intersection(A,B):
            res.append(student)
    return res

#c) Number of students who play football but neither cricket nor badminton (C - A - B)
def diff(l1,l2,l3):
    res = []
    for student in l1:
        if student not in l2:
            if student not in l3:
                res.append(student)
    return res        

#d) Number of students who play cricket and football but not badminton. (A n C - B)
d_ans = diff(intersection(A,C),B,[])

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print("-----------------")

print(f"(A u B) = {union(A,B)}")
print(f"(A n B) = {intersection(A,B)}")
print(f"(A - B) = {diff(A,B,[])}")
print(f"(B - A) = {diff(B,A,[])}")
print("-----------------")

print(f"Solution for part (a) is : {intersection(A,B)}")

print(f"Solution for part (b) is : {symm_diff(A,B)}")

print(f"solution for part (c) is : {diff(C,A,B)}")

print(f"solution for part (d) is : {d_ans}")