// See https://aka.ms/new-console-template for more information

using System;

namespace Ex2
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string input = Console.ReadLine();
            while (input != "End")
            {
                string[] data = input.Split(" ");
                string firstName = data[0];
                string lastName = data[1];
                string department = data[2];

                switch (department)
                {
                    case "Sales":
                        decimal profits = decimal.Parse(data[3]);
                        SalesEmployee se = new SalesEmployee(firstName, lastName, department, profits);
                        
                        Console.WriteLine(se.ToString());
                        Console.WriteLine($"Receives a salary {se.GetSalary()}.");
                        break;
                    case "Engineering":
                        int years = int.Parse(data[3]);
                        Engineer eg = new Engineer(firstName, lastName, department, years);
                        
                        Console.WriteLine(eg.ToString());
                        Console.WriteLine($"Receives a salary {eg.GetSalary()}.");
                        break;
                    case "Junior":
                        Junior ju = new Junior(firstName, lastName, department);
                        
                        Console.WriteLine(ju.ToString());
                        Console.WriteLine($"Receives a salary {ju.GetSalary()}.");
                        break;
                }

                input = Console.ReadLine();
            }
        }
    }
}