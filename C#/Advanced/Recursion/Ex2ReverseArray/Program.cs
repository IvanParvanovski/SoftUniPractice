using System;
using System.Linq;
using System.Text;

namespace Ex2ReverseArray
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] numbers = Console.ReadLine()
                .Split()
                .Select(int.Parse)
                .ToArray();

            Console.WriteLine(ReverseArray(numbers, 0));
        }

        private static string ReverseArray(int[] numbers, int index)
        {
            if (numbers.Length / 2 == index)
            {
                StringBuilder sb = new StringBuilder();
                
                foreach (int num in numbers)
                {
                    sb.Append(num);
                    sb.Append(' ');
                }

                return sb.ToString();
            }

            int c = numbers[index];
            int n = numbers.Length - index - 1;
            numbers[index] = numbers[n];
            numbers[n] = c;
            return ReverseArray(numbers, index + 1);
        }
    }
}