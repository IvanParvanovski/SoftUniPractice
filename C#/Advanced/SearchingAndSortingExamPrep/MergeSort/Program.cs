// See https://aka.ms/new-console-template for more information

using System;

namespace MergeSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] numbers = {2, 8, 9, 7, 3, 12, 45};
            SortArray(numbers, 0, numbers.Length - 1);
            
            Console.WriteLine(string.Join(" ", numbers));
        }

        public static void MergeArray(int[] array, int left, int middle, int right)
        {
            int leftArrayLength = middle - left + 1;
            int rightArrayLength = right - middle;

            var leftTempArray = new int[leftArrayLength];
            var rightTempArray = new int[rightArrayLength];
            int i, j;

            for (i = 0; i < leftArrayLength; ++i)
            {
                leftTempArray[i] = array[left + i];
            }

            for (j = 0; j < rightArrayLength; ++j)
            {
                rightTempArray[j] = array[middle + 1 + j];
            }

            i = 0;
            j = 0;
            int k = left;

            while (i < leftArrayLength && j < rightArrayLength)
            {
                if (leftTempArray[i] <= rightTempArray[j])
                {
                    array[k++] = leftTempArray[i++];
                }
                else
                {
                    array[k++] = rightTempArray[j++];
                }
            }

            while (i < leftArrayLength)
            {
                array[k++] = leftTempArray[i++];
            }

            while (j < rightArrayLength)
            {
                array[k++] = rightTempArray[j++];
            }
        }
        
        public static void SortArray(int[] array, int left, int right)
        {
            if (left < right)
            {
                int middle = left + (right - left) / 2;
                SortArray(array, left, middle);
                SortArray(array, middle + 1, right);
                
                MergeArray(array, left, middle, right);
            }
        }
        
    }
}