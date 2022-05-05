using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3
{
    class Vertex
    {
        public int Value { get; set; }
        public List<Vertex> Edges = new List<Vertex>();
        public bool Visited { get; set; }
        public Vertex(int value)
        {
            this.Value = value;
            this.Visited = false;
        }

        public void AddEdge(Vertex ver)
        {
            if (!Edges.Contains(ver))
            {
                Edges.Add(ver);
            }
        }

        public override string ToString()
        {
            return $"Vertex({this.Value})";
        }
    }
    
    internal class Program
    {
        private static Vertex[] vertices;
        private static int bestPath = Int32.MaxValue;
        private static bool hasFound = false;
        
        public static void Main(string[] args)
        {
            int verticesCount = int.Parse(Console.ReadLine()!);
            int edgesCount = int.Parse(Console.ReadLine()!);

            vertices = new Vertex[verticesCount];
            for (int v = 0; v < verticesCount; v++)
            {
                vertices[v] = new Vertex(v);
            }

            for (int i = 0; i < edgesCount; i++)
            {
                int[] edgeInfo = Console.ReadLine()
                    .Split()
                    .Select(int.Parse)
                    .ToArray();
                
                vertices[edgeInfo[0]].AddEdge(vertices[edgeInfo[1]]);
                vertices[edgeInfo[1]].AddEdge(vertices[edgeInfo[0]]);
            }

            int startIndex = int.Parse(Console.ReadLine());
            Vertex start = vertices[startIndex];

            int endIndex = int.Parse(Console.ReadLine());
            Vertex end = vertices[endIndex];

            FindShortestPath(start, end);

            Console.WriteLine($"Shortest path length from 0 to {verticesCount - 1}: ");
            
            if (hasFound)
            {
                Console.WriteLine($"Path found. Length: {bestPath}");
            }
            else
            {
                Console.WriteLine($"No path exists");
            }
        }

        public static void FindShortestPath(Vertex start, Vertex end, int currentVal=0)
        {
            if (start == end)
            {
                bestPath = bestPath > currentVal ? currentVal : bestPath;
                hasFound = true;
                return;
            }

            if (!start.Visited)
            {
                start.Visited = true;
                
                foreach (Vertex child in start.Edges)
                {
                    FindShortestPath(child, end, currentVal + 1);
                }

                start.Visited = false;
            }
        }
    }
}