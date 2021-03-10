using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex7ListManipulationAdvanced
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
            bool isChanged = false;
            while (true)
            {
                string input = Console.ReadLine();

                if (input == "end")
                    break;

                string[] commands = input.Split();
                string command = commands[0];

                switch (command)
                {
                    case "Add":
                        isChanged = true;
                        numbers.Add(int.Parse(commands[1]));
                        break;
                    case "Remove":
                        isChanged = true;
                        numbers.Remove(int.Parse(commands[1]));
                        break;
                    case "RemoveAt":
                        isChanged = true;
                        numbers.RemoveAt(int.Parse(commands[1]));
                        break;
                    case "Insert":
                        isChanged = true;
                        numbers.Insert(int.Parse(commands[2]), int.Parse(commands[1]));
                        break;
                    case "Contains":
                        Console.WriteLine(numbers.Contains(int.Parse(commands[1])) ? "Yes" : "No such number");
                        break;
                    case "PrintEven":
                        Console.WriteLine(string.Join(" ", numbers.Where(x => x % 2 == 0).ToList()));
                        break;
                    case "PrintOdd":
                        Console.WriteLine(string.Join(" ", numbers.Where(x => x % 2 != 0).ToList()));
                        break;
                    case "GetSum":
                        Console.WriteLine(numbers.Sum());
                        break;
                    case "Filter":
                        if (commands[1] == "<")
                            Console.WriteLine(string.Join(" ", numbers.Where(x => x < int.Parse(commands[2]))));
                        else if (commands[1] == "<=")
                            Console.WriteLine(string.Join(" ", numbers.Where(x => x <= int.Parse(commands[2]))));
                        else if (commands[1] == ">")
                            Console.WriteLine(string.Join(" ", numbers.Where(x => x > int.Parse(commands[2]))));
                        else if (commands[1] == ">=")
                            Console.WriteLine(string.Join(" ", numbers.Where(x => x >= int.Parse(commands[2]))));
                        break;
                }
            }
            if (isChanged)
                Console.WriteLine(string.Join(" ", numbers));
        }
    
    }
}
