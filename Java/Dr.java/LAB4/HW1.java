import java.util.Scanner;
public class HW1 {
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input the number of terms: ");
        int n = sc.nextInt();
        int sum = 0;
        System.out.println("The odd numbers are: ");
        for(int i=1; i<=n; i++){
                int oddn=2*i-1;
                System.out.println(oddn);
                sum += oddn;
        }
        System.out.println("The sum of odd numbers up to " + n + " terms is: " + sum);
        sc.close();
    }
}