using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex5BombNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
            int[] bombData = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int bombPower = bombData[0];
            int bombRange = bombData[1];
         
            while (numbers.Contains(bombPower))
            {
                int bombIndex = numbers.IndexOf(bombPower);

                int maxBombRange = bombRange + bombIndex;
                if (maxBombRange >= numbers.Count())
                    maxBombRange = numbers.Count() - 1;

                int minBombRange = bombIndex - bombRange;
                if (minBombRange < 0)
                    minBombRange = 0;

                for (int i = minBombRange; i < maxBombRange + 1; i++)
                    numbers.RemoveAt(minBombRange);
            }
                      
            Console.WriteLine(numbers.Sum());

        }
    }
}
