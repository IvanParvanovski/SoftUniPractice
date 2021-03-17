using System;
using System.Text.RegularExpressions;

namespace Ex2SoftUniBarIncome
{
    class Program
    {
        static void Main(string[] args)
        {
            string regexPattern = @"%(?<name>[A-Z][a-z]+)%.*?<(?<product>\w+)>.*?\|(?<quantity>\d+)\|.*?(?<price>\d+(\.\d+)?)\$";
            Regex regex = new Regex(regexPattern);
            double total = 0;

            while (true)
            {
                string text = Console.ReadLine();
                if (text == "end of shift")
                    break;
                
                Match match = regex.Match(text);
                if (!match.Success)
                    continue;
                
                double cost = double.Parse(match.Groups["price"].ToString()) * 
                               double.Parse(match.Groups["quantity"].ToString());
                
                Console.WriteLine($"{match.Groups["name"]}: " +
                                  $"{match.Groups["product"]} - " +
                                  $"{cost:f2}");

                total += cost;
            }

            Console.WriteLine($"Total income: {total:f2}");
        }
    }
}