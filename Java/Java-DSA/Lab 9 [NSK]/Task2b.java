public class Task2b {
  public static void main(String[] args) {
    int v = 8;
    Node[] adjList = new Node[v];
    
    addEdge(adjList, 0, 1, 4);
    addEdge(adjList, 0, 2, 2);
    addEdge(adjList, 0, 3, 5);
    addEdge(adjList, 0, 4, 1);
    addEdge(adjList, 0, 7, 6);
    
    addEdge(adjList, 1, 2, 3);
    addEdge(adjList, 1, 3, 2);
    addEdge(adjList, 1, 5, 6);
    addEdge(adjList, 1, 6, 4);
    addEdge(adjList, 1, 7, 2);
    
    addEdge(adjList, 2, 4, 4);
    addEdge(adjList, 2, 5, 1);
    addEdge(adjList, 2, 6, 3);
    addEdge(adjList, 2, 7, 7);
    
    addEdge(adjList, 3, 4, 7);
    addEdge(adjList, 3, 6, 2);
    addEdge(adjList, 3, 7, 3);
    
    addEdge(adjList, 4, 5, 3);
    addEdge(adjList, 4, 6, 5);
    addEdge(adjList, 4, 7, 1);
    
    addEdge(adjList, 5, 6, 2);
    addEdge(adjList, 5, 7, 4);
    
    addEdge(adjList, 6, 7, 5);
    
    int maxV = 0;
    int maxS = 0;
    for (int i = 0; i < v; i++) {
      int sum = 0;
      Node temp = adjList[i];
      while (temp != null) {
        sum += temp.weight;
        temp = temp.next;
      }
      if (sum > maxS) {
        maxS = sum;
        maxV = i;
      }
    }
    
    System.out.println("Vertex with maximum weight is: " + maxV + " and total weight is: " + maxS);
  }
  
  private static void addEdge(Node[] adjList, int u, int v, int w) {
    Node nodeU = new Node(v, w);
    nodeU.next = adjList[u];
    adjList[u] = nodeU;
    Node nodeV = new Node(u, w);
    nodeV.next = adjList[v];
    adjList[v] = nodeV;
  }
}
