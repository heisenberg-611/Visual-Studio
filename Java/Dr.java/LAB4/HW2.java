import java.util.Scanner;

public class HW2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        for(int i=0; i<10; i++)
        {
            System.out.println("Enter Number: ");
            int n = sc.nextInt();
            int x = sum+=n;
            System.out.println("Sum = "+x);
        }
        sc.close();
    }
}