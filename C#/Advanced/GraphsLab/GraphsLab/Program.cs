// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

namespace GraphsLab
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var g = new[]
            {
                new List<int> {3, 6},
                new List<int> {2, 3, 4, 5, 6},
                new List<int> {1, 4, 5},
                new List<int> {0, 1, 5},
                new List<int> {1, 2, 6},
                new List<int> {1, 2, 3},
                new List<int> {0, 1, 4},
            };

            bool[] visited = new bool[g.Length];

            for (int vertex = 0; vertex < g.Length; vertex++)
            {
                DFS(vertex, visited, g);
            }
        }

        private static void DFS(int vertex, bool[] visited, List<int>[] g)
        {
            if (!visited[vertex])
            {
                visited[vertex] = true;

                foreach (var adjacent in g[vertex])
                {
                    DFS(adjacent, visited, g);
                }

                Console.WriteLine(vertex);
            }
        }
    }
}
