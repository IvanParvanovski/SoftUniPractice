using System;
using System.Collections.Generic;

namespace AverageSumLevels
{
    class Node
    {
        public int Value { get; set; }
        public Node Left { get; set; }
        public Node Right { get; set; }
        public bool visited { get; set; }

        public Node(int value)
        {
            this.Value = value;
        }
    }


    class MainClass
    {
        public static void Main(string[] args)
        {
            Node rootNode = new Node(3);

            Node firstNode = new Node(9);
            Node secondNode = new Node(20);
            Node thirdNode = new Node(15);
            Node forthNode = new Node(7);
        }

        public static List<double> AverageLevels(Node rootNode)
        {
            Queue<Node> mainQueue = new Queue<Node>();
            Queue<Node> currentQueue = new Queue<Node>();

            mainQueue.Enqueue(rootNode);

            while (currentQueue.)
            {
                while (mainQueue.Count > 0)
                {
                    Node currentNode = mainQueue.Dequeue();

                    Node leftNode = currentNode.Left;
                    if (leftNode == null)
                    {
                        currentQueue.Enqueue(new Node(0));
                    }
                    else
                    {
                        currentQueue.Enqueue(leftNode);
                    }

                    Node rightNode = currentNode.Right;
                    if (rightNode == null)
                    {
                        currentQueue.Enqueue(new Node(0));
                    }
                    else
                    {
                        currentQueue.Enqueue(rightNode);
                    }
                }

                double levelSum = 0;
                while (currentQueue.Count > 0)
                {
                    Node temp = currentQueue.Dequeue();
                    levelSum += temp.Value;

                    temp.visited = true;
                    mainQueue.Enqueue(temp);
                }
            }

            return new List<double>();
        }
    }
}
