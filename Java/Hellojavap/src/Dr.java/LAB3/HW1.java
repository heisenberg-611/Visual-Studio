import java.util.Scanner;
public class HW1 {
    public static void main(String[] args)
    {
        double num1, num2;
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the numbers:");
       
        num1 = sc.nextDouble();
        num2 = sc.nextDouble();
 
        System.out.println("Enter the operator (+,-,*,/):");
 
        char operator = sc.next().charAt(0);

        if(operator == '+'){
            System.out.println("The sum of the numbers is:");
            System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
        }
        else if(operator == '-'){
            System.out.println("The difference of the numbers is:");
            System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
        }
        else if(operator == '*'){
            System.out.println("The product of the numbers is:");
            System.out.println(num1 + " * " + num2 + " = " + (num1 * num2));
        }
        else if(operator == '/'){
            System.out.println("The quotient of the numbers is:");
            System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
        }
        else{
            System.out.println("Invalid operator");
        }
        sc.close();
    }
}