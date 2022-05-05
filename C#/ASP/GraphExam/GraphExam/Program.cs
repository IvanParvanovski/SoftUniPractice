// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;

namespace GraphSkeleton
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Graph<string> graph = new Graph<string>(
                new BFSBehaviour<string>());
            
            graph.AddManyNodes(new List<string>()
            {
                "Boss", 
                "Sarah", 
                "Lora", 
                "Viktor", 
                "Evan", 
                "Cole", 
                "Mary",
                "Clare",
                "Nicole",
                "Alex",
                "Anya",
                "Peter",
                "Mike"
            });
            
            graph.AddManyEdges(new List<List<string>>
            {
                new List<string>{"Boss", "Sarah"},
                new List<string>{"Boss", "Evan"},
                new List<string>{"Boss", "Mike"},
                new List<string>{"Sarah", "Lora"},
                new List<string>{"Sarah", "Viktor"},
                new List<string>{"Evan", "Cole"},
                new List<string>{"Evan", "Nicole"},
                new List<string>{"Cole", "Mary"},
                new List<string>{"Cole", "Clare"},
                new List<string>{"Nicole", "Alex"},
                new List<string>{"Nicole", "Anya"},
                new List<string>{"Alex", "Peter"}
            });
            
            string end = Console.ReadLine();
            
            graph.PerformComputation("Boss", end);
            
        }
    }
}