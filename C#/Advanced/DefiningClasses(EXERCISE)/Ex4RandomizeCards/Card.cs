using System;

namespace Ex3ClassCard
{
    public class Card
    {
        public string Face { set; get; }
        public string Suite { set; get; }
        
        public Card(string face, string suite)
        {
            this.Face = face;
            this.Suite = suite;
        }

        public void Print()
        {
            Console.WriteLine($"{this.Face} {this.Suite}");
        }
    }
}