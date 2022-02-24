using System;

namespace Ex3CombinationsWithoutRepetition
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int lastElement = int.Parse(Console.ReadLine());
            int totalElements = int.Parse(Console.ReadLine());
            
            Combinations(lastElement, new int[totalElements], 0, 1);
        }

        public static void Combinations(int lastElement, int[] elements, int elIndex, int startIndex)
        {
            if (elIndex == elements.Length)
            {
                Console.WriteLine(String.Join(" ", elements));
                return;
            }

            for (int i = startIndex; i <= lastElement; i++)
            {
                elements[elIndex] = i;
                Combinations(lastElement, elements, elIndex + 1, i + 1);
            }
        }
    }
}