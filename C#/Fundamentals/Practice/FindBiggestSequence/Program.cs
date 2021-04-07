using System;
using System.Collections.Generic;
using System.Linq;

namespace FindBiggestSequence
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()?.Split()
                                               .Select(int.Parse)
                                               .ToArray();

            Console.WriteLine(string.Join(' ', FindBiggestSequence(numbers)));
            Console.WriteLine(string.Join(' ', Test(numbers)));
            
        }
        private static List<int> FindBiggestSequence(int[] numbers)
        {
            List<int> resultSeq = new List<int>();
            List<int> currentSequence = new List<int>();
            int numLen = numbers!.Length;
            
            for (int i = 0; i < numLen; i++)
            {
                int number = numbers[i];
                
                if (currentSequence.Count == 0)
                {
                    currentSequence.Add(number);
                    continue;
                }

                int previousNumber = numbers[i - 1];
                if (number > previousNumber)
                {
                    currentSequence.Add(number);
                    
                    if (i != numLen - 1)
                        continue;
                }
                
                if (currentSequence.Count > resultSeq.Count)
                    resultSeq = currentSequence.ToList();
                currentSequence = new List<int> {number};
            }

            return resultSeq;
        }

        private static List<int> Test(int[] numbers)
        {
            List<int> resultSeq = new List<int>();
            List<int> currentSequence = new List<int>();
            int numLen = numbers!.Length;
            
            for (int i = 0; i < numLen; i++)
            {
                int number = numbers[i];
                int previousNumber;

                try
                {
                    previousNumber = numbers[i - 1];
                }
                catch (IndexOutOfRangeException)
                {
                    currentSequence.Add(number);
                    continue;
                }
                
                if (number > previousNumber)
                {
                    currentSequence.Add(number);
                    
                    if (i != numLen - 1)
                        continue;
                }
                    
                if (currentSequence.Count > resultSeq.Count)
                    resultSeq = currentSequence.ToList();
                currentSequence = new List<int> {number};
            }
            return resultSeq;
        }
    }
    
}