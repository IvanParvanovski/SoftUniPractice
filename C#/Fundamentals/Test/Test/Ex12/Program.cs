using System;
using System.Text.RegularExpressions;

namespace Ex12
{
    class Program
    {
        static void Main(string[] args)
        {
            string regexPattern = @"<>(?<gearName>.*?)<>(?<quantity>\d+)--(?<price>\d+(\.?\d+)?)";
            Regex regex = new Regex(regexPattern);

            Console.WriteLine("Gear bought:");
            double total = 0;
            
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "Run!")
                {
                    break;
                }

                Match result = regex.Match(input);
                if (result.Length > 0)
                {
                    Console.WriteLine(result.Groups["gearName"]);
                    total += double.Parse(result.Groups["price"].ToString()) *
                             int.Parse(result.Groups["quantity"].ToString());
                }
            }

            Console.WriteLine($"Total cost: {total:f2}");
        }
    }
}