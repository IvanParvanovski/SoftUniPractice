using System;

namespace Ex7
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // Ivan
            // Ivan123567890
            // My name is Ivan Parvanovski
            
            // Add or cut user's input.
            BoundedString result = new BoundedString(Console.ReadLine());
            
            // Print the stdout
            Console.WriteLine(result.Result);
        }
    }
}