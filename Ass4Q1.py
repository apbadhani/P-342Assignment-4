#importing the library
from lib import mylib as lib
#storing matrices
with open('Q1.txt', 'r') as f:
    a = [[int(num) for num in line.split()] for line in f]
with open('Q1b.txt', 'r') as f:
    b = [[int(num) for num in line.split()] for line in f]
lib.partial_pivot(a,b)
#LU decomposition
lib.lu_dec(a)
sol=lib.sub(a,b)
#printing solution
print('Solution of Q1 is',sol)

#output
Solution of Q1 is [[-7.0], [7.0], [5.0], [4.0]]

