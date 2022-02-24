using System;
using System.Linq;

namespace Ex4GeneratingCombinations
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] elements = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int k = int.Parse(Console.ReadLine());
            
            Combinations(elements, new int[k], 0, 0);
        }

        public static void Combinations(int[] elements, int[] result, int index, int startIndex)
        {
            if (index == result.Length)
            {
                Console.WriteLine(String.Join(" ", result));
                return;
            }

            for (int i = startIndex; i < elements.Length; i++)
            {
                result[index] = elements[i];
                Combinations(elements, result, index + 1, i + 1);
            }
        }
    }
}