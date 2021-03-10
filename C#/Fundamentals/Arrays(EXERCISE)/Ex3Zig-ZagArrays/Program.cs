using System;
using System.Linq;

namespace Ex3Zig_ZagArrays
{
    class Program
    {
        static void Main(string[] args)
        {
            int numbersCount = int.Parse(Console.ReadLine());
            int[] firstArray = new int[numbersCount];
            int[] secondArray = new int[numbersCount];

            for (int i = 0; i < numbersCount; i++)
            {
                int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();
                if (i % 2 == 0)
                {
                    firstArray[i] = numbers[0];
                    secondArray[i] = numbers[1];
                }
                else
                {
                    firstArray[i] = numbers[1];
                    secondArray[i] = numbers[0];
                }
            }

            Console.WriteLine(string.Join(' ', firstArray));
            Console.WriteLine(string.Join(' ', secondArray));
        }
    }
}
