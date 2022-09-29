import numpy as np

def main():
    """
    Matrix Math Application main
    """
    # Menu
    print('*****Welcome to the Python Matrix Application!*****')
    selection1 = str(input('\nDo you want to use this Matrix Operation Calculator?\n'
                           'Enter Y for Yes or N for No:\n')).upper().strip()

    # Sentinel While loop
    while selection1 != 'N':

        # Answer is Y
        if selection1 == 'Y':

            selection = str(input('CHOOSE ONE! \n'
                                   'a. Two Matrix Operation\n'
                                   'b. Determinant\n'
                                   'c. Inverse Matrix\n'
                                   'd. Transpose Matrix\n'
                                   'e. Upper Triangular Matrix\n'
                                   'f. Lower Triangular Matrix\n'
                                   'g. SPL using Cofactor\n'
                                   'h. SPL using Cramer\n'
                                   'i. SPL using OBE\n'))

            # Invalid selection2
            while selection not in ['a', 'b', 'c', 'd']:
                print('You must enter a, b, c, d, e, f, g, h or i. Please try again.')
                selection = str(input('CHOOSE ONE! \n'
                                   'a. Two Matrix Operation\n'
                                   'b. Determinant\n'
                                   'c. Inverse Matrix\n'
                                   'd. Transpose Matrix\n'
                                   'e. Upper Triangular Matrix\n'
                                   'f. Lower Triangular Matrix\n'
                                   'g. SPL using Cofactor\n'
                                   'h. SPL using Cramer\n'
                                   'i. SPL using OBE\n'))

            # if selection is a
            if selection == 'a':

                # Matrix 1 Creation
                size = int(input('Enter matrix size: '))
                matrix1list = np.zeros((size,size))
                for i in range(size):
                    matrix1list[i] = [int(j) for j in input().split()]
                matrix1 = np.array(matrix1list).reshape(size, size)
                print('Your first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))

                # Matrix 2 Creation
                matrix2list = np.zeros((size,size))
                for i in range(size):
                    try:
                        matrix2list[i] = [int(j) for j in input().split()]
                        matrix2 = np.array(matrix2list).reshape(size, size)
                    except ValueError:
                        print('You must enter an Integer. Please try again.')
                print('Your first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix2))

                selection2 = str(input('Select a Matrix Operation from the list below:\n'
                                    'a. Addition\n'
                                    'b. Subtraction\n'
                                    'c. Matrix Multiplication\n'
                                    'd. Element by Element Multiplication\n')).lower().strip()

                # Invalid selection2
                while selection2 not in ['a', 'b', 'c', 'd']:
                    print('You must enter a, b, c, or d. Please try again.')
                    selection2 = str(input('Select a Matrix Operation from the list below:\n'
                                        'a. Addition\n'
                                        'b. Subtraction\n'
                                        'c. Matrix Multiplication\n'
                                        'd. Element by Element Multiplication\n')).lower().strip()

                # a is selected
                if selection2 == 'a':
                    print('\nYou selected Addition. The results are:')
                    addedmatrix = matrix1 + matrix2
                    print(addedmatrix)

                # b is selected
                elif selection2 == 'b':
                    print('\nYou selected Subtraction. The results are:')
                    submatrix = matrix1 - matrix2
                    print(submatrix)

                # c is selected
                elif selection2 == 'c':
                    print('\nYou selected Matrix Multiplication. The results are:')
                    multmatrix = np.matmul(matrix1, matrix2)
                    print(multmatrix)

                # d is selected
                elif selection2 == 'd':
                    print('\nYou selected Element by Element Multiplication. The results are:')
                    elmultmatrix = matrix1 * matrix2
                    print(elmultmatrix)

            elif selection == 'b':

                # Get the shape of the matrix.
                n = int(input("Enter the no of columns of the square matrix:\n").strip())

                # Get the square matrix from user.
                matrix = np.zeros((n,n))
                print("\nEnter the matrix in the format such that each row is in\n"
                    "different line and each element in a row is separated by\n"
                    "a space.\n")
                for i in range(n):
                    matrix[i] = [int(j) for j in input().split()]

                # calculating the determinant of matrix
                det = np.linalg.det(matrix)
  
                print("\nDeterminant of given matrix:")
                print(int(det))

            elif selection == 'c':
                size = int(input('Enter matrix size: '))
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

                print("The Invers of Given Matrix is:\n")
                print(inv)
            
            elif selection == 'd':
                size = int(input('Enter matrix size: '))
                matrix = np.zeros((size,size))
                for i in range(size):
                    matrix[i] = [int(j) for j in input().split()]
                matrixx = np.array(matrix).reshape(size, size)
                print('\nThe Transpose is:')
                print(matrixx.T)


            selection1 = str(input('\nDo you want to play the Matrix Game?\n'
                            'Enter Y for Yes or N for No:\n')).upper().strip()

        # Answer is Invalid (y/n)
        else:
            print('You must enter Y or N. Please try again.')
            selection1 = str(input('\nDo you want to play the Matrix Game?\n'
                                   'Enter Y for Yes or N for No:\n')).upper().strip()

    # Answer is N
    print('*****Thanks for playing the Matrix Game.*****')
    return

if __name__ == "__main__":
    main()
