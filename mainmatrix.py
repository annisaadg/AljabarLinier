import modulematrix as mm
import gaussjordan as gj
 
def main():
    """
    Matrix Math Application main
    """
    # Menu
    print('\n*****Welcome to the Python Matrix Application!*****')
    selection1 = str(input('\nDo you want to use this Matrix Operation Calculator?\n'
                           'Enter Y for Yes or N for No:\n')).upper().strip()
 
    # Sentinel While loop
    while selection1 != 'N':
 
        # Answer is Y
        if selection1 == 'Y':
 
            selection = str(input('\nCHOOSE ONE! \n'
                                   'a. Two Matrix Operation\n'
                                   'b. Determinant\n'
                                   'c. Inverse Matrix\n'
                                   'd. Transpose Matrix\n'
                                   'e. SPL using OBE (Gauss-Jordan)\n'))
        
            # Invalid selection2
            while selection not in ['a', 'b', 'c', 'd', 'e']:
                print('You must enter a, b, c, d, or e. Please try again.')
                selection = str(input('CHOOSE ONE! \n'
                                   'a. Two Matrix Operation\n'
                                   'b. Determinant\n'
                                   'c. Inverse Matrix\n'
                                   'd. Transpose Matrix\n'
                                   'e. SPL using OBE\n'))
 
            # if selection is a
            if selection == 'a':
                size = int(input('\nEnter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                print('\nYour first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))
 
                print("Enter your second matrix")
                matrix2 = mm.inmatrix2(size)
                print('\nYour second ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix2))
                while True:
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
                    
                    print("Do you want to do two matrix operation again? [Y/N]")
                    selection1 = str(input()).upper().strip()
                    if(selection1 == 'Y'):
                        continue
                    else:
                        break
            # if selection is b
            elif selection == 'b':
                size = int(input('\nEnter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                print('\nYour first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))
                print("Determinant of given matrix:")
                det = mm.detmatrix(matrix1)
                print(det)
 
            # if selection is c
            elif selection == 'c':
                size = int(input('\nEnter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                det = mm.detmatrix(matrix1)
                if det == 0:
                    print("\nThere is no inverse because the determinant is 0\n")
                else :
                    print("\nThe Invers of Given Matrix is:\n")
                    print(mm.invmatrix(matrix1))
 
            # if selection is d
            elif selection == 'd':
                size = int(input('\nEnter matrix size: '))
                matrix1 = mm.inmatrix1(size)
                print('\nYour first ', size, 'x',size, ' Matrix is:\n{}\n'.format(matrix1))
                print('\nThe Transpose is:')
                print(mm.transmatrix(matrix1))
 
            
            # # if selection id e
            elif selection == 'e':
                # size = int(input('\nEnter matrix size: '))
                # coefficients = mm.inmatrix1(size)
                # print('\nEnter the right hand side matrix: ')
                # right_hand_side = mm.right_hand(1, size)
                # result = mm.gauss_jordan(coefficients, right_hand_side, 2)
                # print(result)
                row = int(input('\nEnter matrix row: '))
                col = int(input('\nEnter matrix column: '))
                matrix1 = mm.inmatrix3(row, col)
                gj.getGaussJordanMatrix(matrix1, row, col, 1)
            selection1 = str(input('\nDo you want to play the Matrix Game?\n'
                            'Enter Y for Yes or N for No:\n')).upper().strip()
            
            
    # Answer is N
    print('*****Thanks for playing the Matrix Game.*****')
    return
 
if __name__ == "__main__":
    main()