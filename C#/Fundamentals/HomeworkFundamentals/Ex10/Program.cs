using System;
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace Ex10
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // We are living in a yellow submarine. We don't have anything else. Inside the submarine is very tight. So we are drinking all the day. We will move out of it in 5 days.
            // in
            
            // Output:
            // We are living in a yellow submarine.
            // We will move out of it in 5 days.

            // Read user's input, split it, and check if it is not null.
            string[] sentences = Console.ReadLine()?.Split(". ");
            Debug.Assert(sentences != null, nameof(sentences) + " != null");

            // Read searched word.
            string searchedWord = Console.ReadLine();

            // Set up the regular expression.
            string regexPattern = @"\b" + searchedWord + @"\b";
            Regex regex = new Regex(regexPattern);
            
            // Go threw the sentences and print the ones who have the searched word in them.
            foreach (string sentence in sentences)
                if (regex.IsMatch(sentence))
                    Console.WriteLine(sentence);
        }
    }
}