// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace ExamPreparation 
{
    internal class Program
    {
        private static bool[] visited;
        private static List<int>[] graph;
        private static bool hasFound;
        
        public static void Main(string[] args)
        {
            graph = ReadGraph();
            visited = new bool[graph.Length];
            DFS(1, 1);
            Console.WriteLine(hasFound ? "Yes" : "No");
        }
        private static void DFS(int start, int end)
        {
            if (start == end)
            {
                hasFound = true;
                return;
            }

            if (visited[start]) { return; }

            visited[start] = true;

            foreach (var child in graph[start])
            {
                DFS(child, end);
            }
        }
        private static List<int>[] ReadGraph()
        {
            int n = int.Parse(Console.ReadLine());
            var currentGraph = new List<int>[n];

            for (int i = 0; i < n; i++)
            {
                currentGraph[i] = Console.ReadLine()
                    .Split(" ", StringSplitOptions.RemoveEmptyEntries)
                    .Select(int.Parse)
                    .ToList();
            }

            return currentGraph;
        }
    }
}