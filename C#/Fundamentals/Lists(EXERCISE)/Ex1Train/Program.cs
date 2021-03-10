using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1Train
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> wagons = Console.ReadLine().Split().Select(int.Parse).ToList();
            int maxCapacity = int.Parse(Console.ReadLine());

            while (true)
            {
                string user_input = Console.ReadLine();

                if (user_input == "end")
                    break;

                string[] user_input_data = user_input.Split();

                if (user_input_data[0] == "Add")
                    wagons.Add(int.Parse(user_input_data[1]));

                else
                {
                    int passangers = int.Parse(user_input_data[0]);
                    for (int wagon_index = 0; wagon_index < wagons.Count(); wagon_index++)
                        if (wagons[wagon_index] + passangers <= maxCapacity)
                        {
                            wagons[wagon_index] += passangers;
                            break;
                        }
                }
                    
            }

            Console.WriteLine(string.Join(" ", wagons));
        }
    }
}
