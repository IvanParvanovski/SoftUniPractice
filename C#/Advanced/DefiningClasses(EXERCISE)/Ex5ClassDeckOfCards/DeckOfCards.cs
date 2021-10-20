using System;
using System.Collections.Generic;
using Ex3ClassCard;

namespace Ex5ClassDeckOfCards
{
    public class DeckOfCards
    {
        private List<Card> _cards;

        public DeckOfCards(List<Card> cards)
        {
            this._cards = cards;
        }

        public void Add(string face, string suit)
        {
            _cards.Add(new Card(face, suit));
        }

        public void Print()
        {
            _cards[^1].Print();
        }

        public void GetAllCards()
        {
            _cards.ForEach(c => c.Print());
        }

        public void Shuffle()
        {
            _cards = Randomize(_cards);
            GetAllCards();
        }

        public void Clear()
        {
            _cards = new List<Card>();
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