using System.Collections.Generic;

namespace Ex3ClassCard
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Card> cards = new List<Card>
            {
                new Card("A", "Spades"),
                new Card("J", "Diamonds"),
                new Card("Q", "Clubs"),
                new Card("10", "Hearts"),
            };
            
            cards.ForEach(c => c.Print());
        }
    }
}