using System;

namespace Exercise
{
    class Program
    {
        static void Main(string[] args)
        {
            static double Distance(Point p1, Point p2)
            {
                double d = Math.Sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
                return d;
            }

            static bool IsInCircle(Circle c, Point p)
            {
                double d = Distance(p, c.center);
                if (d <= c.radius)
                {
                    return true;
                }

                return false;
            }

            static bool IsIntersect(Circle c1, Circle c2)
            {
                double cRadius = c1.radius + c2.radius;
                double d = Distance(c1.center, c2.center);
                
                return d < cRadius ? true : false;
            }

            static void Main(string[] args)
            {
                Point c = new Point();
                c.x = 10;
                c.y = 20;

                Circle c1 = new Circle();
                c1.center = c;
                c1.radius = 50;

                Point p2 = new Point();
                p2.x = 10;
                p2.y = 13;

                Console.WriteLine(IsInCircle(c1, p2));

                c1.Print();
            }
        }
    }
}
