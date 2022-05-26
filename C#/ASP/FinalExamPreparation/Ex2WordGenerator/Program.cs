// See https://aka.ms/new-console-template for more information

using System;

namespace Ex2WordGenerator
{
    internal class Program
    {
        private static char[] array;
        
        public static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine()!);
            array = new char[num];
            
            WordGeneration(num, 0);
        }

        private static void WordGeneration(int n, int current)
        {
            if (current >= n)
            {
                Console.WriteLine(string.Join("", array));
                return;
            }

            for (int i = 97; i < 97 + n; i++)
            {
                array[current] = (char)i;
                WordGeneration(n, current + 1);
            }
        }
    }
}