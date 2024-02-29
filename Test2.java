import java.util.Scanner;

public class Test2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number;
        
        while (true) {
            System.out.print("Enter number): ");
            number = scanner.nextInt();

            if (number % 2 != 0) {
                break;
            }

            int divisorCount = countDivisors(number);
            System.out.println(number + " has " + divisorCount+" divisors");
        }
        
        scanner.close();
    }

    // Function to count the number of divisors of a given number
    public static int countDivisors(int num) {
        int count = 0;
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                count++;
            }
        }
        return count;
    }
}