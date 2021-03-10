using System;

namespace Ex1DaysOfWeek
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] daysOfWeek = { "Monday",
                                    "Tuesday",
                                    "Wednesday",
                                    "Thursday",
                                    "Friday",
                                    "Saturday",
                                    "Sunday"
                                  };

            int dayNum = int.Parse(Console.ReadLine());
            string output = "";
            try
            {
                output = daysOfWeek[dayNum - 1];
            }

            catch (IndexOutOfRangeException)
            {
                output = "Invalid day!";
            }

            Console.WriteLine(output);
        }
    }
}
