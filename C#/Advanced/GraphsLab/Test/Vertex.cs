using System.Collections.Generic;

namespace Test
{
    public class Vertex<T>
    {
        private T _value;
        private bool _visited;
        private List<Edge<T>> _vertices = new List<Edge<T>>();
        public Vertex(T value)
        {
            _value = value;
            this.Visited = false;
        }

        public override string ToString()
        {
            return $"Vertex({_value})";
        }

        public void AddEdge(Edge<T> edge)
        {
            _vertices.Add(edge);
        }

        public void RemoveEdge(Edge<T> edge)
        {
            _vertices.Remove(edge);
        }

        public bool Visited
        {
            get => _visited;
            set => _visited = value;
        }

        public T Value
        {
            get => _value;
            set => _value = value;
        }

        public List<Edge<T>> Vertices
        {
            get => _vertices;
            set => _vertices = value;
        }
    }
}