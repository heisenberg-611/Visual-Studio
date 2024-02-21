import java.util.Scanner;
public class HW4 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the student ID:");
        int id = sc.nextInt();
        int year = id/1000000;
        int session = id%1000000;
        int session1 = session/100000;
        if(session1 == 1){
            System.out.println("Student Joined BRAC in Spring "+year);
        }
        else if(session1 == 2){
            System.out.println("Student Joined BRAC in Fall "+year);
        }
        else if(session1 == 3){
            System.out.println("Student Joined BRAC in Summer "+year);
        }
        else{
            System.out.println("Invalid ID");
        }
        sc.close();
    }
}