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

if __name__ == "__main__":

   grid = getGrid()
   print("grid", grid)
