import java.lang.Math;
public class HW7 {
    public static void main(String[] args) {
        double a = 8, b = 3, c, area, circumference;
        area = ((Math.sqrt(3)/4)*6);
        System.out.printf("Area of the Hexagone: %.4f\n",area);
        c = (Math.sqrt(((a/2)*(a/2))+b*b));
        circumference = (a/2)*c;
        System.out.println("Circumference of the Hexagone: "+circumference);
    }
}
/*Assume a Hexagon where each of the sides are of the same length. 
From the visualization, we can see the values of a and b are given. 
Your task is to (a) draw a flowchart and (b) write a Java code to find the area and 
the circumference of the Hexagon a = 8, b=3*/
