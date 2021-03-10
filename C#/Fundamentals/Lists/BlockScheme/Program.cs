using System;
using System.Collections.Generic;
using System.Linq;

namespace BlockScheme
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> wagons = Console.ReadLine().Split().Select(int.Parse).ToList();
            int maxCapacity = int.Parse(Console.ReadLine());

            while (true)
            {
                string input = Console.ReadLine();

                if (input == "end")
                    break;

                string[] commands = input.Split();
                
                if (commands.Count() == 1)
                {
                    wagons.Add(int.Parse(commands[0]));
                    continue;
                }

                string command = commands[0];
                int passengers = int.Parse(commands[1]);

                if (command == "Add")
                    for (int i = 0; i < wagons.Count; i++)
                        if (CanWagonContainPassengers(wagons[i], passengers, maxCapacity))
                        {
                            wagons[i] += passengers;
                            break;
                        }
            }

            Console.WriteLine(string.Join(" ", wagons));
        }

        private static bool CanWagonContainPassengers(int wagon, int passengers, int maxCapacity)
        {
            return wagon + passengers <= maxCapacity;
        }
    }
}
