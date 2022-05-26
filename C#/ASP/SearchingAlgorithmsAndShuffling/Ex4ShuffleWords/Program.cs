// See https://aka.ms/new-console-template for more information

using System;
using System.Linq;

namespace Ex4ShuffleWords
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string[] arr = Console.ReadLine().Split().ToArray();
            int n = arr.Length;
            
            Randomize(arr, n);
        }

        public static void Randomize(string[] arr, int n)
        {
            Random r = new Random();

            for (int i = n - 1; i > 0; i--)
            {
                int j = r.Next(0, i + 1);

                string temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }

            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(arr[i]);
            }
        } 
    }
}