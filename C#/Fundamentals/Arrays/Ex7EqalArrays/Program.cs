using System;
using System.Linq;

namespace Ex7EqalArrays
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] firstArray = Console.ReadLine()
                              .Split()
                              .Select(int.Parse)
                              .ToArray();


            int[] secondArray = Console.ReadLine()
                                .Split()
                                .Select(int.Parse)
                                .ToArray();

            
            for (int i = 0; i < firstArray.Length; i++)
            {
                int firstArrayNum = firstArray[i];
                int secondArrayNum = secondArray[i];

                if (firstArrayNum != secondArrayNum)
                {
                    Console.WriteLine("Arrays are not identical. " +
                                      $"Found difference at {i} index");
                    return;
                }       
            }

            Console.WriteLine($"Arrays are identical. Sum: {firstArray.Sum()}");
        }
    }
}
