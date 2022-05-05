// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

namespace FindAllPathsBFS
{
    internal class Program
    {
        private static List<int>[] graph =
        {
            new List<int> {1, 2},
            new List<int> {2, 3},
            new List<int> {4, 1},
            new List<int> {5},
            new List<int> {5},
            new List<int> {},
        };

        private static bool[] visited = new bool[6];
        private static Queue<int> sequence = new Queue<int>(); 
        
        public static void Main(string[] args)
        {
            BFS(2, 5, new List<int>());
        }

        private static void BFS(int start, int end, List<int> result)
        {
            sequence.Enqueue(start);
            visited[start] = true;

            while (sequence.Count > 0)
            {
                int node = sequence.Dequeue();
                result.Add(node);

                if (node == end)
                {
                    Console.WriteLine(string.Join(" ", result));
                    return;
                }
                
                foreach (var child in graph[node])
                {
                    if (!visited[child])
                    {
                        sequence.Enqueue(child);
                        visited[child] = true;
                    }
                }
            }
        }
    }
}