package Class;
import java.util.Scanner;
public class sadab {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int i = s.nextInt();
        double d= s.nextDouble();s.nextLine();
        String s1 = s.nextLine();

        System.out.println("String: " + s1);
        System.out.println("Int: " + i);
        System.out.println("Double: " + d);
        s.close();
    }
}
