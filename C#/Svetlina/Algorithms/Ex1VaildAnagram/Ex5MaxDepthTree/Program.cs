namespace MaxDepth
{
    public class Program
    {
        class Node
        {
            int Value { get; set; }
            public Node Right { get; set; }
            public Node Left { get; set; }

            public Node(int value)
            {
                this.Value = value;
            }
        }

        public int maxValue = 0;

        public static void Main(string[] args)
        {
            Node root = new Node(3);
            Node firstNode = new Node(9);
            Node secondNode = new Node(20);
            Node thirdNode = new Node(15);
            Node forthNode = new Node(7);



        }

        public static void Traverse(int root)
        {

        }
    }
}