using System;

namespace Ex2_Articles
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = Console.ReadLine()?.Split(", ");
            
            if (data != null)
            {
                Article currentArticle = new Article(data[0], data[1], data[2]);
            }

            int commandsQuantity = int.Parse(Console.ReadLine() ?? string.Empty);

            for (int i = 0; i < commandsQuantity; i++)
            {
                string[] 
            }


        }
    }
}