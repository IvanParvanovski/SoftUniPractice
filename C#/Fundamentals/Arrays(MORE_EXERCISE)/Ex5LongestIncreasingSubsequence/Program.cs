using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex5LongestIncreasingSubsequence
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();
            List<int> longestSeq = new List<int>();
            int longestSeqLen = 0;

            for (int i = 0; i < numbers.Length; i++)
            {
                int currentNum = numbers[i];

                List<int> currentSeq = new List<int>();
                currentSeq.Add(currentNum);

                for (int j = i + 1; j < numbers.Length; j++)
                {
                    int nextNum = numbers[j];
                    if (nextNum < currentNum)
                        break;
                    
                    currentSeq.Add(nextNum);
                }

                if (longestSeq.Count() == 0)
                {
                    longestSeq = currentSeq;
                    longestSeqLen = currentSeq.Count();
                    continue;
                }

                List<int> previousSeq = longestSeq.ToList();

                if (currentSeq.Count > longestSeqLen)
                {
                    longestSeq = longestSeq.Take(longestSeq.Count - longestSeqLen).ToList();
                    longestSeq.Concat(currentSeq);
                    longestSeqLen = currentSeq.Count();
                }

                for (int k = 0; k < previousSeq.Count(); k++)
                {
                    int previousElement = previousSeq[k];
                    int currentElement = longestSeq[k];
                }
                

            }

            Console.WriteLine(string.Join(" ", longestSeq));

        }
    }
}
