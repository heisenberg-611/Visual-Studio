import java.util.Scanner;

public class LAB7 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        n = sc.nextInt();
        sc.close();
        int i;
        int count = 0;
        for (i = 1; i <= n; i++) {
            if (n % i == 0) {
                count++;
            }
        }
        if(count == 2){
            System.out.println(n + " is a prime number."); 
        }
        else{
            System.out.println(n + " is not a prime number.");
        }
    }
}