using System;
using System.Linq;

namespace QuickSort
{
    internal class Program
    {
        public static int Partition(int[] arr, int left, int right) 
        {
            int pivot;
            pivot = arr[left];
            
            while (true) {
                while (arr[left] < pivot) {
                    left++;
                }
                
                while (arr[right] > pivot) {
                    right--;
                }
                
                if (left < right) {
                    int temp = arr[right];
                    arr[right] = arr[left];
                    arr[left] = temp;
                } else {
                    return right;
                }
            }
        }
        public static void QuickSort(int[] arr, int left, int right) 
        {
            int pivot;
            
            if (left < right) {
                pivot = Partition(arr, left, right);
                
                if (pivot > 1) {
                    QuickSort(arr, left, pivot - 1);
                }  
                if (pivot + 1 < right) {
                    QuickSort(arr, pivot + 1, right);
                }
            }
        }
        
        static void Main(string[] args) {
            int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int n = arr.Length, i;
        
            QuickSort(arr, 0, n - 1);
            
            for (i = 0; i < n; i++) 
            {
                Console.Write(arr[i] + " ");
            }
        }
    }
}