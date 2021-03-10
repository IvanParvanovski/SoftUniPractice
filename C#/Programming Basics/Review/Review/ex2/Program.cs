using System;

namespace ex2
{
    class Program
    {
        static void Main(string[] args)
        {
            int dailyWage = Int32.Parse(Console.ReadLine());
            int firstWorkPlaceDays = Int32.Parse(Console.ReadLine());
            int salary = dailyWage * 3 + 60 * firstWorkPlaceDays;

            if (firstWorkPlaceDays < 3 || firstWorkPlaceDays > 7)
                Console.WriteLine($"{firstWorkPlaceDays} is invalid number.");
            else
            {
                for (int i = 0; i < firstWorkPlaceDays; i++)
                {
                    string workDay = Console.ReadLine();
                    switch (workDay)
                    {
                        case "Friday":
                        case "Saturday":
                            salary += 9;
                            break;
                    }
                }
                Console.WriteLine($"{salary:f2}");
            }
        }
    }
}
