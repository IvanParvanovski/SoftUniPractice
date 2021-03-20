using System;
using System.Diagnostics;
using System.Linq;

namespace Ex17
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // Enter the first date: 27.02.2006
            // Enter the second date: 3.03.2004
            
            // Read user's input and 
            int[] firstDateData = Console.ReadLine()?.Trim()
                                                     .Split(": ", StringSplitOptions.RemoveEmptyEntries)[1]
                                                     .Split('.', StringSplitOptions.RemoveEmptyEntries)
                                                     .Select(int.Parse)
                                                     .ToArray();
            
            int[] secondDateData = Console.ReadLine()?.Trim()
                                                      .Split(": ", StringSplitOptions.RemoveEmptyEntries)[1]
                                                      .Split('.', StringSplitOptions.RemoveEmptyEntries)
                                                      .Select(int.Parse)
                                                      .ToArray();

            // Check if the first day data is not empty
            Debug.Assert(firstDateData != null, nameof(firstDateData) + " != null");
            
            // Create the first date
            DateTime firstDate = new DateTime(firstDateData[2], firstDateData[1], firstDateData[0]);
            
            // Check if the second day data is not empty
            Debug.Assert(secondDateData != null, nameof(secondDateData) + " != null");
            
            // Create the second date
            DateTime secondDate = new DateTime(secondDateData[2], secondDateData[1], secondDateData[0]);

            // If the year is leap reduce one day
            if (DateTime.IsLeapYear(firstDate.Year))
                secondDate = firstDate.AddDays(-1);

            if (DateTime.IsLeapYear(secondDate.Year))
                secondDate = secondDate.AddDays(-1);
            
            // Print the difference
            Console.WriteLine($"Distance: {Math.Abs(firstDate.DayOfYear - secondDate.DayOfYear)}");
        }
    }
}