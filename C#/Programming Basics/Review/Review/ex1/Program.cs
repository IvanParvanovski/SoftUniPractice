using System;
using System.Linq;

namespace ex1
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] numbers = Console.ReadLine().Split().Select(long.Parse).ToArray();

            if (numbers.Length > 1)
            {
                bool areidentical = true;
                for (int index = 1; index < numbers.Length; index++)
                {
                    long currentnum = numbers[index];
                    if (numbers[0] != currentnum)
                    {
                        areidentical = false;
                        break;
                    }
                }

                if (areidentical)
                {
                    Console.WriteLine($"There are {numbers.Length} identical numbers");
                    return;
                }
            }

            for (int i = 0; i < numbers.Length; i++)
            {
                bool isBigger = true;
                long num = numbers[i];

                for (int j = i + 1; j < numbers.Length; j++)
                    if (num <= numbers[j])
                    {
                        isBigger = false;
                        break;
                    }

                if (isBigger)
                    Console.Write($"{num} ");
            }

        }


    }
}