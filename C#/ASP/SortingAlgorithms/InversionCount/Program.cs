// See https://aka.ms/new-console-template for more information


using System;
using System.Linq;

namespace InversionCount
{
    internal class Program
    {
        static int[] arr;
 
        static int GetInvCount(int n)
        {
            int invCount = 0;

            for (int i = 0; i < n - 1; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (arr[i] > arr[j])
                    {
                        invCount++;
                    }
                }
            }
            
            return invCount;
        }
 
        // Driver code
        public static void Main()
        {
            arr = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            
            Console.WriteLine(GetInvCount(arr.Length));
        }
    } 
}
