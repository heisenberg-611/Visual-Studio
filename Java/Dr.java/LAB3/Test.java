/*public class Test {

    public static double calculateSeriesSum(int n) {
        double sum = 0.0;
        for (int i = 1; i <= n; i++) {
            sum += 1.0 / i;
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 10; // You can change the value of n as per your requirement
        double seriesSum = calculateSeriesSum(n);
        System.out.println("Sum of the series up to " + n + " numbers: " + seriesSum);
    }
}
*/
public class Test {

    public static int calculateSeriesSum(int n) {
        int sum = 0;
        int currentSum = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                currentSum += j;
            }
            sum += currentSum;
            currentSum = 0; // Reset current sum for the next iteration
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 5; // You can change the value of n as per your requirement
        int seriesSum = calculateSeriesSum(n);
        System.out.println("Sum of the series up to " + n + "th element: " + seriesSum);
    }
}
