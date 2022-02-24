using System;

namespace RecursionExam
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());
            DrawFirstPart(0, num);
            DrawSecondPart(1, num);
        }
        public static void DrawFirstPart(int start, int end)
        {
            if (start == end)
            {
                return;
            }
            
            Console.WriteLine(
                new string (' ', start) +
                new string('#', end - start)
            );

            DrawFirstPart(start + 1, end);
        } 
        
        public static void DrawSecondPart(int start, int end)
        {
            if (start == end + 1)
            {
                return;
            }

            Console.WriteLine(
                new string(' ', end - start) +
                new string('*', start)
            );
            
            DrawSecondPart(start + 1, end);
        }
    }
}