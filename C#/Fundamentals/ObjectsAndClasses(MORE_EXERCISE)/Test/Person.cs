using System;
using System.Collections;
using System.Collections.Generic;

namespace Test
{
    public class Person : IEnumerable
    {
        public int Age { get; set; }

        // private string _name;
        public Person(int age)
        {
            this.Age = age;
        }


        // public string Name
        // {
        //     get => _name;
        //     set
        //     {
        //         if (value == null)
        //             throw new Exception("Error");
        //         _name = value;
        //     }
        // }
        //
        // public string Talk(string word)
        // {
        //     return $"Hello, {word}!";
        // }
        //
        // public static bool operator > (Person a, string b)
        // {
        //     return a.Age > b.Length;
        // }
        //
        // public static bool operator < (Person a, string b)
        // {
        //     return a.Age < b.Length;
        // }
        //
        // public static bool operator > (Person a, int b)
        // {
        //     return a.Age > b;
        // }
        //
        // public static bool operator < (Person a, int b)
        // {
        //     return a.Age < b;
        // }
        //
        // public static bool operator > (Person a, Person b)
        // {
        //     return a > b;
        // }
        //
        // public static bool operator < (Person a, Person b)
        // {
        //     return a < b;
        // }

        // public IEnumerator GetEnumerator()
        // {
        // }
        //
        public IEnumerator GetEnumerator()
        {
            throw new NotImplementedException();
        }
    }
}
