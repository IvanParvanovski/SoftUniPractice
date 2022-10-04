// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1TraverseGraphBFS
{
    class Graph
    {
        private static int verticesCount;
        private static LinkedList<int>[] adjacents;

        public Graph(int _verticesCount)
        {
            adjacents = new LinkedList<int>[_verticesCount];
            
            for (int i = 0; i < adjacents.Length; i++)
            {
                adjacents[i] = new LinkedList<int>();
            }

            verticesCount = _verticesCount;
        }

        public void AddEdge(int firstVertex, int secondVertex)
        {
            adjacents[firstVertex].AddLast(secondVertex);
        }

        public void BFS(int vertex)
        {
            bool[] visitedVertices = new bool[verticesCount];
            LinkedList<int> queue = new LinkedList<int>();
            
            visitedVertices[vertex] = true;
            queue.AddLast(vertex);

            while (queue.Any())
            {
                vertex = queue.First();
                Console.Write(vertex + " ");
                queue.RemoveFirst();
                LinkedList<int> list = adjacents[vertex];

                foreach (var adjacent in list)
                {
                    if (!visitedVertices[adjacent])
                    {
                        visitedVertices[adjacent] = true;
                        queue.AddLast(adjacent);
                    }
                }
            }
        }
    }
       
    class Program
    {
        
        public static void Main(string[] args)
        {
            Graph graph = new Graph(4);
            
            graph.AddEdge(0, 1);
            graph.AddEdge(0, 2);
            graph.AddEdge(1, 2);
            graph.AddEdge(2, 0);
            graph.AddEdge(2, 3);
            graph.AddEdge(3, 3);
            
            Console.Write("Following is Breadth First " +
                          "Traversal(starting from vertex 2\n");
            
            graph.BFS(2);
        }
    }
}