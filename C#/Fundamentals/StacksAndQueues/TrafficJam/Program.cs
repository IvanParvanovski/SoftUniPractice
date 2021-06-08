using System;
using System.Collections.Generic;

namespace TrafficJam
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<string> cars = new Queue<string>();
            int carsThatCanPass = int.Parse(Console.ReadLine());
            int totalCars = 0;
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "end")
                {
                    break;
                }

                if (input == "green")
                {
                    for (int i = 0; i < carsThatCanPass; i++)
                    {
                        if (cars.Count > 0)
                        {
                            totalCars++;
                            Console.WriteLine($"{cars.Dequeue()} passed!");
                        }
                        else
                        {
                            break;
                        }
                    }
                }
                else
                {
                    cars.Enqueue(input);
                }
            }

            Console.WriteLine($"{totalCars} cars passed the crossroads.");
        }
    }
}