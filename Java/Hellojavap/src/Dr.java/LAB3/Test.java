/*Draw a flowchart and then write a calculator program in Java that takes
 two integers and an op (+, -, *, /) as input and performs the corresponding
calculation.
Please use the equals( ) method for string comparison. 
import java.util.Scanner;
public class Test {
   public static void main(String[] args)
    {
        int num1, num2;
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the numbers:");

        num1 = sc.nextInt();
        num2 = sc.nextInt();sc.nextLine();

        System.out.println("Enter the op (+,-,*,/):");

        String op = sc.nextLine();

        if(op.equals("+")){
            System.out.println("The sum of the numbers is:");
            System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
        }
        else if(op == "-"){
            System.out.println("The difference of the numbers is:");
            System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
        }
        else if(op == "*"){
            System.out.println("The product of the numbers is:");
            System.out.println(num1 + " * " + num2 + " = " + (num1 * num2));
        }
        else{
         System.out.println("The quotient of the numbers is:");
            System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
            sc.close();
        }
      }
   }*/
   // hw - 06
/*import java.util.Scanner;
public class Test{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float num1 = sc.nextFloat();
        float num2 = sc.nextFloat();
        float num3 = sc.nextFloat();
        float max, min;
        if((num1 > num2) && (num1 > num3)){
            max = num1;
            if(num2 > num3){
                min = num3;
            }
            else{
                min = num2;
            }
        }
        else if(num2 > num3){
            max = num2;
            if(num1 > num3){
                min = num3;
            }
            else{
                min = num1;
            }
        }
        else{
            max = num3;
            if(num1 > num2){
                min = num2;
            }
            else{
                min = num1;
            }
        }
        sc.close();
        
        System.out.printf("Maximum number is %.2f\n", max);
        System.out.printf("Minimum number is %.2f\n", min);

    }
}
        */
        import java.util.Scanner;
        public class Test{
          public static void main(String[]args){
            Scanner sc = new Scanner (System.in);
            System.out.println("Enter your numbers");
            float a= sc.nextFloat();
            float b= sc.nextFloat();
            float c= sc.nextFloat();
            if(a>b && a>c && c<b){
              System.out.println("Maximum number is " +a);
              System.out.println("Minimum number is " +c);
            }
            else if(b>a && b>c && a<c){
              System.out.println("Maximum number is " +b);
              System.out.println("Minimum number is " +a);
            }
            else {
              System.out.println("Maximum number is " +c);
              System.out.println("Minimum number is " +b);
            }
            sc.close();
          }
        }    