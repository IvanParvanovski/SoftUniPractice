using System;
using System.Collections.Generic;

namespace Ex1_AdvertismentMessage
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> phrases = new List<string>
            {
                "Excellent product.", 
                "Such a great product.", 
                "I always use that product.",
                "Best product of its category.", 
                "Exceptional product.", 
                "I can’t live without this product."
            };

            List<string> events = new List<string>
            {
                "Now I feel good.",
                "I have succeeded with this product.",
                "Makes miracles. I am happy of the results!",
                "I cannot believe but now I feel awesome.",
                "Try it yourself, I am very satisfied.",
                "I feel great!"
            };
            
            List<string> authors = new List<string>
            {
                "Diana", 
                "Petya", 
                "Stella",
                "Elena",
                "Katya",
                "Iva",
                "Annie",
                "Eva"
            };
            
            List<string> cities = new List<string>
            {
                "Burgas", 
                "Sofia",
                "Plovdiv",
                "Varna",
                "Ruse"
            };
            Random random = new Random();
            
            int phraseNum = random.Next(phrases.Count);
            string cPhrase = phrases[phraseNum];

            int authorNum = random.Next(authors.Count);
            string cAuthor = authors[authorNum];

            int eventNum = random.Next(events.Count);
            string cEvent = events[eventNum];

            int cityNum = random.Next(cities.Count);
            string cCity = cities[cityNum];
            
            Console.WriteLine($"{cPhrase} {cEvent} {cAuthor} - {cCity}");
        }
    }
}