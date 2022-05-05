// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace MergeSort
{
    internal class Program
    {
        public static void Merge(int[] arr, int left, int mid, int right)
        {
            int n1 = mid - left + 1;
            int n2 = right - mid;
      
            int[] leftArray = new int[n1];
            int[] rightArray = new int[n2];
            int i, j;
      
            for (i = 0; i < n1; ++i)
            {
                leftArray[i] = arr[left + i];
            }

            for (j = 0; j < n2; ++j)
            {
                rightArray[j] = arr[mid + 1 + j];
            }
      
            i = 0;
            j = 0;
      
            int k = left;
           
            while (i < n1 && j < n2) {
                if (leftArray[i] <= rightArray[j]) {
                    arr[k] = leftArray[i];
                    i++;
                }
                else {
                    arr[k] = rightArray[j];
                    j++;
                }
                k++;
            }
      
            while (i < n1) {
                arr[k] = leftArray[i];
                i++;
                k++;
            }
      
            while (j < n2) {
                arr[k] = rightArray[j];
                j++;
                k++;
            }
        }
        public static void Sort(int[] arr, int left, int right)
        {
            if (left < right) {
                int mid = left + (right - left)/2;
      
                Sort(arr, left, mid);
                Sort(arr, mid + 1, right);
      
                Merge(arr, left, mid, right);
            }
        }
      
        public static void PrintArray(int[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n; ++i)
            {
                Console.Write(arr[i] + " ");
            }
            Console.WriteLine();
        }
      
        public static void Main(String[] args)
        {
            var arr = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            Sort(arr, 0, arr.Length - 1);
            PrintArray(arr);
        }
    }
}