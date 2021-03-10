using System;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            Person firstPerson = new Person(10);
            Person secondPerson = new Person(15);
            Console.WriteLine($"FirstPerson Age: {firstPerson.Age}");
            Console.WriteLine($"SecondPerson Age: {secondPerson.Age}");

            firstPerson.Age = 20;
            Console.WriteLine($"FirstPerson Age: {firstPerson.Age}");
            Console.WriteLine($"SecondPerson Age: {secondPerson.Age}");

            // Student myStudent = new Student(5);
            // Console.WriteLine(myStudent.Age);
        }
    }
}