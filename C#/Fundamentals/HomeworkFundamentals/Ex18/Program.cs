using System;
using System.Linq;

namespace Ex18
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // 20.3.2020 5.56.48
            // 20.3.2020 20.56.48
            // 20.3.2020 1.30.0

            // Read user's date
            string[] fullData = Console.ReadLine()?.Split();
            
            // Separate the attributes from the first part
            int[] firstPart = fullData[0].Split('.')
                                         .Select(int.Parse)
                                         .ToArray();
            
            // Separate the attributes from the second part
            int[] secondPart = fullData[1].Split('.')
                                          .Select(int.Parse)
                                          .ToArray();
            
            // Initialize DateTime variable
            DateTime time = new DateTime(
                firstPart[2], firstPart[1], firstPart[0],
                secondPart[0], secondPart[1], secondPart[2]
            );

            // Add 6:30 hours
            time = time.AddHours(6.5);
            
            // Print the result
            Console.WriteLine($"{time.Day}.{time.Month}.{time.Year} " +
                              $"{time.Hour}.{time.Minute}.{time.Second}");
            
        }
    }
}