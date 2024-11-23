using System;

namespace ExTrees
{
    class MainClass
    {
        public class Node
        {
            public int Value { get; set; }
            public Node Left { get; set; }
            public Node Right { get; set; }

            public Node(int value)
            {
                this.Value = value;
            }
        }

        public static void Main(string[] args)
        {
            //Node rootNode = new Node(8);

            //Node nodeFirst = new Node(4);
            //Node nodeSecond = new Node(2);
            //Node nodeThird = new Node(6);
            //Node nodeForth = new Node(12);

            //rootNode.Left = nodeFirst;
            //rootNode.Right = nodeForth;
            //nodeFirst.Left = nodeSecond;
            //nodeFirst.Right = nodeThird;

            Node rootNode = new Node(12);
            Node leftNode = new Node(6);
            Node rightNode = new Node(11);

            rootNode.Left = leftNode;
            leftNode.Right = rightNode;

            Console.WriteLine(FindMinimumDifference(rootNode, int.MaxValue));
        }

        public static int FindMinimumDifference(Node root, int currentVal)
        {
            if (root.Left == null && root.Right == null)
            {
                return currentVal;
            }

            if (root.Left != null)
            {
                int differenceLeft = Math.Abs(root.Left.Value - root.Value);

                if (currentVal > differenceLeft)
                {
                    return FindMinimumDifference(root.Left, differenceLeft);
                }
                else
                {
                    return FindMinimumDifference(root.Left, currentVal);
                }

            }

            if (root.Right != null)
            {
                int differenceRight = Math.Abs(root.Right.Value - root.Value);

                if (currentVal > differenceRight)
                {
                    return FindMinimumDifference(root.Right, differenceRight);
                }
                else
                {
                    return FindMinimumDifference(root.Right, currentVal);
                }
            }

            return -1;
        }
    }
}
