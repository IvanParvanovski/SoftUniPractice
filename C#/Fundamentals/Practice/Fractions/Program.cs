using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace Fractions
{
    class Program
    {
        static void Main(string[] args)
        {
            string regexPattern = @"(?<firstFraction>\d+\/\d+)\s(?<operator>.+?)\s(?<secondPart>(\d+\/\d+)|(\d+(\.\d+)?))";
            Regex regex = new Regex(regexPattern);
            
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "END")
                    break;

                string expression = input;
                Match match = regex.Match(expression!);
                
                if (match.Length == 0)
                {
                    Console.WriteLine("Invalid expression");
                    continue;
                }

                int[] firstFractionData = match.Groups["firstFraction"].ToString()
                                                                       .Split('/')
                                                                       .Select(int.Parse)
                                                                       .ToArray();

                string expressionOperator = match.Groups["operator"].ToString();
                Fraction firstFraction = new Fraction(firstFractionData[0], firstFractionData[1]);
                Fraction secondFraction = new Fraction(1, 1);
                double step = 0;
                
                if (expressionOperator != "^")
                {
                    int[] secondFractionData = match.Groups["secondPart"].ToString()
                        .Split('/')
                        .Select(int.Parse)
                        .ToArray();
                    
                    secondFraction = new Fraction(secondFractionData[0], secondFractionData[1]);
                }
                else
                {
                    step = double.Parse(match.Groups["secondPart"].ToString());
                }

                switch (expressionOperator)
                {
                    case "+":
                        Console.WriteLine(firstFraction + secondFraction);
                        break;
                    case "-":
                        Console.WriteLine(firstFraction - secondFraction);
                        break;
                    case "/":
                        Console.WriteLine(firstFraction / secondFraction);
                        break;
                    case "*":
                        Console.WriteLine(firstFraction * secondFraction);
                        break;
                    case "^":
                        Console.WriteLine(firstFraction ^ step);
                        break;
                    case ">":
                        Console.WriteLine(firstFraction > secondFraction);
                        break;
                    case "<":
                        Console.WriteLine(firstFraction < secondFraction);
                        break;
                    case ">=":
                        Console.WriteLine(firstFraction >= secondFraction);
                        break;
                    case "<=":
                        Console.WriteLine(firstFraction <= secondFraction);
                        break;
                    case "==":
                        Console.WriteLine(firstFraction == secondFraction);
                        break;
                    case "!=":
                        Console.WriteLine(firstFraction != secondFraction);
                        break;
                    default:
                        Console.WriteLine("Invalid operator");
                        break;
                }
            }
        }
    }
}