/*Write a Java code that asks an integer as input from the user and takes that 
many integer inputs. Your task is to count how many numbers are non-negative and 
negative. */
import java.util.Scanner;
public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of terms: ");
        int n = sc.nextInt();
        int negative = 0;
        int nonNegative = 0;
        for(int i=0; i<n; i++){
            System.out.println("Enter a number: ");
            int num = sc.nextInt();
            if(num<0){
                negative++;
            }
            else{
                nonNegative++;
            }
        }
        System.out.println("The number of negative numbers is: " + negative);
        System.out.println("The number of non-negative numbers is: " + nonNegative);
        sc.close();
    }
}
 