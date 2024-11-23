namespace ExamFile
{
    public class TreeNode
    {
        public TreeNode? Right { get; set; }
        public TreeNode? Left { get; set; }
        public int Value { get; set; }

        public TreeNode(int value = 0)
        {
            this.Right = null;
            this.Left = null;
            this.Value = value;
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            //TreeNode root = new TreeNode(3);

            //TreeNode firstNode = new TreeNode(9);
            //TreeNode secondNode = new TreeNode(20);
            //TreeNode thirdNode = new TreeNode(15);
            //TreeNode forthNode = new TreeNode(7);

            //root.Left = firstNode;
            //root.Right = secondNode;

            //root.Right.Left = thirdNode;
            //root.Right.Right = forthNode;

            //Console.WriteLine(FindTheSumOfBTLeftLeaves(root));

            //var matrix = new int[3][] {
            //   new int[] {1, 2},
            //   new int[] {3, 4},
            //   new int[] {5, 6},
            //};

            //ChangeDimensionsOfMatrix(matrix, 2, 2);

            //Console.WriteLine(ValidatePangram("thequickbrownfoxjumpsoverthelazydog"));
            //Console.WriteLine(ValidatePangram("harrypotter"));

            TreeNode root = new TreeNode(1);
            TreeNode firstNode = new TreeNode(0);
            TreeNode secondNode = new TreeNode(1);
            TreeNode thirdNode = new TreeNode(0);
            TreeNode forthNode = new TreeNode(1);
            TreeNode fifthNode = new TreeNode(0);
            TreeNode sixthNode = new TreeNode(1);

            root.Left = firstNode;
            root.Right = secondNode;

            root.Left.Left = thirdNode;
            root.Left.Right = forthNode;

            root.Right.Left = fifthNode;
            root.Right.Right = sixthNode;

            LeafRootBinSum(root);
        }

        public static int FindNumber(int[] numbers)
        {
            var uniqueNumbers = numbers.ToHashSet();
            int maxNum = uniqueNumbers.Max();
            int minNum = uniqueNumbers.Min();

            var uniqueNumbersRequired = Enumerable.Range(minNum, maxNum + 1).ToHashSet();
            var result = uniqueNumbersRequired.Except(uniqueNumbers);

            if (result.Count() == 0)
            {
                return maxNum + 1;
            }

            return result.First();
        }

        public static int FindTheSumOfBTLeftLeaves(TreeNode node)
        {
            int sum = 0;
            var nodes = new Stack<TreeNode>();
            nodes.Push(node);

            while (nodes.Count > 0)
            {
                var currentNode = nodes.Pop();

                if (currentNode.Left != null &&
                    currentNode.Left.Left == null &&
                    currentNode.Left.Right == null)
                {
                    sum += currentNode.Left.Value;
                }

                if (currentNode.Left != null)
                {
                    nodes.Push(currentNode.Left);
                }
                if (currentNode.Right != null)
                {
                    nodes.Push(currentNode.Right);
                }
            }

            return sum;
        }

        public static int[][] ChangeDimensionsOfMatrix(int[][] mat, int r, int c)
        {
            int m = mat.Length;
            int n = mat[0].Length;
            int[][] result = new int[r][];
            int row = 0;
            int col = 0;

            if (m * n != r * c)
            {
                return mat;
            }  

            for (int i = 0; i < r; i++)
            {
                result[i] = new int[c];
            }

            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {

                    result[row][col] = mat[i][j];
                    col++;

                    if (col == c)
                    {
                        row++;
                        col = 0;
                    }
                }
            }
            return result;
        }

        public static bool ValidatePangram(string sentence)
        {
            return sentence.ToHashSet().Count() == 26;
        }

        public static int LeafRootBinSum(TreeNode root)
        {


            var nodes = new Queue<TreeNode>();
            nodes.Enqueue(root);

            var paths = new Queue<Queue<TreeNode>>();
            var currentQueue = new Stack<TreeNode>();

            while (nodes.Count != 0)
            {
                TreeNode currentNode = nodes.Dequeue();
                currentQueue.Push(currentNode);

                if (currentNode.Left == null && currentNode.Right == null)
                {
                    foreach(var v in currentQueue)
                    {
                        Console.WriteLine(v.Value);
                    }

                    currentQueue.Pop();
                    
                    Console.WriteLine();
                }

                //currentQueue.Enqueue(currentNode);

                if (currentNode.Left != null)
                {
                    nodes.Enqueue(currentNode.Left);
                }

                if (currentNode.Right != null)
                {
                    nodes.Enqueue(currentNode.Right);
                }
            }

            foreach (Queue<TreeNode> q in paths)
            {
                foreach (var a in q)
                {
                    Console.WriteLine(a.Value);
                }

                Console.WriteLine();
            }

            return 0;
        }
    }
}