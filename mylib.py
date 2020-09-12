#partial pivoting
def partial_pivot(x,b):
    n=len(x)
    for i in range(n-1):
        if x[i][i]==0:
            val=0
            for k in range(i+1,n):
                if abs(x[k][i]) > abs(x[i][i]):
                    for j in range(0,n):
                        val=x[i][j]
                        x[i][j]=x[k][j]
                        x[k][j]=val
                    if (b != 0):
                        d1 = b[i]
                        b[i] = b[k]
                        b[k] = d1
#LU decomposition
def lu_dec(a):
    n=len(a)
    for i in range(n):
        for j in range(n):
            s = 0
            if i <= j:
                for k in range(i):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = a[i][j] - s
            else:
                 for k in range(j):
                     s = s + (a[i][k] * a[k][j])
                 a[i][j] = (a[i][j] - s) / a[j][j]
#for substitution both forward and backward
def sub(A,b):
    n=len(A)
    m=len(b[0])
    y = [[0 for y in range(m)] for x in range(n)]
    x = [[0 for y in range(m)] for x in range(n)]
    for i in range(n):
        for j in range(m):
            sum=0
            for k in range(i):
                sum=sum+(A[i][k]*y[k][j])
            y[i][j]=b[i][j]-sum
    for i in range(n-1,-1,-1):
            for j in range(m):
                sum=0
                for k in range(i+1,n):
                    sum+=A[i][k]*x[k][j]
                x[i][j]=(y[i][j]-sum)/A[i][i]
    return x
def tri_ang_det(A=[]):                  #calculating determinant
    n=len(A)
    det=1
    for i in range(n):
        det=det*A[i][i]
    return det
def matmul(X = [], Y = []):                     #matrix multiplication
    Z = [[0 for y in range(len(Y[0]))]for x in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                Z[i][j]+=X[i][k]*Y[k][j]
    return Z







