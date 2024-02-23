import java.util.Scanner;
public class Test_Runner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of terms: ");
        int n = sc.nextInt();
        int sum = 0;
        System.out.println("Enter a number: ");
        for(int i=0; i<n; i++){
            
            int num = sc.nextInt();
            sum += num;
        }
        double average = sum/n;
        System.out.println("The sum of " + n + " no is: " + sum);
        System.out.println("The average of " + n + " is: " + average);
        sc.close();
    }
}