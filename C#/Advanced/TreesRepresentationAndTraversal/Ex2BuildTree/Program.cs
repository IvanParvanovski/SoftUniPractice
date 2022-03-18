// See https://aka.ms/new-console-template for more information

using SimpleTreeNode;

namespace Ex2
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            TreeNode<int> tree = new TreeNode<int>(25,
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
                        new TreeNode<int>(28))));
        }
    }
}
