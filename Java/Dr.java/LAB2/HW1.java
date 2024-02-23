import java.util.Scanner;
public class HW1 {
    public static void main(String[] args) { 
    
        int a, o;
        Scanner sc = new Scanner(System.in);
        System.out.println("Input a integer number: ");
        a = sc.nextInt();
        o = a % 100;
        if(o < 0){
        System.out.println(o = -o); 
        }
        else{
        System.out.println(o);
        }
        sc.close();
        }
    }