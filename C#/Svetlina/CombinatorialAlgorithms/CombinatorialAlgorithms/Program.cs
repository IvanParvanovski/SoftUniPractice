namespace CombinatorialAlgorithms
{
    public class Program
    {
        public static void Main(string[] args)
        {
            char[] items = new char[3] { 'X', 'Y', 'Z'};
            int k = 3;

            List<List<char>> result = new List<List<char>>();

            Combinations(items, k, 0, new Stack<char>(), result);

            foreach (var combination in result)
            {
                Console.WriteLine(string.Join(", ", combination));
            }
        }

        static void Combinations(
            char[] items,
            int k,
            int startIndex,
            Stack<char> selectedItems,
            List<List<char>> result)
        {
            if (k == 0)
            {
                var copy = selectedItems.ToList();
                copy.Reverse();

                result.Add(copy);
                return;
            }

            for (int i = startIndex; i < items.Count(); i++)
            {
                selectedItems.Push(items[i]);
                Combinations(items, k - 1, i + 1, selectedItems, result) ;
                selectedItems.Pop();
            }
        }
    }
}