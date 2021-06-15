using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex5TruckTour
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<int[]> pumps = new Queue<int[]>();
            int pumpsAmount = int.Parse(Console.ReadLine()!);

            for (int i = 0; i < pumpsAmount; i++)
            {
                int[] data = Console.ReadLine()!.Split()
                                                .Select(int.Parse)
                                                .ToArray();
                
                pumps.Enqueue(new int[2]{ data[0], data[1] });
            }
            
            for (int i = 0; i < pumpsAmount; i++)
            {
                int fuel = 0;
                bool isValid = true;

                for (int j = 0; j < pumpsAmount; j++)
                {
                    int[] currentPump = pumps.Dequeue();
                    fuel += currentPump[0] - currentPump[1];

                    if (fuel < 0)
                    {
                        isValid = false;
                    }
                    pumps.Enqueue(currentPump);
                }

                if (isValid)
                {
                    Console.WriteLine(i);
                    break;
                }
                pumps.Enqueue(pumps.Dequeue());
            }
        }
    }
}