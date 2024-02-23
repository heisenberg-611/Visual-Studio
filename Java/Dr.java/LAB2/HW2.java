import java.util.Scanner;
public class HW2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double n1,n2;
        System.out.println("Enter a number in inch: ");
        n1 = sc.nextDouble();
        n2 = n1*0.0254;
        System.out.println(n2);
        sc.close();
    }
}