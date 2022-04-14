using System;
using System.Collections.Generic;
using System.Linq;

namespace GraphSkeleton
{
    public class DFSBehaviour<T>: IGraphBehaviour<T>
    {
        private Node<T> _start;
        private Node<T> _end;
        private List<Node<T>> _nodes;
        private List<Edge<T>> _edges;
       
        public void Compute(
            Node<T> start, Node<T> end,
            List<Node<T>> nodes, List<Edge<T>> edges)
        {
            _start = start;
            _end = end;
            _nodes = nodes;
            _edges = edges;

            var finalRes = GetResult(start, end, new List<Node<T>>());

            foreach (var VARIABLE in finalRes)
            {
                Console.WriteLine(VARIABLE);
            }
        }
        
        public List<Node<T>> GetResult(Node<T> start, Node<T> end, List<Node<T>> res)
        {
            Stack<Edge<T>> _sequence = new Stack<Edge<T>>();
            
            foreach (Edge<T> edge in _edges)
            {
                if (edge.Start == start)
                {
                    _sequence.Push(edge);
                }
            }

            if (start == end)
            {
                res.Add(end);
                
                return res;
            }

            if (!start.Visited)
            {
                start.Visited = true;
                res.Add(start);

                foreach (Edge<T> edge in _sequence)
                {
                    var finalResult = GetResult(edge.End, end, res.ToList());
                
                    if (finalResult.Contains(end))
                    {
                        return finalResult;
                    }
                }
            }
            
            return new List<Node<T>>();
        }

        public override string ToString()
        {
            return $"DFS({_start}, {_end})";
        }
    }
}