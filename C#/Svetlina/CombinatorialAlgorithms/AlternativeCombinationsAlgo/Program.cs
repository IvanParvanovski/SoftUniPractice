namespace AlternativeCombinations
{
    public class Program
    {
        public static void Main(string[] args)
        {
            List<char> items = new List<char> { 'A', 'B', 'C', 'D' };
            int k = 4;

            List<List<char>> result = Combinations(items, k);

            foreach (var combination in result)
            {
                Console.WriteLine(string.Join(", ", combination));
            }
        }

        static List<List<T>> Combinations<T>(List<T> items, int k)
        {
            List<List<T>> result = new List<List<T>>();

            CombinationsHelper(items, new List<T>(), 0, k, result);

            return result;
        }

        static void CombinationsHelper<T>(
            List<T> items,
            List<T> selectedItems,
            int startIndex,
            int k,
            List<List<T>> result)
        {
            if (k == 0)
            {
                result.Add(new List<T>(selectedItems));
                return;
            }

            for (int i = startIndex; i < items.Count; i++)
            {
                selectedItems.Add(items[i]);
                CombinationsHelper(items, selectedItems, i + 1, k - 1, result);
                selectedItems.RemoveAt(selectedItems.Count - 1);
            }
        }
    }
}