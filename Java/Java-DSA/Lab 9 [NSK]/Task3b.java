public class Task3b {
  public static void main(String[] args) {
    int v = 8;
    Edge[] adjList = new Edge[v];
    
    addEdge(adjList, 0, 1, 4);
    addEdge(adjList, 0, 2, 2);
    addEdge(adjList, 0, 3, 5);
    addEdge(adjList, 0, 4, 1);
    addEdge(adjList, 0, 7, 6);
    
    addEdge(adjList, 1, 0, 4);
    addEdge(adjList, 1, 2, 3);
    addEdge(adjList, 1, 3, 2);
    addEdge(adjList, 1, 5, 6);
    addEdge(adjList, 1, 6, 4);
    addEdge(adjList, 1, 7, 2);
    
    addEdge(adjList, 2, 0, 2);
    addEdge(adjList, 2, 1, 3);
    addEdge(adjList, 2, 4, 4);
    addEdge(adjList, 2, 5, 1);
    addEdge(adjList, 2, 6, 3);
    addEdge(adjList, 2, 7, 7);
    
    addEdge(adjList, 3, 0, 5);
    addEdge(adjList, 3, 1, 2);
    addEdge(adjList, 3, 4, 7);
    addEdge(adjList, 3, 6, 2);
    addEdge(adjList, 3, 7, 3);
    
    addEdge(adjList, 4, 0, 1);
    addEdge(adjList, 4, 2, 4);
    addEdge(adjList, 4, 3, 7);
    addEdge(adjList, 4, 5, 3);
    addEdge(adjList, 4, 6, 5);
    addEdge(adjList, 4, 7, 1);
    
    addEdge(adjList, 5, 1, 6);
    addEdge(adjList, 5, 2, 1);
    addEdge(adjList, 5, 4, 3);
    addEdge(adjList, 5, 6, 2);
    addEdge(adjList, 5, 7, 4);
    
    addEdge(adjList, 6, 1, 1);
    addEdge(adjList, 6, 2, 2);
    addEdge(adjList, 6, 3, 3);
    addEdge(adjList, 6, 4, 4);
    addEdge(adjList, 6, 5, 5);
    addEdge(adjList, 6, 6, 6);
    addEdge(adjList, 6, 7, 7);
    
    addEdge(adjList, 7, 1, 1);
    addEdge(adjList, 7, 2, 2);
    addEdge(adjList, 7, 3, 3);
    addEdge(adjList, 7, 4, 4);
    addEdge(adjList, 7, 5, 5);
    addEdge(adjList, 7, 6, 6);
    addEdge(adjList, 7, 7, 7);
    
    int maxV = 0;
    int maxS = 0;
    int maxD = 0;
    int[] maxDVertices = new int[v];
    int maxDCnt = 0;
    for (int i = 0; i < v; i++) {
      int sum = 0;
      int degree = 0;
      Edge temp = adjList[i];
      while (temp != null) {
        sum += temp.weight;
        degree++;
        temp = temp.next;
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
    System.out.println("Vertex with maximum outgoing weight is: " + maxV + " and total outgoing weight is: " + maxS);
    System.out.print("Vertex/vertices with maximum out-degree (" + maxD + "): ");
    for (int k = 0; k < maxDCnt; k++) {
      System.out.print(maxDVertices[k] + " ");
    }
    System.out.println();
  }
  public static void addEdge(Edge[] adjList, int src, int dest, int w) {
    Edge newEdge = new Edge(dest, w);
    newEdge.next = adjList[src];
    adjList[src] = newEdge;
  }
}

