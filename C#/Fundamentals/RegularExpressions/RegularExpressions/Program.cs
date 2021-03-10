using System;
using System.Text.RegularExpressions;

namespace RegularExpressions
{
    class Program
    {
        static void Main(string[] args)
        {
            string email = "parvanovski_ivan@abv.bg";
            string regex = @"[a-zA-z]{3,}([0-9]+)?@([a-zA-z]+){3,}(\.[a-zA-Z]+)+";
            Match m = Regex.Match(email, regex);
            
            if (m.Success)
                Console.WriteLine("Valid email!");
            else
                Console.WriteLine("Invalid email!");
            
        }
    }
}
