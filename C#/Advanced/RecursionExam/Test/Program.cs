using System;

namespace Test
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Gen01(new int[n], 0);
        }
        private static void Gen01(int[] vector, int index)
        {
            if (index > vector.Length - 1)
            {
                Console.WriteLine(String.Join("", vector));
                return;
            }

            for (int i = 0; i <= 1; i++)
            {
                vector[index] = i;
                Gen01(vector, index + 1);
            }
        }
        
    }
}