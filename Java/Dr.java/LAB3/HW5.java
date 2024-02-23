import java.util.Scanner;
public class HW5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the payment:");
        int payment = sc.nextInt();
        System.out.println("Enter the age:");
        int age = sc.nextInt();
        if(payment < 10000){
            System.out.println("Your tax amounts is 0 Tk");
        }
        else if(age < 18){
            System.out.println("Your tax amounts is 0 Tk");
        }
        else if(payment >= 10000 && payment <= 20000){
            int tax1 = payment*5/100;
            System.out.println("Your tax amounts is "+tax1+" Tk");
        }
        else if(payment > 20000){
            int tax2 = payment*10/100;
            System.out.println("Your tax amounts is "+tax2+" Tk");
        }
        sc.close();
    }
}
    
