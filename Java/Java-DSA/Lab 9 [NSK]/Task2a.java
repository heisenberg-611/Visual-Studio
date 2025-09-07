public class Task2a {
  public static void main(String[] args) {
    int v = 8;
    int[][] adjacencyMatrix = {
      {0,4,2,5,1,0,0,6},
      {4,0,3,2,0,6,4,2},
      {2,3,0,0,4,1,3,7},
      {5,2,0,0,7,0,2,3},
      {1,0,4,7,0,3,5,1},
      {0,6,1,0,3,0,2,4},
      {0,4,3,2,5,2,0,5},
      {0,1,2,3,4,5,6,7}
    };
    int maxV = 0;
    int maxS = 0;
    for (int i = 0; i < v; i++) {
      int sum = 0;
      for (int j = 0; j < v; j++) {
        sum += adjacencyMatrix[i][j];
      }
      if (sum > maxS) {
        maxS = sum;
        maxV = i;
      }
    }
    System.out.println("Vertex with maximum weight is: " + maxV + " and total weight is: " + maxS);
  }
}
