using System;
using System.Collections.Generic;
using System.Linq;

namespace StackSum
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<int> numbers = new Stack<int>(Console.ReadLine()!
                                                        .Split()
                                                        .Select(int.Parse));

            while (true)
            {
                string input = Console.ReadLine();
                if (input!.ToLower() == "end")
                {
                    break;
                }

                string[] data = input.Split();
                string command = data[0];

                if (command.ToLower() == "add")
                {
                    int firstNumber = int.Parse(data[1]);
                    int secondNumber = int.Parse(data[2]);
                    numbers.Push(firstNumber);
                    numbers.Push(secondNumber);
                }
                else if (command.ToLower() == "remove")
                {
                    int amountOfNumbers = int.Parse(data[1]);
                    if (numbers.Count < amountOfNumbers)
                        continue;

                    for (int i = 0; i < amountOfNumbers; i++)
                            numbers.Pop();
                }
            }

            Console.WriteLine($"Sum: {numbers.Sum()}");
        }
    }
}