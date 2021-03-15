using System;
using System.Diagnostics;
using System.Linq;

namespace Ex17
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] firstDateData = Console.ReadLine()?.Split(": ")[1].Split('.').Select(int.Parse).ToArray();
            int[] secondDateData = Console.ReadLine()?.Split(": ")[1].Split('.').Select(int.Parse).ToArray();

            Debug.Assert(firstDateData != null, nameof(firstDateData) + " != null");
            DateTime firstDate = new DateTime(firstDateData[2], firstDateData[1], firstDateData[0]);
            
            Debug.Assert(secondDateData != null, nameof(secondDateData) + " != null");
            DateTime secondDate = new DateTime(secondDateData[2], secondDateData[1], secondDateData[0]);
            
            Console.WriteLine($"Distance: {Math.Abs(firstDate.DayOfYear - secondDate.DayOfYear)}");
        }
    }
}