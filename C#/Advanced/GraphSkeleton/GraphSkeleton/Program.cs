using System;
using System.Collections.Generic;

namespace GraphSkeleton
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            
            Graph<string> graph = new Graph<string>(
                new FindShortestPath<string>()
            );
            
            graph.AddManyNodes(new List<string> 
                {"Sofia", "Pleven", "Knezha", "Plovdiv", "Montana", "Lovech"}
            );
            
            graph.AddManyEdges(new List<List<string>>
            {
                new List<string>{"Sofia", "Knezha"},
                new List<string>{"Sofia", "Pleven"},
                
                new List<string>{"Pleven", "Montana"},
                
                new List<string>{"Montana", "Plovdiv"},
                
                new List<string>{"Knezha", "Pleven"},
                new List<string>{"Knezha", "Plovdiv"},
                new List<string>{"Knezha", "Lovech"},
                new List<string>{"Knezha", "Sofia"},
                
                new List<string>{"Plovdiv", "Montana"},
                new List<string>{"Plovdiv", "Knezha"},
                new List<string>{"Plovdiv", "Lovech"},
                
                new List<string>{"Lovech", "Knezha"},
            });

            graph.PerformComputation("Pleven", "Sofia");
        }
    }
}