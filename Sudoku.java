  
class Sudoku {
   public static void main(String[] args) {
      System.out.println("hello world");

      int[][] board = generateBoard();
   }

   private static int[][] generateBoard() {
      return generateBoard(9, 9);
   }

   private static int[][] generateBoard(int rows, int cols) {
      int[][] board = new int[rows][cols];

      for(int a = 0; a < rows; a++) {
         for(int b = 0; b < cols; b++) {
            board[a][b] = 0;
         }
      }

      return board;
   }

}