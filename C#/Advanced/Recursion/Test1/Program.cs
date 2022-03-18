using System;
using System.Collections.Generic;
using System.Linq;

namespace Test1
{
    internal class Program
    {
        
        public class  Rect
        {
            
            public int X { get; set; }
            public int Y { get; set; }
            public int Z { get; set; }

            public int[] GetOrderedSides() => (new int[] {X, Y, Z}).OrderByDescending(x => x).ToArray();

        }
        
        public static void Main(string[] args)
        {

            List<Rect> rects = new List<Rect>();
            
            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                var inpt = Console.ReadLine().Split(' ');
                rects.Add(new Rect(){X = int.Parse(inpt[0]), Y = int.Parse(inpt[1]), Z = int.Parse(inpt[2])});
            }
            
            
            
        }

        public static int GetHeight(List<Rect> rects, Rect prevRect)
        {
            if (rects.Count <= 0) return 0;
            if (prevRect is null)
            {
                rects = rects.OrderByDescending(x => x.GetOrderedSides()[0]).ToList();
            }

            return 9;
        }
        
    }
}