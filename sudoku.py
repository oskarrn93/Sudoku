# -*- coding: utf-8 -*-

DEBUG = True
#DEBUG = False

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

if __name__ == "__main__":

   grid = getGrid()
   printGrid(grid)

   if DEBUG:
      print("validateRow", validateRow(grid, 0, 5)) #siffrorna är bara testfall
      print("validateRow", validateRow(grid, 2, 5))
      print("validateColumn", validateColumn(grid, 1, 3))
      print("validateColumn", validateColumn(grid, 0, 3))
      print("validateSubGrid", validateSubGrid(grid, 0, 0, 6))
      print("validateSubGrid", validateSubGrid(grid, 0, 0, 1))

      print("validateValue", validateValue(grid, 0, 0, 1))
      print("validateValue", validateValue(grid, 0, 0, 6))

