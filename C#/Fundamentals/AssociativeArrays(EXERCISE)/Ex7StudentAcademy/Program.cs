using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex7StudentAcademy
{
    class Program
    {
        static void Main(string[] args)
        {
            int people = Int32.Parse(Console.ReadLine());
            Dictionary<string, List<double>> grades = new Dictionary<string, List<double>>();


            for (int i = 0; i < people; i++)
            {
                string name = Console.ReadLine();
                double grade = double.Parse(Console.ReadLine());

                if (!grades.ContainsKey(name))
                    grades[name] = new List<double>();

                grades[name].Add(grade);
            }

            grades = grades.OrderByDescending(x => x.Value.Sum() / x.Value.Count).ToDictionary(x => x.Key, x => x.Value);

            foreach (var person in grades)
            {
                double sum = 0;

                foreach (double grade in person.Value)
                    sum += grade;

                double average = sum / person.Value.Count;

                if (average >= 4.5)
                    Console.WriteLine($"{person.Key} -> {average:f2}");
            }
        }
    }
}
