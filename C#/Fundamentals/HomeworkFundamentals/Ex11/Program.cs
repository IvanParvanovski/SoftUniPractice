using System;
using System.Diagnostics;
using System.Text;

namespace Ex11
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // C#,CLR,Microsoft
            // Microsoft announced its next generation C# compiler today. It uses advanced parser and special optimizer for the Microsoft CLR.
            
            // Output:
            // ********* announced its next generation ** compiler today. It uses advanced parser and special optimizer for the ********* ***.
            
            // Read the banned words.
            string[] bannedWords = Console.ReadLine()?.Split(',');
            Debug.Assert(bannedWords != null, nameof(bannedWords) + " != null");
            
            // Read user's text.
            StringBuilder text = new StringBuilder(Console.ReadLine());
            
            // Replace the bad words with stars
            foreach (string bannedWord in bannedWords)
                text.Replace(bannedWord, new string('*', bannedWord.Length));
            
            // Print the stdout
            Console.WriteLine(text);
            
            
            
        }
    }
}