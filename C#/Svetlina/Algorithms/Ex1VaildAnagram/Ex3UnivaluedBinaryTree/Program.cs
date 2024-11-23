namespace UnivaluedBinaryTree
{
    public class Node
    {
        public Node Right { get; set; }
        public Node Left { get; set; }
        public int Value { get; set; }

        public Node(int value)
        {
            this.Value = value;
        }
    }

    public class Program
    {
        

        public static void Main(string[] args)
        {
            Node root = new Node(2);

            Node firstNode = new Node(2);
            Node secondNode = new Node(2);
            Node thirdNode = new Node(5);
            Node forthNode = new Node(2);

            root.Left = firstNode;
            root.Right = secondNode;

            firstNode.Left = thirdNode;
            firstNode.Right = forthNode;

            Console.WriteLine(DFS(root).Count == 1);
            
        }

        public static HashSet<int> DFS(Node root)
        {
            Stack<Node> currentNodes = new Stack<Node>();
            HashSet<int> result = new HashSet<int>();
            currentNodes.Push(root);


            while (currentNodes.Count != 0)
            {
                Node temp = currentNodes.Pop();
                result.Add(temp.Value);

                if (temp.Right != null)
                {
                    currentNodes.Push(temp.Right);
                }
                if (temp.Left != null)
                {
                    currentNodes.Push(temp.Left);
                }
            }

            return result;
        } 
    }
}