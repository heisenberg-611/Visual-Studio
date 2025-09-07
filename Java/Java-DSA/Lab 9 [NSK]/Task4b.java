public class Task4b {
    public static void main(String[] args) {
        int v = 8;
        int[][] dMatrix = {
            {0,4,2,5,1,0,0,6}, 
            {4,0,3,2,0,6,4,2},
            {2,3,0,0,4,1,3,7},
            {5,2,0,0,7,0,2,3},
            {1,0,4,7,0,3,5,1},
            {0,6,1,0,3,0,2,4},
            {0,4,3,2,5,2,0,5},
            {0,1,2,3,4,5,6,7}
        };
        int[][] n = new int[v][v];
        int[][] w   = new int[v][v];
        int[] c = new int[v];
        for (int i = 0; i < v; i++) {
            for (int j = 0; j < v; j++) {
                n[i][j] = -1;
                w[i][j] = 0;
            }
            c[i] = 0;
        }
        for (int i = 0; i < v; i++) {
            for (int j = i + 1; j < v; j++) {
                int wt = Math.max(dMatrix[i][j], dMatrix[j][i]);
                if (wt > 0) {
                    n[i][c[i]] = j;
                    w[i][c[i]] = wt;
                    c[i]++;
                    n[j][c[j]] = i;
                    w[j][c[j]] = wt;
                    c[j]++;
                }
            }
        }
        System.out.println("Converted List: ");
        for (int i = 0; i < v; i++) {
            System.out.print(i + ": ");
            for (int k = 0; k < c[i]; k++) {
                System.out.print("(" + n[i][k] + "," + w[i][k] + ") ");
            }
            System.out.println();
        }
    }
}
