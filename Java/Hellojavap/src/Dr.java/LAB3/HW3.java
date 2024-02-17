import java.util.Scanner;
import java.lang.Math;
public class HW3 {
    public static void main(String[] args){
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number:");
        n = sc.nextInt();
        if(n<0){
                System.out.println("Output: "+2*n);
        }
        else if(0 <= n && n < 2){
                System.out.println("Output: "+(n+1));
        }
        else if(2 <= n && n < 5){
            System.out.println("Output: "+((n*n)-1));
        }
        else if(n>=5){
            double a = ((3*(Math.pow(n ,2))+2));
            int b = (int) a;
            System.out.printf("Output: "+b);
        }
        sc.close();
    }
}