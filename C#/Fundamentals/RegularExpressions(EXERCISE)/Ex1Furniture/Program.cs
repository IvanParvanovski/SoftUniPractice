using System;
using System.Text.RegularExpressions;

namespace Ex1Furniture
{
    class Program
    {
        static void Main(string[] args)
        {
            string regexPattern = @">>(?<furnitureName>\w+)<<(?<price>\d+(\.\d+)?)!(?<quantity>\d+)";
            Regex regex = new Regex(regexPattern);
            double total = 0;
            Console.WriteLine("Bought furniture:");

            while (true)
            {
                string text = Console.ReadLine();
                if (text == "Purchase")
                    break;

                Match result = regex.Match(text);
                if (result.Success)
                {
                    Console.WriteLine(result.Groups["furnitureName"]);
                    total += double.Parse(result.Groups["price"].ToString()) * 
                             double.Parse(result.Groups["quantity"].ToString());
                }
            }
            Console.WriteLine($"Total money spend: {total:f2}");
        }
    }
}