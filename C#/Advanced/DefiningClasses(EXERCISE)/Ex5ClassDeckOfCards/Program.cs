using System;
using System.Collections.Generic;
using Ex3ClassCard;

namespace Ex5ClassDeckOfCards
{
    class Program
    {
        static void Main(string[] args)
        {
            DeckOfCards deckOfCards = new DeckOfCards(new List<Card>());
            
            while (true)
            {
                string input = Console.ReadLine();

                if (input == "End")
                {
                    break;
                }

                string[] commandTokens = input!.Split(" ");
                string command = commandTokens[0];

                switch (command)
                {
                    case "Add":
                        string face = commandTokens[1];
                        string suit = commandTokens[2];
                        
                        deckOfCards.Add(face, suit);
                        break;
                    case "Print":
                        deckOfCards.Print();
                        break;
                    case "Get":
                        deckOfCards.GetAllCards();
                        break;
                    case "Randomize":
                        deckOfCards.Shuffle();
                        break;
                    case "Clear":
                        deckOfCards.Clear();
                        break;
                }
            }
        }
    }
}