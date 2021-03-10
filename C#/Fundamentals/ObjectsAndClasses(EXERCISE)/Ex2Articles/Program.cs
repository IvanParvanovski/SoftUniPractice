using System;

namespace Ex2Articles
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = Console.ReadLine()?.Split(", ", StringSplitOptions.RemoveEmptyEntries);
            Article article = new Article(data?[0], data?[1], data?[2]);
            int commandsCount = int.Parse(Console.ReadLine() ?? string.Empty);
            
            for (int i = 0; i < commandsCount; i++)
            {
                string[] commandData = Console.ReadLine()?.Split(": ", StringSplitOptions.RemoveEmptyEntries);
                string command = commandData?[0];
                string newInfo = commandData?[1];
                
                switch (command)
                {
                    case "Edit":
                        article.Edit(newInfo);
                        break;
                    case "ChangeAuthor":
                        article.ChangeAuthor(newInfo);
                        break;
                    case "Rename":
                        article.Rename(newInfo);
                        break;
                }
            }
            Console.WriteLine(article);
        }
    }
}