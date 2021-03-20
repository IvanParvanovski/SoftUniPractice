using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex15
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // .NET – platform for applications from Microsoft
            // CLR – managed execution environment for .NET
            // namespace – hierarchical organization of classes
            // End
            // CLR
            // namespace
            // End
            
            // Set up a dictionary to keep the words + their description
            Dictionary<string, string> words = new Dictionary<string, string>();

            // Add the words and their description in the dictionary 
            while (true)
            {
                string text = Console.ReadLine();
                
                if (text == "End")
                    break;
                
                string[] data = text.Split(" - ");
                words[data[0]] = data[1];
            }

            // Read the searched word and if it ...
            // Exist -> print the description
            // Does not exist -> print missing message
            while (true)
            {
                string searchedWord = Console.ReadLine();
                
                if (searchedWord == "End")
                    break;
                
                try
                {
                    Console.WriteLine(words[searchedWord]);
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine($"The searched word ({searchedWord}) is missing!");
                }
            }
        }
    }
}