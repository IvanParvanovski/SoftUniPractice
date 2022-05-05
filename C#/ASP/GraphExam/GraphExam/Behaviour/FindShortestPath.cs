using System;
using System.Collections.Generic;
using System.Linq;

namespace GraphSkeleton
{
    public class FindShortestPath<T>: IGraphBehaviour<T>
    {
        private Node<T> _start;
        private Node<T> _end;
        private List<Node<T>> _nodes;
        private List<Edge<T>> _edges;
        
        private List<Node<T>> _bestPath = new List<Node<T>>();
        private int _bestPathVal = Int32.MaxValue;
        private bool _hasFound = false;
        
        public void Compute(
            Node<T> start, 
            Node<T> end, 
            List<Node<T>> nodes,
            List<Edge<T>> edges)
        {
            _start = start;
            _end = end;
            _nodes = nodes;
            _edges = edges;
            
            GetResult(start, end, new List<Node<T>>());

            if (!_hasFound)
            {
                Console.WriteLine("There is no path found!");
            }
            else
            {
                foreach (Node<T> n in _bestPath)
                {
                    Console.WriteLine(n);
                }

                Console.WriteLine(_bestPathVal);
            }
        }

        public void GetResult(Node<T> start, Node<T> end, List<Node<T>> result, int currentVal=0)
        {
            Stack<Edge<T>> _sequenceOfEdges = new Stack<Edge<T>>();
            
            foreach (Edge<T> edge in _edges)
            {
                if (edge.Start == start)
                {
                    _sequenceOfEdges.Push(edge);
                }
            }

            if (start == end)
            {
                if (currentVal < _bestPathVal)
                {
                    _bestPath = result;
                    _bestPathVal = currentVal;
                }

                _hasFound = true;
                return;
            }

            if (_sequenceOfEdges.Count == 0)
            {
                return;
            }

            if (!start.Visited)
            {
                start.Visited = true;
                result.Add(start);
                
                foreach (Edge<T> edge in _sequenceOfEdges)
                {
                    GetResult(edge.End, end, result.ToList(), currentVal + edge.Weight);
                }

                start.Visited = false;
            }
        }
    }
}