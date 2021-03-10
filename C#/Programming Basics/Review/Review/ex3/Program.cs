using System;
using System.Collections.Generic;

namespace ex3
{
    class Program
    {
        static void Main(string[] args)
        {
            double a = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1;
            Console.WriteLine(a);
            double b = 8 * 0.1;
            Console.WriteLine(b);

            if (Math.Abs(a - b) < 0.01)
                Console.WriteLine("Equals");
            else
                Console.WriteLine("Not equals");
        }

        public static string checkFree()
        {
            string checkDayFree = Console.ReadLine();
            int checkHourFree = Int32.Parse(Console.ReadLine());

            if (checkHourFree < 10 || checkHourFree > 22)
                return $"You cannot disturb Maria on {checkDayFree} at {checkHourFree}.";
            
            int workDays = Int32.Parse(Console.ReadLine());

            if (workDays < 3 || workDays > 7)
                return $"{workDays} is invalid number.";

            Dictionary<string, bool> freeDays = new Dictionary<string, bool>();
            freeDays.Add("Monday", true);
            freeDays.Add("Tuesday", true);
            freeDays.Add("Wednesday", true);
            freeDays.Add("Thursday", true);
            freeDays.Add("Friday", true);
            freeDays.Add("Saturday", true);
            freeDays.Add("Sunday", true);

            for (int i = 0; i < workDays; i++)
            {
                string day = Console.ReadLine();
                freeDays[day] = false;
            }

            if (freeDays[checkDayFree])
                return $"Maria is free on {checkDayFree} at {checkHourFree}.";
            else
                return $"Maria isn't free on {checkDayFree} at {checkHourFree}.";
        }
    }
}
