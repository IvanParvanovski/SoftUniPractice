using System;
using System.Linq;

namespace Ex4
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());
            ReversedVectors(new int[num], 0);
        }

        public static void ReversedVectors(int[] combination, int index)
        {
            if (index > combination.Length - 1)
            {
                Console.WriteLine(string.Join("", combination.Reverse()));
                return;
            }

            for (int i = 0; i <= 1; i++)
            {
                combination[index] = i;
                ReversedVectors(combination, index + 1);
            }
        }
    }
}