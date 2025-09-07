class Edge {
  int dest;
  int weight;
  Edge next;
  
  Edge(int d, int w) {
    dest = d;
    weight = w;
    next = null;
  }
}