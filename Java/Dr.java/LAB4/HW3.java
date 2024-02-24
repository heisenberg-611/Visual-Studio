import java.util.Scanner;
public class HW3 {
    public static void main(String[] args) {
            System.out.println("Enter a positive integer: ");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            for(int i=1; i<=n; i++){
                if(i%5==0 && i%3!=0){
                System.out.println(i);
            }
        }
        sc.close();
    }
}