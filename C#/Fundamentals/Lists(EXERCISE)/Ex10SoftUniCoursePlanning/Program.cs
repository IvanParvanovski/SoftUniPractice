using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex10SoftUniCoursePlanning
{
    class Program
    {
        static void Main(string[] args)
        {
            
        }

        private static int[] Ex10(int a, int b, int c)
        {
            int[] numbers = new int[c];

            for (int i = 0; i < numbers.Length; i++)
            {
                if (i == 0)
                {
                    numbers[i] = a;
                    continue;
                }

                numbers[i] = a + b * i;
            }

            return numbers;
        }
    }
}