using System;

namespace Ex4RectangleClass
{
    class Rectangle
    {
        private int width;
        private int height;
        private string color;
            
        public Rectangle(int width, int height, string color)
        {
            this.Width = width;
            this.Height = height;
            this.Color = color;
        }

        public int Width
        {
            get => width;
            set => width = value;
        }

        public int Height
        {
            get => height;
            set => height = value;
        }

        public string Color
        {
            get => color;
            set => color = value;
        }

        public double CalculateArea()
        {
            return this.width * this.height;
        }

        public override string ToString()
        {
            return $"Rect({Width}, {Height}, {Color}) has area {CalculateArea()}.";
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            int width = int.Parse(Console.ReadLine()!);
            int height = int.Parse(Console.ReadLine()!);
            string color = Console.ReadLine();

            Rectangle rect = new Rectangle(width, height, color);
            Console.WriteLine(rect);
        }
    }
}