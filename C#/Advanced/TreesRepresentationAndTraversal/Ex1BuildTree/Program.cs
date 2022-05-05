using System;
using SimpleTreeNode;

namespace Ex1BuildTree
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            // TreeNode<string> tree = new TreeNode<string>("A", 
            //     new TreeNode<string>("B", 
            //         new TreeNode<string>("D",
            //             new TreeNode<string>("H"), 
            //             new TreeNode<string>("I")),
            //         new TreeNode<string>("E")
            //     ),
            //     new TreeNode<string>("C",
            //         new TreeNode<string>("F",
            //             new TreeNode<string>("J")),
            //         new TreeNode<string>("G"))
            // );
            //
            // Console.WriteLine(tree.ToString());

            TreeNode<int> tree2 = new TreeNode<int>(25,
                new TreeNode<int>(20, 
                    new TreeNode<int>(10,
                        new TreeNode<int>(5,
                            new TreeNode<int>(1),
                            new TreeNode<int>(8)),
                        new TreeNode<int>(12,
                            new TreeNode<int>(15))),
                    new TreeNode<int>(22)),
                new TreeNode<int>(36,
                    new TreeNode<int>(30,
                        new TreeNode<int>(28)),
                    new TreeNode<int>(40,
                        new TreeNode<int>(38),
                        new TreeNode<int>(48,
                            new TreeNode<int>(45),
                            new TreeNode<int>(50)))));

            Console.WriteLine(tree2.ToString());
        }
    }
}