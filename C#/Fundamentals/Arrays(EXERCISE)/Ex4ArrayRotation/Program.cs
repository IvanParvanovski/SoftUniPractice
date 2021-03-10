using System;
using System.Linq;

namespace Ex4ArrayRotation
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()
                            .Split()
                            .Select(int.Parse)
                            .ToArray();

            int step = int.Parse(Console.ReadLine());

            int[] changedArray = new int[numbers.Length];
            for (int i = 0; i < numbers.Length; i++)
            {
                int newIndex = i - step; 
                if (newIndex < 0)
                    newIndex += numbers.Length;

                changedArray[newIndex] = numbers[i];
            }

            Console.WriteLine(Join(' ', numbers));
        }
    }
}
