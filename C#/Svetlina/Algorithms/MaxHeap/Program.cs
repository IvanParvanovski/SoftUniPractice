namespace MaxHeap
{
    public class Program
    {
        public class Node
        {
            public Node left;
            public Node right;
            public Node parent;

            public int data;

            public Node(int data)
            {
                this.data = data;
            }
        }

        public class MaxBinaryHeap
        {
            Node Root;
            Node InsertPos;

            public MaxBinaryHeap(Node node)
            {
                Root = node;
                InsertPos = node;
            }

            public void Insert(Node n)
            {
                if (InsertPos.left == null)
                {
                    InsertPos.left = n;
                    n.parent = InsertPos;
                }
            }
        }

        public void Main(string[] args)
        {

        }
    }
}