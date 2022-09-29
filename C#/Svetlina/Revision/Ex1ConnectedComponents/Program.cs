// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace ConnectedComponents
{
    class Program
    {
        public static bool[] visited;
        public static List<int[]> graph;
        
        public static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            graph = ReadGraph(n);
            GetAllPaths();
        }

        public static void GetAllPaths()
        {
            visited = new bool[graph.Count];

            for (int startNode = 0; startNode < graph.Count; startNode++)
            {
                if (!visited[startNode])
                {
                    Console.Write("Connected component:");
                }
            }
        }

        public static void DFS(int vertex) 
        {
            if (!visited[vertex])
            {
                visited[vertex] = true;
                foreach (var child in graph[vertex])
                {
                    DFS(child);
                }
            }
        }

        public static List<int[]> ReadGraph(int n)
        {
            List<int[]> tempGraph = new List<int[]>();

            for (int i = 0; i < n; i++)
            {
                string inputData = Console.ReadLine();
                if (inputData == "")
                {
                    tempGraph.Add(new int[0]);
                }
                else
                {
                    int[] currentRow = inputData.Split().Select(int.Parse).ToArray();
                    tempGraph.Add(currentRow);
                }
            }

            return tempGraph;
        }
    }
}