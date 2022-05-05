using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2TraverseDFS
{
    class Graph
    {
        private static int verticesCount;
        private static List<int>[] adjacents;

        public Graph(int _verticesCount)
        {
            adjacents = new List<int>[_verticesCount];

            for (int i = 0; i < adjacents.Length; i++)
            {
                adjacents[i] = new List<int>();
            }

            verticesCount = _verticesCount;
        }

        public void AddEdge(int firstVertex, int secondVertex)
        {
            adjacents[firstVertex].Add(secondVertex);
        }

        public void DFS(int vertex)
        {
            bool[] visited = new bool[verticesCount];

            DFSUtil(vertex, visited);
        }

        public void DFSUtil(int vertex, bool[] visited)
        {
            visited[vertex] = true;
            Console.Write(vertex + " ");
            List<int> verticesList = adjacents[vertex];

            foreach (var v in verticesList)
            {
                if (!visited[v])
                {
                    DFSUtil(v, visited);
                }
            }
        }
    }
    
    internal class Program
    {
        public static void Main(string[] args)
        {
            var graph = ReadGraph();

            int number = int.Parse(Console.ReadLine());
           
            Console.WriteLine("Following is Depth First " +
                              $"Traversal(starting from vertex {number})");
            
            graph.DFS(number);
        }
        
        public static Graph ReadGraph()
        {
            int vCount = int.Parse(Console.ReadLine());
            int edgeCount = int.Parse(Console.ReadLine());
            
            Graph graph = new Graph(vCount);

            for (int i = 0; i < edgeCount; i++)
            {
                int[] directions = Console.ReadLine()
                    .Split(' ')
                    .Select(int.Parse)
                    .ToArray();
                
                graph.AddEdge(directions[0], directions[1]);
            }
            
            return graph;
        }
    }
}