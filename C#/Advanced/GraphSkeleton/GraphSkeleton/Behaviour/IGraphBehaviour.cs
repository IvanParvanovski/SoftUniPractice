using System.Collections.Generic;
using System.Threading;

namespace GraphSkeleton
{
    public interface IGraphBehaviour<T>
    {
        void Compute(
            Node<T> start,
            Node<T> end,
            List<Node<T>> nodes, 
            List<Edge<T>> edges);
    }
}