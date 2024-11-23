namespace Ex6InOrderTraversal
{
    public class Node
    {
        public int Value { get; set; }
        public Node? Left { get; set; }
        public Node? Right { get; set; }

        public Node(int value)
        {
            this.Value = value;
            this.Left = null;
            this.Right = null;
        }
    }

    public class BinaryTree
    {
        public Node Root { get; set; }

        public void InOrderTraversal(Node root)
        {
            if (root != null)
            {
                InOrderTraversal(root.Left);
                Console.Write(root.Value + " ");
                InOrderTraversal(root.Right);
            }
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            Node root = new Node(5);

            root.Left = new Node(3);
            root.Right = new Node(6);
            root.Right.Right = new Node(8);
            root.Right.Right.Left = new Node(7);
            root.Right.Right.Right = new Node(9);


            root.Left.Left = new Node(2);
            root.Left.Right = new Node(4);

            root.Left.Left.Left = new Node(1);


            BinaryTree binaryTree = new BinaryTree();
            binaryTree.Root = root;

            Console.WriteLine("In-Order Traversal:");
            binaryTree.InOrderTraversal(binaryTree.Root);
        }
    }
}