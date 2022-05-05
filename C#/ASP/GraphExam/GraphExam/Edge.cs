namespace GraphSkeleton
{
    public class Edge<T>
    {
        private Node<T> _start;
        private Node<T> _end;
        private int _weight;
        
        public Edge(Node<T> start, Node<T> end, int weight)
        {
            _start = start;
            _end = end;
            _weight = weight;
        }
        
        public Node<T> Start
        {
            get => _start;
        }

        public Node<T> End
        {
            get => _end;
        }

        public int Weight
        {
            get => _weight;
        }

        public override string ToString()
        {
            return $"Edge(start={_start}, end={_end})";
        }
    }
}