namespace Test
{
    public class Edge<T>
    {
        private Vertex<T> _start;
        private Vertex<T> _end;

        public Edge(Vertex<T> start, Vertex<T> end)
        {
            _start = start;
            _end = end;
        }

        public Vertex<T> Start
        {
            get => _start;
            set => _start = value;
        }

        public Vertex<T> End
        {
            get => _end;
            set => _end = value;
        }
    }
}