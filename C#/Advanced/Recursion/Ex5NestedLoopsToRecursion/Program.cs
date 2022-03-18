using System;
using System.Linq;

namespace Ex5NestedLoopsToRecursion
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Combination(new int[n], 0);
        }

        private static void Combination(int[] comb, int index)
        {
            if (index == comb.Length)
            {
                Console.WriteLine(String.Join(" ", comb));
                return;
            }

            for (int i = 1; i <= comb.Length; i++)
            {
                comb[index] = i;
                Combination(comb, index + 1);
            }
        }
    }
}