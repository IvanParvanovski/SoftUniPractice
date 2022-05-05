// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1GraphBFS
{
    // public class Graph
    // {
    //     private static int _verticesCount;
    //     private static LinkedList<int>[] _adjacents;
    //     
    //     public Graph(int verticesCount)
    //     {
    //         _adjacents = new LinkedList<int>[verticesCount];
    //         
    //         for (int i = 0; i < _adjacents.Length; i++)
    //         {
    //             _adjacents[i] = new LinkedList<int>();
    //         }
    //
    //         _verticesCount = verticesCount;
    //     }
    //
    //     public void AddEdge(int firstVertex, int secondVertex)
    //     {
    //         _adjacents[firstVertex].AddLast(secondVertex);
    //     }
    //
    //     public void BFS(int vertex)
    //     {
    //         bool[] visitedVertices = new bool[_verticesCount];
    //         LinkedList<int> queue = new LinkedList<int>();
    //
    //         visitedVertices[vertex] = true;
    //         queue.AddLast(vertex);
    //
    //         while (queue.Any())
    //         {
    //             vertex = queue.First();
    //             Console.Write(vertex + " ");
    //             queue.RemoveFirst();
    //
    //             LinkedList<int> list = _adjacents[vertex];
    //
    //             foreach (var adjacent in list)
    //             {
    //                 if (!visitedVertices[adjacent])
    //                 {
    //                     visitedVertices[adjacent] = true;
    //                     queue.AddLast(adjacent);
    //                 }
    //             }
    //         }
    //     }
    // }
    //
    internal class Program
    {
        
        public static void Main(string[] args)
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

            int number = int.Parse(Console.ReadLine());
           
            Console.WriteLine("Following is Breadth First " +
                              $"Traversal(starting from vertex {number})");
            
            graph.BFS(number);
        }
    }
}
