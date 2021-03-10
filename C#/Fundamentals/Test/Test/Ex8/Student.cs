using System;
using System.Collections.Generic;

namespace Ex8
{
    public class Student
    {
        public String Name { get; set; }
        public int Age { get; set; }
        public double Grade { get; set; }

        public Student( string name, int age, double grade)
        {
            this.Name = name;
            this.Age = age;
            this.Grade = grade;
        }
        
        // Student
        //    Name1
        //    Age1
        //    ....

            // public void printName()
        // {
        //     Console.WriteLine(Name);
        // }
        //
        // public int sumGrades(List<int> grades)
        // {
        //     int total = 0;
        //     foreach (int grade in grades)
        //         total += grade;
        //     return total;
        // }

    }
}

