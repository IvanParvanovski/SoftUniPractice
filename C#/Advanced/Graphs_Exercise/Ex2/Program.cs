// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2
{
    class Node
    {
        private int _value;
        private bool _visited;
        private Node _previous;
        private List<Node> _edges;

        public Node(int value)
        {
            this.Value = value;
            this.Visited = false;
            this._edges = new List<Node>();
        }

        public void AddEdge(Node ed)
        {
            if (!_edges.Contains(ed))
            {
                _edges.Add(ed);
            }
        }

        public override string ToString()
        {
            return $"Node({_value})";
        }

        public int Value
        {
            get => _value;
            set => _value = value;
        }

        public bool Visited
        {
            get => _visited;
            set => _visited = value;
        }
        
        public Node Previous
        {
            get => _previous;
            set => _previous = value;
        }

        public List<Node> Edges
        {
            get => _edges;
            set => _edges = value;
        }
    }
    
    internal class Program
    {
        private static List<Node> nodes = new List<Node>();
        
        public static void Main(string[] args)
        {
            int nodesCount = int.Parse(Console.ReadLine()!);
            int edgesCount = int.Parse(Console.ReadLine()!);

            for (int i = 0; i < nodesCount; i++)
            {
                nodes.Add(new Node(i));
            }

            for (int k = 0; k < edgesCount; k++)
            {
                int[] data = Console.ReadLine()!.Split('-').Select(int.Parse).ToArray();
                nodes[data[0]].AddEdge(nodes[data[1]]);
                nodes[data[1]].AddEdge(nodes[data[0]]);
            }

            bool r = false;
            foreach (Node node in nodes)
            {
                r = HasCycle(node, null);

                if (r)
                {
                    break;
                }
            }

            if (r)
            {
                Console.WriteLine("Graph contains cycle");
            }
            else
            {
                Console.WriteLine("Graph doesn't contain cycle");
            }
        }

        public static bool HasCycle(Node node, Node previous)
        {
            bool res = false;
            node.Previous = previous;
            
            if (!node.Visited)
            {
                node.Visited = true;
                
                foreach (Node child in node.Edges)
                {
                    res = HasCycle(child, node);
                    node.Previous = previous;

                    if (res) { break; }
                }

                node.Visited = false;
            }
            else if (previous.Previous != node)
            {
                res = true;
            }

            return res;
        }
    }
}