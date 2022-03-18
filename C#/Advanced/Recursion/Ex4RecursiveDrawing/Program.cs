using System;

namespace Ex4RecursiveDrawing
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            FirstPart(n);
            SecondPart(0, n);
        }

        private static void FirstPart(int num)
        {
            if (num == 0)
            {
                return;
            }

            if (num == 1)
            {
                Console.Write(new string('*', num));
            }
            else
            {
                Console.WriteLine(new string('*', num));
            }
            FirstPart(num - 1);
        }

        private static void SecondPart(int index, int num)
        {
            if (index > num)
            {
                return;
            }
            
            Console.WriteLine(new string('#', index));
            SecondPart(index + 1, num);
        }
    }
}