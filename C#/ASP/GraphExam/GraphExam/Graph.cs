using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace GraphSkeleton
{
    public class Graph<T>
    {
        private IGraphBehaviour<T> _behaviour;
        private List<Node<T>> _nodes;
        private List<Edge<T>> _edges;
        
        public Graph(IGraphBehaviour<T> behaviour)
        {
            _nodes = new List<Node<T>>();
            _edges = new List<Edge<T>>();
            _behaviour = behaviour;
        }

        public List<Node<T>> Nodes
        {
            get => _nodes;
        }

        public List<Edge<T>> Edges
        {
            get => _edges;
        }
        
        public void AddNode(T value)
        {
            _nodes.Add(new Node<T>(value));
        }
        
        public void AddEdge(T start, T end)
        {
            Node<T> startNode = GetNode(start);
            Node<T> endNode = GetNode(end);
            
            if (startNode == null)
            {
                Console.WriteLine("Such START does not exist!");
                return;
            } 
            
            if (endNode == null)
            {
                Console.WriteLine("Such END does not exist!");
                return;
            }

            Edge<T> edge = new Edge<T>(startNode, endNode, 1);

            _edges.Add(edge);
        }
        
        public void AddManyNodes(List<T> value)
        {
            //  graph.AddManyNodes(new List<string> 
            //      {"Sofia", "Pleven", "Knezha", "Plovdiv", "Montana"}
            // );

            foreach (T val in value)
            {
                AddNode(val);
            }
        }
        
        public void AddManyEdges(List<List<T>> edges)
        {
            // graph.AddManyEdges(new List<List<string>>
            // {
            //     new List<string>{"Sofia", "Knezha"},
            //     new List<string>{"Sofia", "Pleven"},
            //     new List<string>{"Pleven", "Montana"},
            //     new List<string>{"Pleven", "Knezha"},
            //     new List<string>{"Knezha", "Plovdiv"},
            // });
            
            foreach (List<T> edgeInfo in edges)
            {
                if (edgeInfo.Count != 2)
                {
                    throw new Exception("The amount of given node names are more or less than 2!");
                }
                
                T start = edgeInfo[0];
                T end = edgeInfo[1];
                
                AddEdge(start, end);
            }            
        }
        
        public void PerformComputation(T start, T end)
        {
            Node<T> startNode = GetNode(start);
            Node<T> endNode = GetNode(end);
            
            _behaviour.Compute(startNode, endNode, _nodes, _edges);
        }
        
        public Node<T> GetNode(T val)
        {
            return _nodes.Find(x => x.Value.Equals(val));
        }
        
        public void SetGraphBehaviour(IGraphBehaviour<T> graphBehaviour)
        {
            _behaviour = graphBehaviour;
        }
    }
}