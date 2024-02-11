import java.util.Scanner;
public class App2{
  public static void main (String [] args){
    Scanner sc = new Scanner (System.in);
    System.out.println("What is your name?");
    String a = sc.nextLine();
    System.out.println("In which Department?");
    String e = sc.nextLine();
    System.out.println("What is your age?");
    int b = sc.nextInt();
    System.out.println("What is your height?");
    float c = sc.nextFloat();
    System.out.println("Do you read in BRACU?");
    Boolean d = sc.nextBoolean();
    System.out.println("What is your CGPA?");
    float f = sc.nextFloat();
    System.out.println(a);
    System.out.println(b);
    System.out.println(c);
    System.out.println(d);
    System.out.println(e);
    System.out.println(f);
    sc.close();
  }
}