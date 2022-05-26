// See https://aka.ms/new-console-template for more information

using System;

namespace SelectionSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var nums = new[] {1, 3, 7, 2, 1, 2};

            for (int start = 0; start < nums.Length - 1; start++)
            {
                int posMin = start;

                for (int next = start + 1; next < nums.Length; next++)
                {
                    if (nums[next] < nums[posMin])
                    {
                        posMin = next;
                    }
                }

                if (posMin != start)
                {
                    Swap(nums, posMin, start);
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