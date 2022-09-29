import numpy as np

def inmatrix1(size):
    matrix1list = np.zeros((size,size))
    print("\nEnter the matrix in the format such that each row is in\n"
            "different line and each element in a row is separated by\n"
            "a space.\n")
    for i in range(size):
        try:
            matrix1list[i] = [int(j) for j in input().split()]
            matrix1 = np.array(matrix1list).reshape(size, size)
        except ValueError:
            print('You must enter an Integer. Please try again.')
    return matrix1


def inmatrix2(size):
    matrix2list = np.zeros((size,size))
    print("\nEnter the matrix in the format such that each row is in\n"
            "different line and each element in a row is separated by\n"
            "a space.\n")
    for i in range(size):
        try:
            matrix2list[i] = [int(j) for j in input().split()]
            matrix2 = np.array(matrix2list).reshape(size, size)
        except ValueError:
            print('You must enter an Integer. Please try again.')
    return matrix2

def addmatrix(matrix1,matrix2):
    addedmatrix = matrix1 + matrix2
    return addedmatrix

def subsmatrix(matrix1,matrix2):
    submatrix = matrix1 - matrix2
    return submatrix

def multiplymatrix(matrix1,matrix2):
    multmatrix = np.matmul(matrix1, matrix2)
    return mulmatrix

def elmultiplymatrix(matrix1,matrix2):
    elmultmatrix = matrix1 * matrix2
    return elmultmatrix

def detmatrix(matrix):
    det = np.linalg.det(matrix)
    return int(det)

def transmatrix(matrix):
    return matrix.T

def invmatrix(size):
    matrix1list = np.zeros((size,size))
    for i in range(size):
        matrix1list[i] = [int(j) for j in input().split()]
        a = np.array(matrix1list).reshape(size, size)

    inv = np.zeros(shape=(len(a),len(a)))
    for i in range(0,len(inv)):
        for j in range(0,len(inv)):
            if(i==j):
                inv[i,j]=1

    for i in range(0,len(a)-1):
        if(a[i,i] == 0 and a[i+1,i] != 0):
            mat = a[i,:].copy()
            matinv = inv[i,:].copy()
            a[i,:] = a[i+1,:]
            inv[i,:] = inv[i+1,:]
            a[i+1,:] = mat
            inv[i+1,:] = matinv

    for i in range(1,len(a)):
        for j in range(0,len(a)-1):
            if(i!=j):
                if(a[i,j] != 0 and i>j):
                    inv[i,:] = inv[i,:] - a[i,j]*inv[j,:]/a[j,j]
                    a[i,:] = a[i,:] - a[i,j]*a[j,:]/a[j,j]

    for i in range(0,len(a)):
        inv[i,:] = inv[i,:]/a[i,i]
        a[i,:]=a[i,:]/a[i,i]

    for i in range(1,len(a)):
        for j in range(0,len(a)-1):
            if(i!=j):
                if(a[j,i] != 0):
                    inv[j,:] = inv[j,:] - a[j,i]*inv[i,:]/a[i,i]
                    a[j,:] = a[j,:] - a[j,i]*a[i,:]/a[i,i]

    return inv