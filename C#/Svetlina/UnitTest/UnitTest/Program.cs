using System;

namespace UnitTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }

        public int Sum(int[] arr)
        {
            int sum = arr[0];
            for (int i = 0; i < arr.Length; i++)
            {
                sum += arr[i]; 
            }

            return sum;
        }
    }
}

