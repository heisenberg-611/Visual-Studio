import java.util.Scanner;
class HW3{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int radius = 4;
    double Circumference, Area;
    Circumference = 2 * 3.1416 * radius;
    Area = 3.1416 * radius * radius;
    System.out.println("Circumference is "+Circumference+" and area is "+Area);
    sc.close();
  }
}