from collections import defaultdict
 
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) 
        self.V = vertices 
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def topologicalSortUtil(self,v,visited,stack):
 
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        print (v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
            print ('hhhh') 
        # Push current vertex to stack which stores result
        stack.insert(0,v)
        print (stack)
 
    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil()
    def topologicalSort(self):
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Print contents of stack
        print (stack)


def main():
    g= Graph(6)
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
     
    print ("Following is a Topological Sort of the given graph")
    g.topologicalSort()

main()    
