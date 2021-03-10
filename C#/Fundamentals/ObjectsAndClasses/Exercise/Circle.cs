using System;

namespace Exercise
{
    class Circle
    {
        public Point center;
        public double radius;

        public double Area()
        {
            return Math.PI * Math.Pow(radius, 2);
        }

        public double Perimeter()
        {
            return 2 * Math.PI * radius;
        }

        public void Print()
        {
            Console.WriteLine($"Circle: (({center.x}, {center.y}), {radius})");
        }
    }
}