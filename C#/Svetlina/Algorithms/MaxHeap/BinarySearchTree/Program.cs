using System.Diagnostics;

namespace BinarySearchTree
{
    class Node
    {
        public int Value;
        public Node Left;
        public Node Right;
    }

    class Tree
    {
        public Node Insert(Node root, int v)
        {
            if (root == null)
            {
                root = new Node();
                root.Value = v;
            }
            else if (v < root.Value)
            {
                root.Left = Insert(root.Left, v);
            }
            else if (v > root.Value)
            {
                root.Right = Insert(root.Right, v);
            }

            return root;
        }


        public void Traverse(Node root)
        {
            if (root == null)
            {
                return;
            }

            Traverse(root.Left);
            Traverse(root.Right);
        }
    }

    class Program
    {
        public static void Main(string[] args)
        {
            Node root = null;
            Tree bst = new Tree();
            int SIZE = 2000000;
            int[] a = new int[SIZE];

            Console.WriteLine("Generating random array with {0} values...", SIZE);

            Random random = new Random();

            Stopwatch watch = Stopwatch.StartNew();

            for (int i = 0; i < SIZE; i++)
            {
                a[i] = random.Next(10000);
            }

            watch.Stop();

            Console.WriteLine("Done. Took {0} seconds", (double)watch.ElapsedMilliseconds / 1000.0);
            Console.WriteLine();
            Console.WriteLine("Filling the tree with {0} nodes...", SIZE);

            watch = Stopwatch.StartNew();

            for (int i = 0; i < SIZE; i++)
            {
                root = bst.Insert(root, a[i]);
            }

            watch.Stop();

            Console.WriteLine("Done. Took {0} seconds", (double)watch.ElapsedMilliseconds / 1000.0);
            Console.WriteLine();
            Console.WriteLine("Traversing all {0} nodes in tree...", SIZE);

            watch = Stopwatch.StartNew();

            bst.Traverse(root);

            watch.Stop();

            Console.WriteLine("Done. Took {0} seconds", (double)watch.ElapsedMilliseconds / 1000.0);
            Console.WriteLine();

            Console.ReadKey();
        }
    }
}