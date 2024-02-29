import java.util.Scanner;

public class  Test_Runner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("The value of N: ");
        int N = scanner.nextInt();
        scanner.close();
        int sum = 0;
        int y = 0;
        for (int i = 1; i <= N; i++) {
            sum += i; // Calculate the sum of the series 1+2+3+...+N
            y -= sum; // Add the negative sum to y
        }
        System.out.println("The value of y: " + y);
    }
}