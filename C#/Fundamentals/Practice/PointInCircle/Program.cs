using System;

namespace PointInCircle
{
    class Program
    {
        class Point
        {
            public string Name  { get; set; }
            public double X { get; set; }
            public double Y { get; set; }

            public Point(string name, double x, double y)
            {
                this.Name = name;
                this.X = x;
                this.Y = y;
            }

            public override string ToString()
            {
                return $"Point({this.Name}, {this.X}, {this.Y})";
            }
        }

        class Circle
        {
            public double Radius { get; set; }
            public Point Center { get; set; }

            public Circle(double radius, Point center)
            {
                this.Radius = radius;
                this.Center = center;
            }
        }

        static void Main(string[] args)
        {
            
        }
    }
}