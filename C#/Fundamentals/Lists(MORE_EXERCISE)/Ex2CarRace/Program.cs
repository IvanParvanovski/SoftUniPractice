using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2CarRace
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
            int middle = numbers.Count() / 2;

            List<int> leftPart = numbers.Take(middle).ToList();
            List<int> rightPart = numbers.Take(numbers.Count()).Skip(middle + 1).ToList();

            double leftScore = GetSum(leftPart);
            double rightScore = GetSum(rightPart);

            string winnerScore = "";
            string winnerWord = "";

            if (leftScore < rightScore)
            {
                if (Math.Floor(leftScore) != leftScore)
                    winnerScore = $"{leftScore:f1}";
                else
                    winnerScore = $"{leftScore}";
                winnerWord = "left";
            }

            else
            {
                if (Math.Floor(rightScore) != rightScore)
                    winnerScore = $"{rightScore:f1}";
                else
                    winnerScore = $"{rightScore}";

                winnerWord = "right";
            }

            Console.WriteLine($"The winner is {winnerWord} with total time: {winnerScore}");
        
        }

        public static double GetSum(List<int> numbers)
        {
            double sequenceSum = 0;
            foreach (int num in numbers)
            {
                if (num == 0)
                    sequenceSum -= 20 / 100.0 * sequenceSum;
                else
                    sequenceSum += num;
            }

            return sequenceSum;
        }
    }
}
