import java.util.Scanner;
public class A1{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int maxRow = 0;
        int maxCol = 0;
        int indxMaxRow = 0;
        int indxMaxCol = 0;
        // int matrix [][] = new int[2][2];
        int [][] matrix = { 
            { 1, 2}, 
            { 3, 4},
            { 5, 6 }
        };
        for (int i = matrix.length - 1; i >= 0; i--) {
            for (int j = matrix[i].length - 1; j >= 0; j--) {
                System.out.println(matrix[i][j] + " ");
                System.out.println();
            }
        }
        // System.out.println("Enter "+matrix.length+" rows and "+ matrix[0].length+ " columns");
        // for (int[] row : matrix) {
        //     for (int column = 0; column < matrix.length; column++) {
        //         row[column] = sc.nextInt();
        //     }
        // }
        // for (int[] matrix1 : matrix) {
        //     for (int column = 0; column < matrix.length; column++) {
        //         System.out.print(matrix1[column] + " ");
        //     }
        // }
        // int total = 0;
        // for (int[] row : matrix) {
        //     for (int column = 0; column < matrix.length; column++) {
        //         total += row[column];
        //     }
        // }
        // System.out.println(total);
        // for(int col = 0; col<matrix[0].length;col++){
        //     maxRow += matrix[0][col];
        // }
        // System.out.println(matrix[1].length);
        // for (int row = 1; row < matrix.length; row++){
        //     int totalOfRow = 0;
        //     for (int col = 0; col < matrix[row].length; col++) {
        //         totalOfRow += matrix[row][col];
        //     }
        //     if(totalOfRow > maxRow){
        //         maxRow = totalOfRow;
        //         indxMaxRow = row;
        //     }
        // }
        // System.out.println(indxMaxRow);
        // System.out.println(maxRow);
    } 
}