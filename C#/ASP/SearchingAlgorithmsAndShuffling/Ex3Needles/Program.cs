// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3Needles
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] arraysLen = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            
            List<int> numbers = Console.ReadLine()!.Split().Select(int.Parse).ToList();
            List<int> needles = Console.ReadLine()!.Split().Select(int.Parse).ToList();

            
            // Remove zeros
            int prev = numbers[arraysLen[0] - 1];

            for (int i = arraysLen[0] - 1; i >= 0; i--)
            {
                if (numbers[i] == 0)
                {
                    numbers[i] = prev;
                }

                prev = numbers[i];
            }

            // Console.WriteLine(string.Join(" ", numbers));
            
            List<int> result = new List<int>();

            for (int i = 0; i < arraysLen[1]; i++)
            {
                bool isIn = false;
                for (int j = 0; j < numbers.Count; j++)
                {
                    if (numbers[j] >= needles[i])
                    {
                        result.Add(j);
                        isIn = true;
                        
                        break;
                    }
                }

                if (!isIn)
                {
                    int index = numbers.Count - 1;

                    while (index > 0 && numbers[index] == 0)
                    {
                        index--;
                    }

                    if (numbers[index] == 0)
                    {
                        index--;
                    }
                    
                    result.Add(index + 1);
                }
            }
            Console.WriteLine(string.Join(" ", result));
        }
    }
}