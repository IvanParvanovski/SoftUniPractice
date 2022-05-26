// See https://aka.ms/new-console-template for more information

using System;

namespace BubbleSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var numbers = new[] {1, 3, 4, 2, 5, 6};

            for (int i = 0; i < numbers.Length; i++)
            {
                for (int j = 1; j < numbers.Length - i; j++)
                {
                    if (numbers[j - 1] > numbers[j])
                    {
                        Swap(numbers, j - 1, j);
                    }
                }
            }

            Console.WriteLine(string.Join(" ", numbers));
        }
        
        public static void Swap(int[] nums, int index1, int index2)
        {
            int oldNum = nums[index1];
            nums[index1] = nums[index2];
            nums[index2] = oldNum;
        }
    }
}