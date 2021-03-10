using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex6CardsGame
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> firstDeck = Console.ReadLine().Split().Select(int.Parse).ToList();
            List<int> secondDeck = Console.ReadLine().Split().Select(int.Parse).ToList();

            while (true)
            {
                if (firstDeck.Count() == 0 ||
                    secondDeck.Count() == 0)
                    break;

                int firstCard = firstDeck[0];
                firstDeck.RemoveAt(0);

                int secondCard = secondDeck[0];
                secondDeck.RemoveAt(0);

                if (firstCard > secondCard)
                    firstDeck.AddRange(new List<int> { firstCard, secondCard });
                else if (firstCard < secondCard)
                    secondDeck.AddRange(new List<int> { secondCard, firstCard });
            }

            string winner = "";
            List<int> winningDeck = new List<int>();

            if (firstDeck.Count() == 0)
            {
                winner = "Second";
                winningDeck = secondDeck;
            }

            else
            {
                winner = "First";
                winningDeck = firstDeck;
            }

            Console.WriteLine($"{winner} player wins! Sum: {winningDeck.Sum()}");
        }
    }
}
