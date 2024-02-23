/*write a Java program that displays the sum of n odd natural numbers.
Sample Input:
Input number of terms: 5
Expected Output:
The odd numbers are: 1
3
5
7
9
The Sum of odd Natural Numbers up to 5 terms is: 25 */
 import java.util.Scanner;
 public class Test {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         System.out.print("Input number of terms: ");
         int n = sc.nextInt();
         int sum = 0;
         System.out.println("The odd numbers are: ");
         for(int i=1; i<=n; i++) {
             int oddNum = 2*i-1;
             System.out.println(oddNum);
             sum += oddNum;
         }
         System.out.println("The Sum of odd Natural Numbers up to " + n + " terms is: " + sum);
         sc.close();
     }
 }