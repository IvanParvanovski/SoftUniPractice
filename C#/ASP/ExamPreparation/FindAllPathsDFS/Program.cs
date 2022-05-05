// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace FindAllPathsDFS
{
    internal class Program
    {
        private static List<int>[] graph =
        {
            new List<int> {1, 2},
            new List<int> {2, 3},
            new List<int> {4, 1},
            new List<int> {5},
            new List<int> {5}
        };

        private static bool[] visited = new bool[6];
        
        public static void Main(string[] args)
        {
            DFS(0, 5, new List<int>());
        }

        private static void DFS(int start, int end, List<int> result)
        {
            if (start == end)
            {
                result.Add(end);
                Console.WriteLine(string.Join(" ", result));
                
                return;
            }

            if (visited[start])
            {
                return;
            }

            visited[start] = true;
            result.Add(start);
            
            foreach (var child in graph[start])
            {
                DFS(child, end, result.ToList());
            }
         
            visited[start] = false;
        }
    }
}