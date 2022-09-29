import numpy as np
import modulematrix as mm


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
            while selection not in ['a', 'b', 'c', 'd', 'e']:
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
                size = int(input('Enter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                print('Your first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))

                print("Enter your second matrix\n")
                matrix2 = mm.inmatrix2(size)
                print('Your first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix2))

                # operation for selection a
                selection2 = str(input('Select a Matrix Operation from the list below:\n'
                            'a. Addition\n'
                            'b. Subtraction\n'
                            'c. Matrix Multiplication\n'
                            'd. Element by Element Multiplication\n')).lower().strip()
                
                while selection2 not in ['a', 'b', 'c', 'd']:
                    print('You must enter a, b, c, or d. Please try again.')
                    selection2 = str(input('Select a Matrix Operation from the list below:\n'
                                        'a. Addition\n'
                                        'b. Subtraction\n'
                                        'c. Matrix Multiplication\n'
                                        'd. Element by Element Multiplication\n')).lower().strip()
                
                # if selection2 is a
                if selection2 == 'a':
                    print('\nYou selected Addition. The results are:')
                    addition = mm.addmatrix(matrix1,matrix2)
                    print(addition)

                # if selection2 is b
                elif selection2 == 'b':
                    print('\nYou selected Subtraction. The results are:')
                    substraction = mm.subsmatrix(matrix1,matrix2)
                    print(substraction)

                # if selection2 is c
                elif selection2 == 'c':
                    print('\nYou selected Matrix Multiplication. The results are:')
                    mul = mm.multiplymatrix(matrix1,matrix2)
                    print(mul)

                # if selection2 is d
                elif selection2 == 'd':
                    print('\nYou selected Element by Element Multiplication. The results are:')
                    elmul = mm.elmultiplymatrix(matrix1,matrix2)
                    print(elmul)


            # if selection is b
            elif selection == 'b':
                size = int(input('Enter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                print('Your first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))
                print("\nDeterminant of given matrix:")
                det = mm.detmatrix(matrix1)
                print(det)


            # if selection is c
            elif selection == 'c':
                size = int(input('Enter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                det = mm.detmatrix(matrix1)
                if det == 0:
                    print("There is no inverse because the determinant is 0\n")
                else :
                    print("\nEnter the matrix in the format such that each row is in\n"
                        "different line and each element in a row is separated by\n"
                        "a space.\n")
                    print("The Invers of Given Matrix is:\n")
                    print(mm.invmatrix(size))


            # if selection is d
            elif selection == 'd':
                size = int(input('Enter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                print('Your first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))
                print('\nThe Transpose is:')
                print(mm.transmatrix(matrix1))

            
            # if selection id e


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
