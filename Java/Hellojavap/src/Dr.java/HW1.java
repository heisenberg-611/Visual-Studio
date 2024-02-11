import java.util.Scanner;
public class HW1 {
    public static void main(String[] args) { 
    
        int a, o;
        Scanner sc = new Scanner(System.in);
        System.out.println("Input a integer number: ");
        a = sc.nextInt();
        o = a % 100;
        System.out.println(o);
        sc.close();
    }
}