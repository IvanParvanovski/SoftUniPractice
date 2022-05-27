// See https://aka.ms/new-console-template for more information

using System;

namespace Ex2SpecialVariations
{
    internal class Program
    {
        private static char[] array;
        
        public static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine()!);
            array = new char[num];
            
            Variation(num, 0);
        }

        public static void Variation(int n, int current)
        {
            if (current >= n)
            {
                Console.WriteLine(string.Join("", array));
                return;
            }

            for (int i = 97; i < 97 + n; i++)
            {
                array[current] = (char)i;
                
                if (current >= 1)
                {
                    if (array[current] >= array[current - 1])
                    {
                        Variation(n, current + 1);
                    }
                }
                else
                {
                    Variation(n, current + 1);
                }
                
            }
        }
    }
}