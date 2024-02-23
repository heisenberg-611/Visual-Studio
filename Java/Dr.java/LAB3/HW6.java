import java.util.Scanner;
public class HW6 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        float num1 = sc.nextFloat();
        float num2 = sc.nextFloat();
        float num3 = sc.nextFloat();
        if(num1 > num2 && num1 > num3){
            System.out.println("Maximum number is  "+num1);
        }
        else if(num2 > num1 && num2 > num3){
            System.out.println("Maximum number is  "+num2);
        }
        else{
            System.out.println("Maximum number is  "+num3);
        }
        if(num1 < num2 && num1 < num3){
            System.out.println("Minimum number is  "+num1);
        }
        else if(num2 < num1 && num2 < num3){
            System.out.println("Minimum number is  "+num2);
        }
        else{
            System.out.println("Minimum number is  "+num3);
        }
        sc.close();
    }
}