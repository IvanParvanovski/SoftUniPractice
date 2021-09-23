using System;
using System.Linq;

namespace Ex2EverythingInCommon
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] firstNumberSequence = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            int[] secondNumberSequence = Console.ReadLine()!.Split().Select(int.Parse).ToArray();

            (bool areIdentical, int index) = AreIdentical(firstNumberSequence, secondNumberSequence);

            string output;
            if (areIdentical)
            {
                output = "Arrays are identical.\n" + 
                         $"Sum: {firstNumberSequence.Sum()}";
            }
            else
            {
                output = "Arrays are not identical.\n" +
                         $"Found difference at {index} index";
            }

            Console.WriteLine(output);
        }
        
        private static (bool, int) AreIdentical(int[] seq1, int[] seq2)
        {
            for (int i = 0; i < seq1.Length; i++)
            {
                int firstElement = seq1[i];
                int secondElement = seq2[i];

                if (firstElement != secondElement)
                {
                    return (false, i);
                }
            }

            return (true, 0);
        }
    }
}