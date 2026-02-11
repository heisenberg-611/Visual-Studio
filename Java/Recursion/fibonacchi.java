/**
 *    author:  kabir_singh
 *    created: 2025.12.09 23:35:48
 **/
import java.io.*;
import java.util.*;

public class fibonacchi{
    static int[] dp;
    public static int fib( int n) {
        if(n<=1){
            return n;
        }
        if(dp[n] != -1) return dp[n]; 
        dp[n] = fib(n-1)+fib(n-2);
        return dp[n];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n+1];
        Arrays.fill(dp, -1);
        System.out.println(fib(n));
    }
}