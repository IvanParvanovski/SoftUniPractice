using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2MaximumAndMinimumElement
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<int> numbers = new Stack<int>();
            int amountOfQueries = int.Parse(Console.ReadLine());
            for (int i = 0; i < amountOfQueries; i++)
            {
                int[] data = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
                
                int command = data[0];
                if (command == 1)
                {
                    int element = data[1];
                    numbers.Push(element);
                }
                else if (command == 2)
                {
                    if (numbers.Count > 0)
                    {
                        numbers.Pop();
                    }
                }
                else if (command == 3)
                {
                    if (numbers.Count > 0)
                    {
                        Console.WriteLine(Max(numbers));
                    }
                }
                else if (command == 4)
                {
                    if (numbers.Count > 0)
                    {
                        Console.WriteLine(Min(numbers));
                    }
                }
            }

            Console.WriteLine(string.Join(", ", numbers));
        }

        public static int Max(Stack<int> sequence)
        {
            int result = Int32.MinValue;
            foreach (int num in sequence)
            {
                if (num > result)
                {
                    result = num;
                }
            }

            return result;
        }

        public static int Min(Stack<int> sequence)
        {
            int result = Int32.MaxValue;
            foreach (int num in sequence)
            {
                if (num < result)
                {
                    result = num;
                }
            }

            return result;
        }
        
    }
}