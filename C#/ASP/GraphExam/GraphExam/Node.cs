namespace GraphSkeleton
{
    public class Node<T>
    {
        private T _value;
        private bool _visited;

        public Node(T value)
        {
            _value = value;
            _visited = false;
        }
        
        public T Value
        {
            get => _value;
            set => _value = value;
        }
        
        public bool Visited
        {
            get => _visited;
            set => _visited = value;
        }

        public override string ToString()
        {
            return $"Node({_value}, {_visited})";
        }

      
    }
}