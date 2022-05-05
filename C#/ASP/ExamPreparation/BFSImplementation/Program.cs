// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace BFSImplementation
{
    internal class Program
    {
        private static Queue<int> sequence = new Queue<int>();
        private static bool[] visited = new bool[5];
        private static List<int>[] graph =
        {
            new List<int> {1, 2},
            new List<int> {4, 3, 0},
            new List<int> {3, 0},
            new List<int> {1, 4, 2},
            new List<int> {1, 3}
        };
        
        public static void Main(string[] args)
        {
            BFS(0, 4, new List<int>());
        }

        private static void BFS(int start, int end, List<int> result)
        {
            if (start == end)
            {
                result.Add(start);
                Console.WriteLine(string.Join(" ", result));
                
                return;
            }

            if (visited[start]) { return; }

            visited[start] = true;
            result.Add(start);

            foreach (var child in graph[start])
            {
                sequence.Enqueue(child);
            }

            while (sequence.Count > 0)
            {
                int startNode = sequence.Dequeue();
                BFS(startNode, end, result.ToList());
            }            
        }
    }
}

