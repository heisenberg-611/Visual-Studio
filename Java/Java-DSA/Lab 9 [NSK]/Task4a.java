public class Task4a {
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
    int[][] uMatrix = new int[v][v];
    for (int i = 0; i < v; i++) {
      for (int j = i + 1; j < v; j++) {
        int w = Math.max(dMatrix[i][j], dMatrix[j][i]);
        if (w > 0) {
          uMatrix[i][j] = w;
          uMatrix[j][i] = w;
        }
      }
    }
    System.out.println("Converted Matrix: ");
    for (int i = 0; i < v; i++) {
      for (int j = 0; j < v; j++) {
        System.out.print(uMatrix[i][j] + " ");
      }
      System.out.println();
    }
  }
}
