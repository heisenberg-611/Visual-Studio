package BroCode.Java;

public class Class_2 {
    public static void main(String[] args) {
        String x = "Water";
        String y = "Kool";
        String temp;
        temp = x;
        x = y;
        y= temp;

        System.out.println(x);
        System.out.println(y);
    }
}
