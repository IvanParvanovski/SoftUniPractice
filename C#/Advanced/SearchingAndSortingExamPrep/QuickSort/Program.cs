// See https://aka.ms/new-console-template for more information

using System;

namespace QuickSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] array = {10, 7, 8, 9, 1, 5};
            QuickSort(array, 0, array.Length - 1);
            Console.WriteLine(string.Join(" ", array));
        }

        public static int Partition(int[] array, int low, int high)
        {
            int pivot = array[high];
            int i = low - 1;

            for (int j = low; j < high; j++)
            {
                if (array[j] <= pivot)
                {
                    i += 1;
                    Swap(array, j, i);
                }
            }
            
            Swap(array, high, i + 1);

            return i + 1;
        }

        public static void QuickSort(int[] array, int low, int high)
        {
            if (low < high)
            {
                int pi = Partition(array, low, high);
                
                QuickSort(array, low, pi - 1);
                QuickSort(array, pi + 1, high);
            }
        }
        
        public static void Swap(int[] nums, int index1, int index2)
        {
            int oldNum = nums[index1];
            nums[index1] = nums[index2];
            nums[index2] = oldNum;
        }
    }
}