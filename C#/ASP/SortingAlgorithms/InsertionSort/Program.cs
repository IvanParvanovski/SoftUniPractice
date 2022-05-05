// See https://aka.ms/new-console-template for more information

using System;
using System.Linq;

namespace InsertionSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] arr = Console.ReadLine()!.Split(" ").Select(int.Parse).ToArray();
            Sort(arr);
            PrintArray(arr);
        }

        public static void Sort(int[] arr)
        {
            int n = arr.Length;

            for (int i = 1; i < n; ++i)
            {
                int key = arr[i];
                int previous = i - 1;

                while (previous >= 0 && arr[previous] > key)
                {
                    arr[previous + 1] = arr[previous];
                    previous -= 1;
                }

                arr[previous + 1] = key;
            }
        }

        public static void PrintArray(int[] arr)
        {
            Console.WriteLine(string.Join(" ", arr));
        }
    }
}