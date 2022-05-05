// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Test
{
    internal class Program
    {
        private static Dictionary<char, Vertex<char>> points = 
            new Dictionary<char, Vertex<char>>
        {
            {'A', new Vertex<char>('A')},
            {'B', new Vertex<char>('B')},
            {'C', new Vertex<char>('C')},
            {'D', new Vertex<char>('D')},
            {'F', new Vertex<char>('F')},
        };

        public static void Main(string[] args)
        {
            Edge<char> firstEdge = new Edge<char>(points['A'], points['C']);
            Edge<char> secondEdge = new Edge<char>(points['C'], points['B']);
            Edge<char> thirdEdge = new Edge<char>(points['C'], points['F']);
            Edge<char> forthEdge = new Edge<char>(points['B'], points['F']);
            Edge<char> fifthEdge = new Edge<char>(points['F'], points['D']);
            Edge<char> sixthEdge = new Edge<char>(points['D'], points['A']);

            points['A'].AddEdge(firstEdge);
            points['C'].AddEdge(secondEdge);
            points['C'].AddEdge(thirdEdge);
            points['B'].AddEdge(forthEdge);
            points['F'].AddEdge(fifthEdge);
            points['D'].AddEdge(sixthEdge);
            
            DFS(points['D']);
        }

        public static void DFS(Vertex<char> startPoint)
        {
            startPoint.Visited = true;
            Console.WriteLine(startPoint.Value);
            
            foreach (var edge in startPoint.Vertices)
            {
                if (edge.End.Visited == false)
                {
                    DFS(edge.End);
                }
            }
        }
    }
}

