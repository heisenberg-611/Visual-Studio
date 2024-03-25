
/*The organizing committee plans to take the participants of the Olympiad on a hike after the tour. Currently, the number of tents needed to be taken is being calculated. It is known that each tent can accommodate up to 3 people.

Among the participants, there are 𝑎 introverts, 𝑏 extroverts, and 𝑐 universals:

Each introvert wants to live in a tent alone. Thus, a tent with an introvert must contain exactly one person — only the introvert himself.
Each extrovert wants to live in a tent with two others. Thus, the tent with an extrovert must contain exactly three people.
Each universal is fine with any option (living alone, with one other person, or with two others).
The organizing committee respects the wishes of each participant very much, so they want to fulfill all of them.

Tell us the minimum number of tents needed to be taken so that all participants can be accommodated according to their preferences. If it is impossible to accommodate the participants in a way that fulfills all the wishes, output −1.

Input
Each test consists of multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤104) — the number of test cases. This is followed by the descriptions of the test cases.

Each test case is described by a single line containing three integers 𝑎, 𝑏, 𝑐 (0≤𝑎,𝑏,𝑐≤109) — the number of introverts, extroverts, and universals, respectively.

Output
For each test case, output a single integer — the minimum number of tents, or −1 if it is impossible to accommodate the participants. */
package Codeforces;
import java.util.Scanner;
public class Setting_up_camp {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
            int a = in.nextInt();
            int b = in.nextInt();
            int c = in.nextInt();
            if (a + b + c == 0) {
                System.out.println(0);
                continue;
            }
            if (a + b + c == 1) {
                System.out.println(1);
                continue;
            }
            if (a + b + c == 2) {
                System.out.println(2);
                continue;
            }
            if (a + b + c == 3) {
                System.out.println(3);
                continue;
            }
        }
    }
}
