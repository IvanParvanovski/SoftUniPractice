using System;
using System.Text;

namespace Ex7
{
    class Program
    {
        static void Main(string[] args)
        {
            BoundedString result = new BoundedString(Console.ReadLine());
            Console.WriteLine(result.Result);
        }
    }
}