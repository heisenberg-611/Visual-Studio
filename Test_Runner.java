import java.util.Scanner;

public class Test_Runner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the starting number:");
        int start = scanner.nextInt();
        System.out.println("Enter the ending number:");
        int end = scanner.nextInt();
        System.out.println("Enter the divisor:");
        int divisor = scanner.nextInt();

        for (int i = start; i <= end; i++) {
            int product = 1;
            int number = i;
            while (number != 0) {
                product *= number % 10;
                number /= 10;
            }
            if (product % divisor == 0) {
                System.out.println(product);
            }
        }
        scanner.close();
    }
}
