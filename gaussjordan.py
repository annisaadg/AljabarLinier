from random import randint

def createMatrix(row,col,a,b):
  """
  Function description: Create and populate a matrix
  Parameters:
  row - Number of rows
  col  - Number of cols
  a    - Lower limit to randomize
  b    - upper limit to randomize
  Returns: 
  """
  if row <= 0 or col <= 0:
    print ("must have at least one row")
    Matrix = [None]
  else:
    Matrix = [None] * row
    for i in range(row):
      Matrix[i] = [None] * col
    for i in range(row):
      for j in range(col):
        Matrix[i][j] = randint(a,b)
  return Matrix

def printMatrix(Matrix):
  """
  Function description:
  Parameters:
  Returns:
  """
  for i in range(len(Matrix)):
    print(Matrix[i])

def swap(Matrix, row,piv):
  """
  Function description:
  Parameters:
  Returns:
  """
  temp = Matrix[piv]
  if piv == (row-1):
    print("It can't be done")
  else:
    Matrix[piv] = Matrix[piv+1]
    Matrix[piv+1] = temp
    doOne(Matrix,piv,Matrix[piv][piv],row+1)
    doZero(Matrix,piv,row,row+1)

def doOne(Matrix,piv, a,col):
  """
  Function description:
  Parameters:
  Returns:
  """
  if a != 0:
    for j in range(col):
      Matrix[piv][j] = Matrix[piv][j]/a
  else:
    print ("Can't divide by zero")
    swap(Matrix,col-1,piv)

def doZero(Matrix, piv, row,col):
  """
  Function description:
  Parameters:
  Returns:
  """
  for i in range(row):
      if (i!=piv):
          b = Matrix[i][piv]
          for j in range(col):
              Matrix[i][j] = Matrix[i][j]-b*Matrix[piv][j]

def testMatrix(Matrix, row,col):
  """
  Function description:
  Parameters:
  Returns:
  """
  ban = True
  if (row + 1) == col:
    for i in range(row):
      for j in range(col):
          if i==j and Matrix[i][j] == 0:
              ban = False
  else:
    ban = False

  return ban

def getGaussJordanMatrix(Matrix, row, col, debug):
  """
  Function description:
  Parameters:
  row - Number of rows
  col  - Number of cols
  Returns:
  """
  for i in range(row):
    for j in range(col):
        if i == j:
            a = Matrix[i][j]
            doOne(Matrix,i,a,col)
            doZero(Matrix,i,row,col)
            if debug == 1:
              print("Pivot one, zeros up and down")
              printMatrix(Matrix)

def main():
  row = 3
  col = row+1
  a = -9
  b = 9
  #Matrix = createMatrix(row,col,a,b)
  #Matrix = [[2,2,4,6],[7,9,0,4],[1,2,0,3]] #Matrix inconscistente!!
  #Matrix = [[3,2,4,6],[7,0,3,4],[1,2,2,3]] #Matrix inconscistente!!
  #Matrix = [[0,2,0,3],[7,0,2,8],[6,3,8,9]] #Matrix inconscistente!!
  Matrix = [[1,2,3,6],[2,2,2,6],[2,4,6,12]]
  print ("Matrix original")
  printMatrix(Matrix)

  isCandidateMatrix = testMatrix(Matrix,row,col)

  if isCandidateMatrix:
    getGaussJordanMatrix(Matrix, row, col, 1)
  
    print ("Matrix final")
    printMatrix(Matrix)
  else:
    print("It is not possible to apply the Gauss-Jordan method for the introduced Matrix")
    
if __name__ == "__main__":
  main()