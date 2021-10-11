using System;

namespace Ex1Test
{
    class Program
    {
        static void Main(string[] args)
        {
            ulong totalTime = 0;
            
            ulong amountOfPictures = ulong.Parse(Console.ReadLine()!);
            ulong timeFilterPerPicture = ulong.Parse(Console.ReadLine()!);
            double goodPicturesPercentage = double.Parse(Console.ReadLine()!) / 100.0;
            ulong uploadTime = ulong.Parse(Console.ReadLine()!);

            totalTime += amountOfPictures * timeFilterPerPicture;
            double goodPictures = Math.Ceiling(amountOfPictures * goodPicturesPercentage);
                
            totalTime += (ulong)(goodPictures * uploadTime * 1.0);

            ulong minutes = 0;
            ulong leftSeconds = totalTime;
            if (totalTime >= 60)
            {
                minutes = totalTime / 60;
                leftSeconds = totalTime % 60;
            }

            ulong hours = 0;
            ulong leftMinutes = minutes;
            if (minutes >= 60)
            {
                hours = minutes / 60;
                leftMinutes = minutes % 60;
            }

            ulong days = 0;
            ulong leftHours = hours;
            if (hours >= 24)
            {
                days = minutes / 60;
                leftHours = hours % 60;
            }

            string convertedSeconds = leftSeconds < 10 ? $"0{leftSeconds}" : leftSeconds.ToString();
            string convertedMinutes = leftMinutes < 10 ? $"0{leftMinutes}" : leftMinutes.ToString();
            string convertedHours = leftHours < 10 ? $"0{leftHours}" : leftHours.ToString();
            Console.WriteLine($"{days}:{convertedHours}:{convertedMinutes}:{convertedSeconds}");

            
        }   
    }
}