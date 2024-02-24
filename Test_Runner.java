import java.util.Scanner;

public class Test_Runner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter an integer:");
        String input = scanner.next();
        for (int i = 0; i < input.length(); i++) {
            System.out.print(input.charAt(i));
            if (i != input.length() - 1) {
                System.out.print(", ");
            }
        }
        scanner.close();
    }
}
