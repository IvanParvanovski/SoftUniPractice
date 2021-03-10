namespace Methods
{
    using System;

    class Program
    {
        static void Main(string[] args)
        {
            double length, width, height;

            Console.Write("Length: ");
            length = double.Parse(Console.ReadLine());

            Console.Write("Width: ");
            width = double.Parse(Console.ReadLine());

            Console.Write("Height: ");
            height = double.Parse(Console.ReadLine());

            double volume = length * width / 3 * height;
            Console.WriteLine($"Pyramid Volume: {volume:f2}");
        }


    }
}
