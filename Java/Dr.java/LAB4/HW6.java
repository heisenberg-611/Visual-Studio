import java.util.Scanner;

public class HW6 {
    public static void main(String args[]) {
        int n, sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        n = sc.nextInt();
        int i;
        for (i = 1; i <= n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }
        if(sum == (n+1)){
            System.out.println(n + " is a prime number");
        }
        else{
            System.out.println(n + " is not a prime number");
        }
        if (sum == 2*n) 
        {
            System.out.println(n + " is a perfect number.");
        } 
        else 
        {
            System.out.println(n + " is not a perfect number.");
        }
        sc.close();
    }
}