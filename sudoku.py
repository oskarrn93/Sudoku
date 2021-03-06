# -*- coding: utf-8 -*-

#DEBUG = True
DEBUG = False

def getGrid():
   #https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1200px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png
   grid = [
      [5,3,0,0,7,0,0,0,0], 
      [6,0,0,1,9,5,0,0,0], 
      [0,9,8,0,0,0,0,6,0], 
      [8,0,0,0,6,0,0,0,3], 
      [4,0,0,8,0,3,0,0,1], 
      [7,0,0,0,2,0,0,0,6], 
      [0,6,0,0,0,0,2,8,0], 
      [0,0,0,4,1,9,0,0,5], 
      [0,0,0,0,8,0,0,7,9]
   ] 
   return grid

def printGrid(grid):
   for x in range(0, len(grid)):
      print("".join(str(grid[x])))

def getRow(grid, row):
   result = list()

   #hämta ut värdena från raden
   for x in range(9):
      result.append(grid[row][x])

   if DEBUG: print("getRow", result)
   return result

def getColumn(grid, col):
   result = list()

   #hämta ut värdena från kolumnen
   for x in range(9):
      result.append(grid[x][col])

   if DEBUG: print("getColumn", result)
   return result

def validateRow(grid, row, value):
   rowValues = getRow(grid, row)
   #kolla så att value inte matchar något värde som redan finns i samma rad
   if(value in rowValues): 
      return False
   return True

def validateColumn(grid, col, value):
   colValues = getColumn(grid, col)
   #kolla så att value inte matchar något värde som redan i samma kolumn
   if(value in colValues): 
      return False
   return True

def getSubGrid(grid, row, col):
   subGridRowStart = 3 * (row//3) # // är floor division (avrunda neråt till heltal)
   subGridColStart = 3 * (col//3)

   #instansiera subgrid
   subGrid = []
   #subgrid är 3x3 eftersom hela griden är 9x9
   for a in range(0, 3):
      tmpList = list()
      for b in range(0, 3):
         tmpList.append(grid[a+subGridRowStart][b+subGridColStart])
      subGrid.append(tmpList)

   return subGrid

def validateSubGrid(grid, row, col, value):
   subGrid = getSubGrid(grid, row, col)
   subGridValues = list()

   #hämta ut värdena ur subgriden
   for x in range(3):
      for y in range(3):
         subGridValues.append(subGrid[x][y]) 

   if DEBUG: 
      print("subGrid", subGrid)
      print("value", value)
      print("subGridValues", subGridValues)

   #kolla om siffran redan finns i subgrid
   if value in subGridValues:
      return False;
      
   return True;

def validateValue(grid, row, col, value):
   if not validateRow(grid, row, value) or not validateColumn(grid, col, value) or not validateSubGrid(grid, row, col, value):
      return False
   return True

def validateSolution(grid):

   #då det är en 9x9 matris så räcker det att iterera över en sida
   for x in range(9):
      row = getRow(grid, x) #hämta ut rad
      col = getColumn(grid, x) #hämta ut kolumn

      """
      genom att använda set() så tar den bort eventuella dubletter
      så genom att kolla längden på listan (row och column) och längden på set() utav samma lista
      och om dessa är lika långa så finns det inga dubletter
      """

      lenRow = len(row)
      lenRowSet = len(set(row))

      lenCol = len(col)
      lenColSet = len(set(col))

      if DEBUG: 
         print("lenRow:", lenRow)
         print("lenRowSet", lenRowSet)

         print("lenCol:", lenCol)
         print("lenColSet", lenColSet)

      if lenRow is not lenRowSet: 
         if DEBUG: print("ERROR: row length differs")
         return False;

      if lenCol is not lenColSet: 
         if DEBUG: ("ERROR: col length differs")
         return False;

      #allt ok
      return True

def findNextEmptyCell(grid, row, col):
   #leta efter nästa tomma cell   
   for x in range(9):
      for y in range(9):
         if grid[x][y] is 0:
            return x, y

   #om det inte finns någon cell kvar att fylla
   return -1, -1

def solve(grid, row=0, col=0):
   if DEBUG: print("solve")

   row, col = findNextEmptyCell(grid, row, col)

   if DEBUG: 
      print("row", row)
      print("col", col)

   #finns inga fler celler att fylla i, så vi är klara
   if row is -1 and col is -1:
      return True

   #testa med siffrorna 1 till och med 9 att sätta in i cellen
   for value in range(1, 10):
      if validateValue(grid, row, col, value) is True:
         grid[row][col] = value #värdet verkar fungera
         if solve(grid, row, col) is True: #rekursivt fortsätt lösa
            return True
         
         grid[row][col] = 0 #ingen lösning så sätt cell till 0 och testa med nästa vörde i loopen
   
   """
   return False är backtrack om inget värde i loopen lyckades, så går man uppåt/tillbaka 
   i rekursionen och fortsätter testa med ett nytt värde om det är en lösning, dvs en typ utav brute force
   """
   return False

if __name__ == "__main__":

   grid = getGrid()
   printGrid(grid)

   if DEBUG:
      print("validateRow:", validateRow(grid, 0, 5)) #siffrorna är bara testfall
      print("validateRow:", validateRow(grid, 2, 5))
      print("validateColumn:", validateColumn(grid, 1, 3))
      print("validateColumn:", validateColumn(grid, 0, 3))
      print("validateSubGrid:", validateSubGrid(grid, 0, 0, 6))
      print("validateSubGrid:", validateSubGrid(grid, 0, 0, 1))

      print("validateValue:", validateValue(grid, 0, 0, 1))
      print("validateValue:", validateValue(grid, 0, 0, 6))

   result = solve(grid) 

   if DEBUG:
      print("solve result:", result)

   if result is True:
      print("\nSuccess! A solution was found.")
      printGrid(grid)

      result = validateSolution(grid)
      if result is True:
         print("\nThe Solution is valid!")
      else:
         print("\nThe Solution is NOT valid!")
         print("\nNo solution was found :(")
   else:
      print("\nNo solution was found :(")

