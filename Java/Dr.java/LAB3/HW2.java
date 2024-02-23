import java.util.Scanner;
public class HW2 {
    public static void main(String[] args){
        int num;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number:");
        num = sc.nextInt();
        if(num % 5 == 0)
        {
            if(num % 7 == 0)
            {  
                System.out.println("Divisible by Both");
            }
            else
            {
                System.out.println("Invalid: Divisible by 5 Only");
            }
        }
        else if(num % 7 == 0){
            System.out.println("Invalid: Divisible by 7 Only");
        }
        else{
            System.out.println("No");
        }
        sc.close();
    }
}