
# Addition of Two Matrices

from numpy import *

A = array([[2, 4], [5, -6]])
B = array([[9, -3], [3, 6]])
C = A + B      # element wise addition
print("Addition:\n",C)


# Multiplication of Two Matrices


A = array([[3, 6, 7], [5, -3, 0]])
B = array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print("Multiplication:\n",C)


# Adding a row

print("\nAdding a row\n")

m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m_r = append(m,[['Avg',12,15,13,11]],0)

print(m_r,"\n")

# adding a column

print("adding a column\n")

m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)

print(m_c,"\n")

# Update a row in in a Matrix
print("Update a row in in a Matrix")

m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m[3] = ['Thu',0,0,0,0]


print(m,"\n")
