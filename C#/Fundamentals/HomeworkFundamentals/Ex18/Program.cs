using System;
using System.Diagnostics;
using System.Linq;

namespace Ex18
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] fullData = Console.ReadLine()?.Split();
            
            int[] yearPartData = fullData[0].Split('.').Select(int.Parse).ToArray();
            int[] timePartData = fullData[1].Split('.').Select(int.Parse).ToArray();
            
            DateTime time = new DateTime(
                yearPartData[2], yearPartData[1], yearPartData[0], timePartData[0], timePartData[1], timePartData[2]
            );

            Console.WriteLine(time.Date);

            time.AddHours(6.5);
            
            Console.WriteLine(time.Date);
        }
    }
}