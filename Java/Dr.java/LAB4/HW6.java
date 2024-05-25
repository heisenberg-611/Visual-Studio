import java.util.Scanner;

public class HW6 {
    public static void main(String[] args) {
        int n, sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        n = sc.nextInt();
        sc.close();
        int i=0;
        for (i = 1; i < n; i++) {
            if (n % i == 0) {
                sum = sum+i;
            }
        }
        System.out.println(sum);
        if (sum == n) 
        {
            System.out.println(n + " is a perfect number.");
        } 
        else 
        {
            System.out.println(n + " is not a perfect number.");
        } 
    }
}