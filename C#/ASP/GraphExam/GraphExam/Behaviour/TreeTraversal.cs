using System;
using System.Collections.Generic;
using System.Linq;

namespace GraphSkeleton
{
    public class TreeTraversal<T>: IGraphBehaviour<T>
    {
        private Node<T> _start;
        private Node<T> _end;
        private List<Node<T>> _nodes;
        private List<Edge<T>> _edges;
        Stack<Edge<T>> _sequence = new Stack<Edge<T>>();

        public void Compute(Node<T> start, Node<T> end, List<Node<T>> nodes, List<Edge<T>> edges)
        {
            _start = start;
            _end = end;
            _nodes = nodes;
            _edges = edges;

            List<Node<T>> res = GetResult(start, end, new List<Node<T>>());

            foreach (Node<T> n in res)
            {
                Console.WriteLine(n.Value);
            }
        }

        public List<Node<T>> GetResult(Node<T> start, Node<T> end, List<Node<T>> res)
        {
            
            foreach (Edge<T> edge in _edges)
            {
                if (edge.Start == start)
                {
                    // _sequence.Enqueue(edge);
                }
            }

            if (_sequence.Count == 0)
            {
                return new List<Node<T>>();
            }

            if (start == end)
            {
                res.Add(end);
                
                return res;
            }

            res.Add(start);
            foreach (Edge<T> edge in _sequence)
            {
                var finalResult = GetResult(edge.End, end, res);
                
                if (finalResult.Contains(end))
                {
                    
                    return finalResult;
                }
            }
            
            

            return new List<Node<T>>();
        }
    }
}