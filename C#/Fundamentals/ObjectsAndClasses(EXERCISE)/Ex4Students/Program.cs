using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex4Students
{
    class Program
    {
        static void Main(string[] args)
        {
            int studentCount = int.Parse(Console.ReadLine());
            List<Student> students = new List<Student>();
            for (int i = 0; i < studentCount; i++)
            {
                string[] data = Console.ReadLine()?.Split(' ');
                string firstName = data?[0];
                string lastName = data?[1];
                double grade = double.Parse(data?[2]!);
                
                Student student = new Student(firstName, lastName, grade);
                students.Add(student);
            }

            List<Student> orderedStudents = students.OrderByDescending(x => x.Grade).ToList();

            foreach (Student student in orderedStudents)
                Console.WriteLine(student);
        }
    }
}