import java.util.Random; 

class Sudoku {
   static Random random = new Random();

   public static void main(String[] args) {
      System.out.println("hello world");

      int[][] board = generateBoard();
      printBoard(board); 
   }

   private static int[][] generateBoard() {
      return generateBoard(9, 9);
   }

   private static int[][] generateBoard(int rows, int cols) {
      int[][] board = new int[rows][cols];

      int value = 0;
      for(int a = 0; a < rows; a++) {
         for(int b = 0; b < cols; b++) {
            
            //60% chance to use a random number, i.e. fill the board
            if((random.nextInt(10)+1) <= 6) {
               value = generateRandomNumber();
            }
            else {
               value = 0;
            }
           
            board[a][b] = value;
         }
      }

      return board;
   }

   private static int generateRandomNumber() {
      return generateRandomNumber(0, 9); //0 means the cell is not set
   }

   private static int generateRandomNumber(int min, int max) {
      return (random.nextInt(max) + min);
   }

   private static void printBoard(int[][] board) {
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