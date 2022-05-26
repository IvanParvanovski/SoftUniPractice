// See https://aka.ms/new-console-template for more information

using System;

namespace InsertionSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var nums = new [] {1, 3, 4, 2, 5, 6};

            for (int i = 0; i < nums.Length - 1; i++)
            {
                var currentIndex = i;
                while (currentIndex > 0 && nums[currentIndex] < nums[currentIndex - 1])
                {
                    Swap(nums, currentIndex, currentIndex - 1);
                    currentIndex -= 1;
                }
            }

            Console.WriteLine(string.Join(" ", nums));
        }
        
        public static void Swap(int[] nums, int index1, int index2)
        {
            int oldNum = nums[index1];
            nums[index1] = nums[index2];
            nums[index2] = oldNum;
        }
    }
}