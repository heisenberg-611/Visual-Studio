import java.util.Scanner;
import java.lang.Math;

public class HW5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a integer: ");
        int n = sc.nextInt();
        int n1 = n;
        int count = 0;
        int x = 0;
        while (n > 0) {
            n = n / 10;
            count++;
        }
        x = (int) Math.pow(10, (count - 1));
        for (int i = 1; i <= count; i++) {
            System.out.print(n1/x);
            if(i != count){
                System.out.print(", ");
            }
            n1 = n1 % x;
            x = x / 10;
        }
        sc.close();
    }    
}