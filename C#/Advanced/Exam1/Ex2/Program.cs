using System;

namespace Ex2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] infoTokens = Console.ReadLine()!.Split(", ");
            string title = infoTokens[0];
            string text = infoTokens[1];
            string writer = infoTokens[2];

            News news = new News (title, text, writer);
            int n = int.Parse(Console.ReadLine()!);

            for (int i = 0; i < n; i++)
            {
                string[] commandTokens = Console.ReadLine()!.Split(": ");
                string command = commandTokens[0];
                string value = commandTokens[1];

                switch (command)
                {
                    case "Edit":
                        news.Edit(value);
                        break;
                    case "ChangeWriter":
                        news.ChangeWriter(value);
                        break;
                    case "Rename":
                        news.Rename(value);
                        break;
                }   
            }

            Console.WriteLine(news.ToString());
        }
    }
}