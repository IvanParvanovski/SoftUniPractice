using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Ex1BasicQueueOperations
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] data = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            int amountOfElements = data[0];
            int amountOfElementsToRemove = data[1];
            int searchedItem = data[2];
            
            Queue<int> numbers = new Queue<int>(Console.ReadLine()!.Split().Select(int.Parse));

            for (int i = 0; i < amountOfElementsToRemove; i++)
            {
                numbers.Dequeue();
            }

            if (numbers.Contains(searchedItem))
            {
                Console.WriteLine("true");
            } 
            else if (numbers.Count == 0)
            {
                Console.WriteLine(0);
            }
            else
            {
                int result = Int32.MaxValue;
                foreach (int num in numbers)
                {
                    if (num < result)
                    {
                        result = num;
                    }
                }
                Console.WriteLine(result);
            }
        }
    }
}