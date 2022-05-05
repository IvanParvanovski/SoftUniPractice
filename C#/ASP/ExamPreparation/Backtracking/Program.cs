// See https://aka.ms/new-console-template for more information

using System;

namespace ExamPreparation 
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Gen01(0, new int[3]);
        }

        public static void Gen01(int index, int[] vector)
        {
            if (index >= vector.Length)
            {
                Console.WriteLine(string.Join(" ", vector));
            }
            else
            {
                for (int i = 0; i <= 1; i++)
                {
                    vector[index] = i;
                    Gen01(index + 1, vector);
                }
            }
        }
    }
}