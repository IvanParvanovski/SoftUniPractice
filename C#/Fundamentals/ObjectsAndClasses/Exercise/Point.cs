using System;

namespace Exercise
{
    public class Point
    {
        public double x;
        public double y;
        public string name;
 
        public void Print()
        {
            Console.WriteLine($"{name}({x}, {y})");
        }
    }
}