using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3Articles2
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Article> articles = new List<Article>();
            int articlesCount = int.Parse(Console.ReadLine() ?? string.Empty);

            for (int i = 0; i < articlesCount; i++)
            {
                string[] data = Console.ReadLine()?.Split(", ", StringSplitOptions.RemoveEmptyEntries);
                string title = data?[0];
                string content = data?[1];
                string author = data?[2];

                Article article = new Article(title, content, author);
                articles.Add(article);
            }

            string filterInfo = Console.ReadLine();
            List<Article> orderedArticles = new List<Article>();
            switch (filterInfo)
            {
                case "content":
                    orderedArticles = articles.OrderBy(x => x.Content).ToList();
                    break;  
                case "title":
                    orderedArticles = articles.OrderBy(x => x.Title).ToList();
                    break;
                case "author":
                    orderedArticles = articles.OrderBy(x => x.Author).ToList();
                    break;
            }
            
            foreach (Article article in orderedArticles)
                Console.WriteLine(article);
        }
        
    }
}