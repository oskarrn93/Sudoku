import java.util.Random; 

class Sudoku {
   public static void main(String[] args) {
      System.out.println("hello world");

      int[][] board = generateBoard();
      printboard(board);
   }

   private static int[][] generateBoard() {
      return generateBoard(9, 9);
   }

   private static int[][] generateBoard(int rows, int cols) {
      int[][] board = new int[rows][cols];

      for(int a = 0; a < rows; a++) {
         for(int b = 0; b < cols; b++) {
            board[a][b] = generateRandomNumber();
         }
      }

      return board;
   }

   private static int generateRandomNumber() {
      return generateRandomNumber(0, 9); //0 means the cell is not set
   }

   private static int generateRandomNumber(int min, int max) {
      Random random = new Random(); //TODO: fix so the random variable is not initialized on each call
      return (random.nextInt(max) + min);
   }

   private static void printboard(int[][] board) {
      int rows = board.length;
      int cols = board[0].length; //TODO: this might not always exists
      System.out.println();

      for(int a = 0; a < rows; a++) {
         for(int b = 0; b < cols; b++) {
            System.out.print(board[a][b]);
            System.out.print(" ");
         }
         System.out.println();
      }    
   }
}