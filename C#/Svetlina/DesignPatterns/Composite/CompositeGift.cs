using System;
using System.Collections.Generic;

namespace Composite
{
    public class CompositeGift : GiftBase, IGiftOperations
    {
        private List<GiftBase> _gifts;
        
        public CompositeGift(string name, int price) 
            : base(name, price)
        {
            _gifts = new List<GiftBase>();
        }

        public override int CalculateTotalPrice()
        {
            int total = 0;
            
            Console.WriteLine($"{name} contains the following products with prices:");

            foreach (var gift in _gifts)
            {
                total += gift.CalculateTotalPrice();
            }

            return total;
        }

        public void Add(GiftBase gift)
        {
            _gifts.Add(gift);
        }

        public void Remove(GiftBase gift)
        {
            _gifts.Remove(gift);
        }
    }
}