import java.util.Scanner;
public class HW1 {
    public static void main(String[] args){
        int num1, num2;
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the numbers:");
       
        num1 = sc.nextInt();
        num2 = sc.nextInt();
 
        System.out.println("Enter the operator (+,-,*,/):");
 
        //char op = sc.next().charAt(0);
        String op = sc.next();

        if(op.equals("+")){
            System.out.print("The sum of the numbers is: ");
            System.out.print(num1 + num2);
        }
        else if(op.equals("-")){
            System.out.print("The difference of the numbers is: ");
            System.out.print((num1 - num2));
        }
        else if(op.equals("*")){
            System.out.print("The product of the numbers is: ");
            System.out.print((num1 * num2));
        }
        else if(op.equals("/")){
            System.out.print("The quotient of the numbers is: ");
            System.out.print((num1 / num2));
        }
        else{
            System.out.println("Invalid operator");
        }
        sc.close();
    }
}