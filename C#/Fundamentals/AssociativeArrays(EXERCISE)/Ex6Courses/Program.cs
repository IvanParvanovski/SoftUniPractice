using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex6Courses
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, List<string>> courses = new Dictionary<string, List<string>>();
            while (true)
            {
                string userInput = Console.ReadLine();
                if (userInput == "end") break;
                string[] userData = userInput.Split(" : "); 
                string course = userData[0];
                string person = userData[1];

                if (!courses.ContainsKey(course))
                    courses[course] = new List<string>();

                courses[course].Add(person);

            }

            courses = courses.OrderByDescending(x => x.Value.Count).ToDictionary(x => x.Key, x => x.Value);
            foreach (var course in courses)
                course.Value.Sort();

            foreach (var course in courses)
            {
                Console.WriteLine($"{course.Key}: {course.Value.Count}");
                foreach (var person in course.Value)
                    Console.WriteLine($"-- {person}");
            }
        }
    }
}
