using System;

namespace Ex7WaterOverflow
{
    class Program
    {
        static void Main(string[] args)
        {
            int waterTank = 255;
            int timesToPourWater = Int32.Parse(Console.ReadLine());

            for (int i = 0; i < timesToPourWater; i++)
            {
                int value = int.Parse(Console.ReadLine());
                if (waterTank - value < 0)
                {
                    Console.WriteLine("Insufficient capacity!");
                    continue;
                }

                waterTank -= value;
            }

            Console.WriteLine(255 - waterTank);
        }
    }
}
