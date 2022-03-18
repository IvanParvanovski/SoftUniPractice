using System;
using SimpleTreeNode;

namespace Ex1BuildTree
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            TreeNode<string> tree = new TreeNode<string>("A", 
                new TreeNode<string>("B", 
                    new TreeNode<string>("D",
                        new TreeNode<string>("H"), 
                        new TreeNode<string>("I")),
                    new TreeNode<string>("E")
                ),
                new TreeNode<string>("C",
                    new TreeNode<string>("F",
                        new TreeNode<string>("J")),
                    new TreeNode<string>("G"))
            );
            
            Console.WriteLine(tree.ToString());
        }
    }
}