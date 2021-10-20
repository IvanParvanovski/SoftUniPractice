using System;
using System.Collections.Generic;
using Ex3ClassCard;

namespace Ex4RandomizeCards
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] faces = new string[13]
            {
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "A", "J", "Q", "K"
            };

            string[] suites = new string[4]
            {
                "Spades", "Diamonds", "Clubs", "Hearts"
            };

            List<Card> cards = new List<Card>();
            foreach (string face in faces)
            {
                foreach (string suite in suites)
                {
                    cards.Add(new Card(face, suite));
                }
            }

            var randomizedList = Randomize(cards);
            randomizedList.ForEach(c => c.Print());
        }
        
        public static List<T> Randomize<T>(List<T> list)
        {
            List<T> randomizedList = new List<T>();
            Random rnd = new Random();
            while (list.Count > 0)
            {
                int index = rnd.Next(0, list.Count); //pick a random item from the master list
                randomizedList.Add(list[index]); //place it at the end of the randomized list
                list.RemoveAt(index);
            }
            return randomizedList;
        }
    }
}