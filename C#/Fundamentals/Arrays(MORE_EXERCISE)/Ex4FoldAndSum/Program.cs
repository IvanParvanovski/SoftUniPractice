using System;
using System.Linq;

namespace Ex4FoldAndSum
{
    class Program 
    {
        static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int numbersToGetPerSeq = numbers.Length / 4; 
            GetNumbers(numbers, numbersToGetPerSeq);
        }

        private static void GetNumbers(int[] numbers, int step)
        {
            int n = numbers.Length;
            int[] firstHalf = numbers.Take(n / 2).ToArray();
            int[] secondHalf = numbers.Take(n).Skip(n / 2).ToArray();

            int el = firstHalf.Length;
            int[] leftMidElements = firstHalf.Take(el).Skip(step).ToArray();
            int[] rigthMidElements = secondHalf.Take(step).ToArray();
            int[] midElements = leftMidElements.Concat(rigthMidElements).ToArray();

            int[] leftElements = firstHalf.Take(step).ToArray();
            Array.Reverse(leftElements);

            int[] rigthElements = secondHalf.Take(el).Skip(step).ToArray();
            Array.Reverse(rigthElements);

            int[] otherElements = leftElements.Concat(rigthElements).ToArray();
            
            for (int i = 0; i < otherElements.Length; i++)
                Console.Write(otherElements[i] + midElements[i] + " ");
            
        }
    }
}
