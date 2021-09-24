using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3CheckStudents
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> missingStudents = new List<string>();
            int studentsCount = int.Parse(Console.ReadLine());

            for (int i = 0; i < studentsCount; i++)
            {
                string message = Console.ReadLine();
                string[] data = message.Split();
                string name = data[0];
                
                if (data.Contains("not"))
                {
                    if (missingStudents.Contains(name))
                    {
                        Console.WriteLine($"{name} is already in the list!");
                        continue;
                    }
                    
                    missingStudents.Add(name);
                }
                else
                {
                    if (!missingStudents.Contains(name))
                    {
                        continue;
                    }
                    
                    missingStudents.Remove(name);
                    Console.WriteLine($"{name} is in class!");
                }
            }

            Console.WriteLine(string.Join("\n", missingStudents));
        }
    }
}