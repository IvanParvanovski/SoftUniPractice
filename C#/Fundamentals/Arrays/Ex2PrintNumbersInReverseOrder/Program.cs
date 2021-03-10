using System;

namespace Ex2PrintNumbersInReverseOrder
{
    class Program
    {
        static void Main(string[] args)
        {
            int numbersCount = int.Parse(Console.ReadLine());
            int[] numbers = new int[numbersCount];

            for (int i = 0; i < numbers.Length; i++)
                numbers[i] = int.Parse(Console.ReadLine());

            Array.Reverse(numbers);
            Console.WriteLine(string.Join(' ', numbers));
        }
    }
}
