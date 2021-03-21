using System;
using System.Collections.Generic;

namespace Ex26
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input: 
            // title
            // body
            // end
            // <html>
            //
            //    <head><title>News</title></head>
            //
            //    <body><p><a href="https://softuni.bg">Telerik
            //
            //     Academy</a>aims to provide free real-world practical
            //
            //     training for young people who want to turn into
            //
            //     skillful .NET software engineers.</p></body>
            //
            // </html>
            // end
            
            // Output:
            // 
            // Title: News
            // Body: Telerik Academy aims to provide free real-world practical training for young people who want to turn into skillful .NET software engineers.


            // Read important tags
            PrintMessage("Type important tags:");
            List<string> importantTags = ReadImportantTags();

            // Read html
            PrintMessage("Type html:");
            string html = ReadHtml();

            // Remove tags, reduce the number of spaces, and add new lines 
            ClearHtml clearedHtml = new ClearHtml(html, importantTags);

            // Print the result
            Console.WriteLine(clearedHtml.Result);
        }

        private static void PrintMessage(string message)
        {
            // Print colored message

            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(message);
            Console.ForegroundColor = ConsoleColor.White;
        }

        private static List<string> ReadImportantTags()
        {
            // Reads important tags such as: <title> and <body>

            List<string> importantTags = new List<string>();
            while (true)
            {
                string importantTag = Console.ReadLine();

                if (importantTag!.ToLower() == "end")
                    break;

                importantTags.Add($@"<(?<TagTitle>{importantTag})>(?<TagData>.*)<\/{importantTag}>");
            }

            return importantTags;
        }

        private static string ReadHtml()
        {
            // Read the html and make it inline

            string result = "";
            while (true)
            {
                string text = Console.ReadLine();

                if (text!.ToLower() == "end")
                    break;

                if (text != "")
                    result += text;
            }

            return result;
        }
    }
}