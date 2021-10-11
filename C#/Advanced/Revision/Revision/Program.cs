using System;

namespace Revision
{
    class Program
    {
        static void Main(string[] args)
        {
            
            // Read Properties
            ulong amountOfPictures = ulong.Parse(Console.ReadLine()!);
            ulong timeFilterPerPicture = ulong.Parse(Console.ReadLine()!);
            ulong goodPicturesPercentage = ulong.Parse(Console.ReadLine()!);
            ulong uploadTime = ulong.Parse(Console.ReadLine()!);

            // Set values
            ulong hours = 0;
            ulong minutes = 0;
            ulong day = 0;

            // Operations
            ulong first = amountOfPictures * timeFilterPerPicture;
            ulong second = (ulong)Math.Ceiling(amountOfPictures * (goodPicturesPercentage / 100.0));
            second *= uploadTime;
            ulong seconds = first + second;


            // Conditions
            if (seconds >= 86400)
            {
                day = seconds / 86400;
                seconds -= 86400 * day;
            }
            if (seconds >= 3600)
            {
                hours = seconds / 3600;
                seconds -= 3600 * hours;
            }

            if (seconds >= 60)
            {
                minutes = seconds / 60;
                seconds -= 60 * minutes;
            }

            // Print result
            Console.WriteLine($"{day:0}:{hours:00}:{minutes:00}:{seconds:00}");
        }        
    }
}