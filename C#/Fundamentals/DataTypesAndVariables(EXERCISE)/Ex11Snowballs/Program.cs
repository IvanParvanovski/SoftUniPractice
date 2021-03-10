using System;
using System.Collections.Generic;

namespace Ex11Snowballs
{
    class Program
    {
        static void Main(string[] args)
        {

            Dictionary<string, double> bestSnowballScore = new Dictionary<string, double>();
            bestSnowballScore.Add("snowballSnow", 0);
            bestSnowballScore.Add("snowballTime", 0);
            bestSnowballScore.Add("snowballQuality", 0);
            bestSnowballScore.Add("snowballValue", int.MinValue);
            int madeBalls = int.Parse(Console.ReadLine());

            

            for (int i = 0; i < madeBalls; i++)
            {
                int snowballSnow = int.Parse(Console.ReadLine());
                int snowballTime = int.Parse(Console.ReadLine());
                int snowballQuality = int.Parse(Console.ReadLine());

                double currentSnowBallValue = CalculateSnowballValue(snowballSnow,
                                                                     snowballTime,
                                                                     snowballQuality);

                if (currentSnowBallValue > bestSnowballScore["snowballValue"])
                {
                    bestSnowballScore["snowballSnow"] = snowballSnow;
                    bestSnowballScore["snowballTime"] = snowballTime;
                    bestSnowballScore["snowballQuality"] = snowballQuality;
                    bestSnowballScore["snowballValue"] = currentSnowBallValue;
                }
            }

            Console.Write($"{bestSnowballScore["snowballSnow"]} : " +
                          $"{bestSnowballScore["snowballTime"]} = " +
                          $"{bestSnowballScore["snowballValue"]} " +
                          $"({bestSnowballScore["snowballQuality"]})");
        }

        private static double CalculateSnowballValue(double snowballSnow,
                                                     double snowballTime,
                                                     double snowballQuality)
        {
            return Math.Pow(snowballSnow / snowballTime, snowballQuality);
        }
    }
}
