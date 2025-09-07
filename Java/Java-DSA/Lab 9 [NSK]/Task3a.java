public class Task3a {
  public static void main(String[] args) {
    int v = 8;
    int[][] adjacencyMatrix = {
      {0,4,2,5,1,0,0,6},
      {4,0,3,2,0,6,4,2},
      {2,3,0,0,4,1,3,7},
      {5,2,0,0,7,0,2,3},
      {1,0,4,7,0,3,5,1},
      {0,6,1,0,3,0,2,4},
      {0,1,2,3,4,5,6,7},
      {0,1,2,3,4,5,6,7}
    };
    int maxV = 0;
    int maxS = 0;
    int maxD = 0;
    int[] maxDVertices = new int[v];
    int maxDCnt = 0;
    for (int i = 0; i < v; i++) {
      int sum = 0;
      int degree = 0;
      for (int j = 0; j < v; j++) {
        if (adjacencyMatrix[i][j] != 0) degree++;
        sum += adjacencyMatrix[i][j];
      }
      if (sum > maxS) {
        maxS = sum;
        maxV = i;
      }
      if (degree > maxD) {
        maxD = degree;
        maxDCnt = 0;
        maxDVertices[maxDCnt++] = i;
      } else if (degree == maxD) {
        maxDVertices[maxDCnt++] = i;
      }
    }
    System.out.println("Vertex with max outgoing weight is: " + maxV + " and total outgoing weight is: " + maxS);
    System.out.print("Vertex/vertices with maximum out-degree (" + maxD + "): ");
    for (int k = 0; k < maxDCnt; k++) {
      System.out.print(maxDVertices[k] + " ");
    }
    System.out.println();
  }
}
