using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3NothingInCommon
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numberSeq = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            int number = int.Parse(Console.ReadLine()!);

            HashSet<Tuple<int, int>> pairs = new HashSet<Tuple<int, int>>();
            
            for (int i = 0; i < numberSeq.Length; i++)
            {
                int firstNum = numberSeq[i];

                // Console.WriteLine(numberSeq.Where(x => x + firstNum == number));
                
                for (int k = i + 1; k < numberSeq.Length; k++)
                {
                    int secondNum = numberSeq[k];
                    
                    if (firstNum + secondNum == number)
                    {
                        pairs.Add(new Tuple<int, int>(firstNum, secondNum));
                    }
                }
            }

            foreach (Tuple<int, int> pair in pairs)
            {
                Console.WriteLine(pair.Item1 + " " + pair.Item2);
            }
        }
    }
}