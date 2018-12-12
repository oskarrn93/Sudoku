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

if __name__ == "__main__":

   grid = getGrid()
   printGrid(grid)

   print("validateRow", validateRow(grid, 0, 5)) #siffrorna är bara testfall
   print("validateRow", validateRow(grid, 2, 5))
   print("validateColumn", validateColumn(grid, 1, 3))
   print("validateColumn", validateColumn(grid, 0, 3))

