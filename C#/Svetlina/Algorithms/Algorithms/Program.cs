using System;
using System.Collections.Generic;

namespace Algorithms
{
    class Node
    {
        public int Value { get; set; }
        public Node Left { get; set; }
        public Node Right { get; set; }

        public Node(int value)
        {
            this.Value = value;
        }
    }

    class MainClass
    {
        public static void Main(string[] args)
        {
            Node rootNode = new Node(10);
            Node firstNode = new Node(5);
            Node secondNode = new Node(15);
            Node thirdNode = new Node(3);
            Node forthNode = new Node(7);
            Node fifthNode = new Node(18);

            rootNode.Left = firstNode;
            rootNode.Right = secondNode;

            firstNode.Left = thirdNode;
            firstNode.Right = forthNode;

            secondNode.Right = fifthNode;

            int low = 7;
            int high = 15;

            Console.WriteLine("The sum is:" + Traverse(rootNode, low, high));
        }

        public static int Traverse(Node rootNode, int low, int high)
        {
            Queue<Node> nodes = new Queue<Node>();
            nodes.Enqueue(rootNode);
            int sum = 0;

            while (nodes.Count > 0)
            {
                Node currentNode = nodes.Dequeue();
                Console.WriteLine(currentNode.Value);

                if (currentNode.Value >= low && currentNode.Value <= high)
                {
                    sum += currentNode.Value;
                }

                if (currentNode.Left != null)
                {
                    nodes.Enqueue(currentNode.Left);
                }
                if (currentNode.Right != null)
                {
                    nodes.Enqueue(currentNode.Right);
                }
            }

            return sum;
        }
    }
}
